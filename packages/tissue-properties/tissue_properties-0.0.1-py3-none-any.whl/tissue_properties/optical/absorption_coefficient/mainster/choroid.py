import importlib.resources

from ....base_classes import InterpolatedDataModel
from .reference import MainsterModel


class Choroid(InterpolatedDataModel, MainsterModel):
    def __init__(self):
        datafile = importlib.resources.path(__package__, "mua-mainster-choroid.txt")
        super().__init__("absorption coefficient", "1/cm", "wavelength", "nm", datafile)
