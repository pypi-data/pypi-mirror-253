"""This file contains util functions and a class to define
a repertoire, used to store individuals in the MAP-Elites
algorithm as well as several variants."""

from __future__ import annotations

import warnings
from functools import partial
from typing import Callable, List, Optional, Tuple, Union

import flax
import jax
import jax.numpy as jnp
from flax import struct
from jax.flatten_util import ravel_pytree
from numpy.random import RandomState
from sklearn.cluster import KMeans

from qdax.core.containers.mapelites_repertoire import get_cells_indices, MapElitesRepertoire
from qdax.types import Centroid, Descriptor, ExtraScores, Fitness, Genotype, RNGKey


Threshold = Fitness

class MAERepertoire(MapElitesRepertoire):
    """Class for the repertoire in Map Elites.

    Args:
        genotypes: a PyTree containing all the genotypes in the repertoire ordered
            by the centroids. Each leaf has a shape (num_centroids, num_features). The
            PyTree can be a simple Jax array or a more complex nested structure such
            as to represent parameters of neural network in Flax.
        fitnesses: an array that contains the fitness of solutions in each cell of the
            repertoire, ordered by centroids. The array shape is (num_centroids,).
        descriptors: an array that contains the descriptors of solutions in each cell
            of the repertoire, ordered by centroids. The array shape
            is (num_centroids, num_descriptors).
        centroids: an array that contains the centroids of the tessellation. The array
            shape is (num_centroids, num_descriptors).
    """

    thresholds: Threshold
    archive_learning_rate: float = flax.struct.field(pytree_node=False)

    def save(self, path: str = "./") -> None:
        """Saves the repertoire on disk in the form of .npy files.

        Flattens the genotypes to store it with .npy format. Supposes that
        a user will have access to the reconstruction function when loading
        the genotypes.

        Args:
            path: Path where the data will be saved. Defaults to "./".
        """

        def flatten_genotype(genotype: Genotype) -> jnp.ndarray:
            flatten_genotype, _ = ravel_pytree(genotype)
            return flatten_genotype

        # flatten all the genotypes
        flat_genotypes = jax.vmap(flatten_genotype)(self.genotypes)

        # save data
        jnp.save(path + "genotypes.npy", flat_genotypes)
        jnp.save(path + "fitnesses.npy", self.fitnesses)
        jnp.save(path + "descriptors.npy", self.descriptors)
        jnp.save(path + "centroids.npy", self.centroids)
        jnp.save(path + "thresholds.npy", self.thresholds)

    @classmethod
    def load(cls, reconstruction_fn: Callable, path: str = "./") -> MAERepertoire:
        """Loads a MAP Elites Repertoire.

        Args:
            reconstruction_fn: Function to reconstruct a PyTree
                from a flat array.
            path: Path where the data is saved. Defaults to "./".

        Returns:
            A MAP Elites Repertoire.
        """

        flat_genotypes = jnp.load(path + "genotypes.npy")
        genotypes = jax.vmap(reconstruction_fn)(flat_genotypes)

        fitnesses = jnp.load(path + "fitnesses.npy")
        descriptors = jnp.load(path + "descriptors.npy")
        centroids = jnp.load(path + "centroids.npy")
        thresholds = jnp.load(path + "thresholds.npy")

        return cls(
            genotypes=genotypes,
            fitnesses=fitnesses,
            descriptors=descriptors,
            centroids=centroids,
            thresholds=thresholds,
        )

    @jax.jit
    def add(
        self,
        batch_of_genotypes: Genotype,
        batch_of_descriptors: Descriptor,
        batch_of_fitnesses: Fitness,
        batch_of_extra_scores: Optional[ExtraScores] = None,
    ) -> MAERepertoire:
        """
        Add a batch of elements to the repertoire.

        Args:
            batch_of_genotypes: a batch of genotypes to be added to the repertoire.
                Similarly to the self.genotypes argument, this is a PyTree in which
                the leaves have a shape (batch_size, num_features)
            batch_of_descriptors: an array that contains the descriptors of the
                aforementioned genotypes. Its shape is (batch_size, num_descriptors)
            batch_of_fitnesses: an array that contains the fitnesses of the
                aforementioned genotypes. Its shape is (batch_size,)
            batch_of_extra_scores: unused tree that contains the extra_scores of
                aforementioned genotypes.

        Returns:
            The updated MAP-Elites repertoire.
        """

        batch_of_indices = get_cells_indices(batch_of_descriptors, self.centroids)
        batch_of_indices = jnp.expand_dims(batch_of_indices, axis=-1)
        batch_of_fitnesses = jnp.expand_dims(batch_of_fitnesses, axis=-1)

        num_centroids = self.centroids.shape[0]

        # get fitness segment max
        best_fitnesses = jax.ops.segment_max(
            batch_of_fitnesses,
            batch_of_indices.astype(jnp.int32).squeeze(axis=-1),
            num_segments=num_centroids,
        )

        cond_values = jnp.take_along_axis(best_fitnesses, batch_of_indices, 0)

        # put dominated fitness to -jnp.inf
        batch_of_fitnesses = jnp.where(
            batch_of_fitnesses == cond_values, x=batch_of_fitnesses, y=-jnp.inf
        )

        # get addition condition
        repertoire_thresholds = jnp.expand_dims(self.thresholds, axis=-1)
        current_thresholds_nan = jnp.take_along_axis(
            repertoire_thresholds, batch_of_indices, 0
        )
        current_thresholds = jnp.where(
            jnp.isnan(current_thresholds_nan), x=-jnp.inf, y=current_thresholds_nan
        )
        addition_condition = batch_of_fitnesses > current_thresholds

        # assign fake position when relevant : num_centroids is out of bound
        batch_of_indices = jnp.where(
            addition_condition, x=batch_of_indices, y=num_centroids
        )

        # create new repertoire
        new_repertoire_genotypes = jax.tree_util.tree_map(
            lambda repertoire_genotypes, new_genotypes: repertoire_genotypes.at[
                batch_of_indices.squeeze(axis=-1)
            ].set(new_genotypes),
            self.genotypes,
            batch_of_genotypes,
        )

        # compute new fitness and descriptors
        new_fitnesses = self.fitnesses.at[batch_of_indices.squeeze(axis=-1)].set(
            batch_of_fitnesses.squeeze(axis=-1)
        )

        previous_thresholds = self.thresholds.at[batch_of_indices.squeeze(axis=-1)].get()
        updated_thresholds = jnp.where(jnp.isnan(previous_thresholds), x=batch_of_fitnesses.squeeze(axis=-1), y=previous_thresholds)
        updated_thresholds = updated_thresholds * (1. - self.archive_learning_rate) + batch_of_fitnesses.squeeze(axis=-1) * self.archive_learning_rate

        new_thresholds = self.thresholds.at[batch_of_indices.squeeze(axis=-1)].set(
            updated_thresholds.squeeze(axis=-1)
        )
        new_descriptors = self.descriptors.at[batch_of_indices.squeeze(axis=-1)].set(
            batch_of_descriptors
        )

        return MAERepertoire(
            genotypes=new_repertoire_genotypes,
            fitnesses=new_fitnesses,
            descriptors=new_descriptors,
            centroids=self.centroids,
            thresholds=new_thresholds,
            archive_learning_rate=self.archive_learning_rate,
        )

    @classmethod
    def init(
        cls,
        genotypes: Genotype,
        fitnesses: Fitness,
        descriptors: Descriptor,
        centroids: Centroid,
        archive_learning_rate: float,
        extra_scores: Optional[ExtraScores] = None,
        min_threshold: Optional[float] = None,
    ) -> MAERepertoire:
        """
        Initialize a Map-Elites repertoire with an initial population of genotypes.
        Requires the definition of centroids that can be computed with any method
        such as CVT or Euclidean mapping.

        Note: this function has been kept outside of the object MapElites, so it can
        be called easily called from other modules.

        Args:
            genotypes: initial genotypes, pytree in which leaves
                have shape (batch_size, num_features)
            fitnesses: fitness of the initial genotypes of shape (batch_size,)
            descriptors: descriptors of the initial genotypes
                of shape (batch_size, num_descriptors)
            centroids: tesselation centroids of shape (batch_size, num_descriptors)
            extra_scores: unused extra_scores of the initial genotypes

        Returns:
            an initialized MAP-Elite repertoire
        """
        warnings.warn(
            (
                "This type of repertoire does not store the extra scores "
                "computed by the scoring function"
            ),
            stacklevel=2,
        )

        # retrieve one genotype from the population
        first_genotype = jax.tree_util.tree_map(lambda x: x[0], genotypes)

        # create a repertoire with default values
        repertoire = cls.init_default(genotype=first_genotype, centroids=centroids, archive_learning_rate=archive_learning_rate, min_threshold=min_threshold)

        # add initial population to the repertoire
        new_repertoire = repertoire.add(genotypes, descriptors, fitnesses, extra_scores)

        return new_repertoire  # type: ignore

    @classmethod
    def init_default(
        cls,
        genotype: Genotype,
        centroids: Centroid,
        archive_learning_rate: float,
        min_threshold: Optional[float] = None,
    ) -> MAERepertoire:
        """Initialize a Map-Elites repertoire with an initial population of
        genotypes. Requires the definition of centroids that can be computed
        with any method such as CVT or Euclidean mapping.

        Note: this function has been kept outside of the object MapElites, so
        it can be called easily called from other modules.

        Args:
            genotype: the typical genotype that will be stored.
            centroids: the centroids of the repertoire

        Returns:
            A repertoire filled with default values.
        """

        # get number of centroids
        num_centroids = centroids.shape[0]

        # default fitness is -inf
        default_fitnesses = -jnp.inf * jnp.ones(shape=num_centroids)
        if min_threshold is not None:
            default_thresholds = jnp.full_like(default_fitnesses, min_threshold)
        else:
            default_thresholds = jnp.full_like(default_fitnesses, jnp.nan)

        # default genotypes is all 0
        default_genotypes = jax.tree_util.tree_map(
            lambda x: jnp.zeros(shape=(num_centroids,) + x.shape, dtype=x.dtype),
            genotype,
        )

        # default descriptor is all zeros
        default_descriptors = jnp.zeros_like(centroids)

        return cls(
            genotypes=default_genotypes,
            fitnesses=default_fitnesses,
            descriptors=default_descriptors,
            centroids=centroids,
            thresholds=default_thresholds,
            archive_learning_rate=archive_learning_rate,
        )

def test_with_distance_threshold():
    example_genotype = jnp.asarray([[jnp.inf]])
    example_centroids = jnp.asarray([[0.0, 0.0], [1.0, 1.0], [2.0, 2.0]])
    example_fitnesses = jnp.asarray([0.0, ])
    example_descriptors = jnp.asarray([[0.0, 0.0]])
    example_extra_scores = None
    example_min_threshold = -1.0
    archive_learning_rate = 0.5
    example_repertoire = MAERepertoire.init(
        example_genotype,
        example_fitnesses,
        example_descriptors,
        example_centroids,
        archive_learning_rate,
        example_extra_scores,
        example_min_threshold,
    )
    print(example_repertoire)
    example_repertoire = example_repertoire.add(jnp.asarray([[5]]), example_descriptors, example_fitnesses, example_extra_scores)
    print(example_repertoire)
    example_repertoire = example_repertoire.add(jnp.asarray([[13]]), example_descriptors, jnp.asarray([-0.5]), example_extra_scores)
    print(example_repertoire)


def test_no_min_threshold():
    example_genotype = jnp.asarray([[jnp.inf]])
    example_centroids = jnp.asarray([[0.0, 0.0], [1.0, 1.0], [2.0, 2.0]])
    example_fitnesses = jnp.asarray([0.0, ])
    example_descriptors = jnp.asarray([[0.0, 0.0]])
    example_extra_scores = None
    archive_learning_rate = 0.5
    example_repertoire = MAERepertoire.init(
        example_genotype,
        example_fitnesses,
        example_descriptors,
        example_centroids,
        archive_learning_rate,
        example_extra_scores,
        # No min threshold
    )
    print(example_repertoire)
    example_repertoire = example_repertoire.add(jnp.asarray([[5]]), example_descriptors, example_fitnesses, example_extra_scores)
    print(example_repertoire)
    example_repertoire = example_repertoire.add(jnp.asarray([[13]]), example_descriptors, jnp.asarray([-0.5]), example_extra_scores)
    print(example_repertoire)


if __name__ == "__main__":
    # test_with_distance_threshold()
    test_no_min_threshold()
