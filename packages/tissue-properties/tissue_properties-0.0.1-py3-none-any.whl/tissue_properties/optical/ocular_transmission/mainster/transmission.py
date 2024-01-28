import importlib.resources

from ....base_classes import InterpolatedDataModel
from .reference import MainsterModel


class Transmission(InterpolatedDataModel, MainsterModel):
    def __init__(self):
        datafile = importlib.resources.path(
            __package__, "transmission-human_eye-mainster.txt"
        )
        super().__init__("ocular transmission", "", "wavelength", "nm", datafile)
