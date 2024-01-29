# fix some parameters.
# We always need to apply the crop transform, but before this can be applied,
# we need to convert PIL.Image to Tensor.


import torch
from torchvision.transforms import v2 as transf_v2


class CropAuthorshipInformation(torch.nn.Module):
    """
    The lowest 20 pixels contain the authorship information for the picture
    in the FGVCAircraft dataset. This needs to be removed for training and testing.
    See: https://arxiv.org/pdf/1306.5151.pdf , page 3

    This class crops those last 20 pixel rows. It only works on tensors.
    """

    n_annotation_pixels = 20

    def __init__(
        self,
    ):
        super().__init__()

    def forward(self, x):
        # from the last dimension, drop the last n_annotation_pixels rows.
        return x[..., : -self.n_annotation_pixels]


CROP_TRANSFORM = transf_v2.Compose(
    [
        CropAuthorshipInformation(),
    ]
)
