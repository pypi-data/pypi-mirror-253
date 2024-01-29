"""
Defines the different aircraft classifiers.
"""

import logging
from collections import OrderedDict
from pathlib import Path
from timeit import default_timer as timer
from typing import Optional, Tuple, Any

import torch
import torchvision
from PIL import Image
from torch import nn
from torchvision.transforms import v2 as transf_v2

from transfer_learning_vision_classifiers import classifiers as tlvs_classifiers

from . import aircraft_types as act
from . import parameters


def inverse_of_normalisation_transform(transform):
    """
    Perform inverse of the transf_v2.Normalise transform.

    Useful when wanting to visualise images from the dataset or from the dataloader.
    :param transform:
    :return: Inverse of the normalisation transform.
    """
    if hasattr(transform, "mean"):
        means = transform.mean
        stds = transform.std
        # Create the inverse to std.
        inv_std = transf_v2.Normalize(
            mean=[
                0.0,
                0.0,
                0.0,
            ],
            std=[1.0 / s for s in stds],
        )
        # Create the inverse to de-mean.
        inv_means = transf_v2.Normalize(mean=[-m for m in means], std=[1.0, 1.0, 1.0])
        # First apply inverse to divide by std, then inverse to de-mean,
        # reverse of normalisation operation.
        return transf_v2.Compose([inv_std, inv_means])
    else:
        return transf_v2.Identity()


class AircraftClassifier(tlvs_classifiers.TransferLearningVisionClassifier):
    """
    Contains a classifier for aircraft. It contains a model (nn.Module) and the required transform
    """

    def __init__(
        self,
        model_type: str,
        aircraft_subset_name: str,
        load_classifier_pretrained_weights: bool,
        classifier_pretrained_weights_file: Optional[str | Path] = None,
        data_augmentation_transforms: transf_v2.Transform = transf_v2.Identity(),
    ):
        """
        Initialise an AircraftClassifier.

        :param model_type: "vit_b_16", "vit_l_16", "effnet_b2", "effnet_b7", "trivial"
        :param aircraft_subset_name: name of the aircraft subset ('TEST', 'CIVILIAN_JETS',..).
            Must be one defined in aircraft_types.AIRCRAFT_SUBSETS
        :param load_classifier_pretrained_weights: whether to load classifier
        :param classifier_pretrained_weights_file: file for classifier data
        """
        # Check that aircraft_subset_name is actually defined.
        aircraft_subset_name = aircraft_subset_name.upper()
        assert aircraft_subset_name in act.AIRCRAFT_SUBSETS, (
            f"aircraft_subset_name={aircraft_subset_name} undefined, "
            f"not one of {list(act.AIRCRAFT_SUBSETS.keys())}"
        )
        super().__init__(
            model_type=model_type,
            class_names=act.AIRCRAFT_SUBSETS[aircraft_subset_name],
            load_classifier_pretrained_weights=load_classifier_pretrained_weights,
            classifier_pretrained_weights_file=classifier_pretrained_weights_file,
        )
        self.aircraft_subset_name = aircraft_subset_name.upper()

        # If we train on the FGVCAircraft dataset, we need to implement cropping, same for prediction.
        # If we do prediction on a new picture, crop shouldn't be done.
        # Only the training gets the data augmentation transforms.
        self.train_transform_with_crop = transf_v2.Compose(
            [
                tlvs_classifiers.TO_TENSOR_TRANSFORMS,
                parameters.CropAuthorshipInformation(),
                data_augmentation_transforms,
                self.transforms,
            ]
        )
        self.predict_transform_with_crop = transf_v2.Compose(
            [
                tlvs_classifiers.TO_TENSOR_TRANSFORMS,
                parameters.CropAuthorshipInformation(),
                self.transforms,
            ]
        )
        self.predict_transform_without_crop = transf_v2.Compose(
            [tlvs_classifiers.TO_TENSOR_TRANSFORMS, self.transforms]
        )
        self.inv_of_normalisation = inverse_of_normalisation_transform(self.transforms)
