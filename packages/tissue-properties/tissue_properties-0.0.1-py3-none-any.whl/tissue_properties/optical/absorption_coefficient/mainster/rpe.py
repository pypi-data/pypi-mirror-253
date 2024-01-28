import importlib.resources

from ....base_classes import InterpolatedDataModel
from .reference import MainsterModel


class RPE(InterpolatedDataModel, MainsterModel):
    def __init__(self):
        datafile = importlib.resources.path(__package__, "mua-mainster-rpe.txt")
        super().__init__("absorption coefficient", "1/cm", "wavelength", "nm", datafile)
