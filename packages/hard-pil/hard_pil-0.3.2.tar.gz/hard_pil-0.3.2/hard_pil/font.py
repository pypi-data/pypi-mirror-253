import os
from functools import lru_cache

from PIL import ImageFont
from typing_extensions import Literal

fonts_directory = os.path.join(os.path.dirname(__file__), "fonts")


fonts_path = {
    "caveat": {
        "Regular": os.path.join(fonts_directory, "caveat", "caveat.ttf"),
        "Bold": os.path.join(fonts_directory, "caveat", "caveat.ttf"),
        "Italic": os.path.join(fonts_directory, "caveat", "caveat.ttf"),
        "Light": os.path.join(fonts_directory, "caveat", "caveat.ttf"),
    },
    "montserrat": {
        "Regular": os.path.join(fonts_directory, "montserrat", "montserrat_Regular.ttf"),
        "Bold": os.path.join(fonts_directory, "montserrat", "montserrat_Bold.ttf"),
        "Italic": os.path.join(fonts_directory, "montserrat", "montserrat_Italic.ttf"),
        "Light": os.path.join(fonts_directory, "montserrat", "montserrat_Light.ttf"),
    },
    "poppins": {
        "Regular": os.path.join(fonts_directory, "poppins", "poppins_Regular.ttf"),
        "Bold": os.path.join(fonts_directory, "poppins", "poppins_Bold.ttf"),
        "Italic": os.path.join(fonts_directory, "poppins", "poppins_Italic.ttf"),
        "Light": os.path.join(fonts_directory, "poppins", "poppins_Light.ttf"),
    },
    "Lato": {
        "Regular": os.path.join(fonts_directory, "Lato", "Lato-Regular.ttf"),
        "Bold": os.path.join(fonts_directory, "Lato", "Lato-Bold.ttf"),
        "Italic": os.path.join(fonts_directory, "Lato", "Lato-Italic.ttf"),
        "Light": os.path.join(fonts_directory, "Lato", "Lato-Light.ttf"),
    },
    "BarlowCondensed": {
        "Regular": os.path.join(fonts_directory, "BarlowCondensed", "BarlowCondensed-Regular.ttf"),
        "Bold": os.path.join(fonts_directory, "BarlowCondensed", "BarlowCondensed-Bold.ttf"),
        "Italic": os.path.join(fonts_directory, "BarlowCondensed", "BarlowCondensed-Italic.ttf"),
        "Light": os.path.join(fonts_directory, "BarlowCondensed", "BarlowCondensed-Light.ttf"),
    },
}


class Font:
    """Font class

    Parameters
    ----------
    path : str
        Path of font
    size : int, optional
        Size of font, by default 10
    """

    def __init__(self, path: str, size: int = 10, **kwargs) -> None:
        self.font = ImageFont.truetype(path, size=size, **kwargs)

    def getsize(self, text: str):
        bbox = self.font.getbbox(text)
        return bbox[2], bbox[3]

    @staticmethod
    @lru_cache(32)
    def poppins(
        variant: Literal["Regular", "Bold", "Italic", "Light"] = "Regular",
        size: int = 10,
    ):
        """Poppins font

        Parameters
        ----------
        variant : Literal["Regular", "Bold", "Italic", "Light"], optional
            Font variant, by default "Regular"
        size : int, optional
            Font size, by default 10
        """
        return ImageFont.truetype(fonts_path["poppins"][variant], size=size)

    @staticmethod
    @lru_cache(32)
    def caveat(
        variant: Literal["Regular", "Bold", "Italic", "Light"] = "Regular",
        size: int = 10,
    ):
        """Caveat font

        Parameters
        ----------
        variant : Literal["Regular", "Bold", "Italic", "Light"], optional
            Font variant, by default "Regular"
        size : int, optional
            Font size, by default 10
        """
        return ImageFont.truetype(fonts_path["caveat"][variant], size=size)

    @staticmethod
    @lru_cache(32)
    def montserrat(
        variant: Literal["Regular", "Bold", "Italic", "Light"] = "Regular",
        size: int = 10,
    ):
        """Montserrat font

        Parameters
        ----------
        variant : Literal["Regular", "Bold", "Italic", "Light"], optional
            Font variant, by default "Regular"
        size : int, optional
            Font size, by default 10
        """
        return ImageFont.truetype(fonts_path["montserrat"][variant], size=size)
    
    @staticmethod
    @lru_cache(32)
    def Lato(
        variant: Literal["Regular", "Bold", "Italic", "Light"] = "Regular",
        size: int = 10,
    ):
        """Montserrat font

        Parameters
        ----------
        variant : Literal["Regular", "Bold", "Italic", "Light"], optional
            Font variant, by default "Regular"
        size : int, optional
            Font size, by default 10
        """
        return ImageFont.truetype(fonts_path["Lato"][variant], size=size)
    
    @staticmethod
    @lru_cache(32)
    def BarlowCondensed(
        variant: Literal["Regular", "Bold", "Italic", "Light"] = "Regular",
        size: int = 10,
    ):
        """Montserrat font

        Parameters
        ----------
        variant : Literal["Regular", "Bold", "Italic", "Light"], optional
            Font variant, by default "Regular"
        size : int, optional
            Font size, by default 10
        """
        return ImageFont.truetype(fonts_path["BarlowCondensed"][variant], size=size)
