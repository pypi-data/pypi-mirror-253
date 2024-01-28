"""Module for custom loss functions."""
from .frequency_weighted_binary_crossentropy import FrequencyWeightedBinaryCrossEntropy
from .frequency_weighted_categorical_crossentropy import FrequencyWeightedCategoricalCrossEntropy

__all__ = ["FrequencyWeightedBinaryCrossEntropy", "FrequencyWeightedCategoricalCrossEntropy"]
