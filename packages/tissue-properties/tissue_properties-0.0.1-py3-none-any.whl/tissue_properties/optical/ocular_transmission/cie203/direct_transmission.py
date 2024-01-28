import importlib.resources

from ....base_classes import InterpolatedDataModel
from .reference import CIEModel203


class DirectTransmission(InterpolatedDataModel, CIEModel203):
    def __init__(self):
        datafile = importlib.resources.path(
            __package__, "direct_transmission-human_eye-cie203_2012.txt"
        )
        super().__init__("direct ocular transmission", "", "wavelength", "um", datafile)
