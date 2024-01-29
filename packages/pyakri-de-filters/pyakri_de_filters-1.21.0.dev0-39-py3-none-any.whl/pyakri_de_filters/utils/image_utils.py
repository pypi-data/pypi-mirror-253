from pathlib import Path
from typing import Tuple

import numpy as np
import PIL
from numpy import ndarray
from PIL import Image
from PIL import ImageFile
from PIL import UnidentifiedImageError
from pyakri_de_filters import logger

ImageFile.LOAD_TRUNCATED_IMAGES = True


def image_exception_handler(func):
    def meth(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except UnidentifiedImageError as ex:
            logger.error("Unknown Image format")
            raise ex
        except Exception as ex:
            logger.error("Failed to load image")
            raise ex

    return meth


class ImageUtils:
    @staticmethod
    @image_exception_handler
    def get_image_from_file(file: Path) -> Image:
        with Image.open(file) as img:
            img.load()
            return img

    @classmethod
    def is_image_corrupted(cls, file: Path):
        try:
            cls.get_image_from_file(file)
            return False
        except Exception:
            return True

    @classmethod
    @image_exception_handler
    def get_image_thumbnail(
        cls, file: Path, resize_dim: Tuple[int, int], resample_algo=Image.BICUBIC
    ) -> Image:
        with Image.open(file) as img:
            img = cls.convert_image_to_rgb(img)
            img.thumbnail(resize_dim, resample=resample_algo)

            return img

    @classmethod
    @image_exception_handler
    def resize_image_file(
        cls,
        file: str,
        resize_dim: Tuple[int, int],
        resample_algo=Image.BICUBIC,
        flatten_img=True,
    ) -> ndarray:
        with Image.open(file) as img:
            return cls.resize(
                img=img,
                resize_dim=resize_dim,
                resample_algo=resample_algo,
                flatten_img=flatten_img,
            )

    @staticmethod
    @image_exception_handler
    def convert_image_to_rgb(img: Image) -> Image:
        return img.convert("RGB")

    @staticmethod
    @image_exception_handler
    def convert_image_to_grayscale(img: Image) -> Image:
        return img.convert("L")

    @staticmethod
    @image_exception_handler
    def get_image_array(img: Image) -> ndarray:
        return np.asarray(img)

    @staticmethod
    @image_exception_handler
    def get_image_from_array(np_image: ndarray, dtype=np.uint8) -> Image:
        return Image.fromarray(np_image.astype(dtype))

    @classmethod
    def resize_image(
        cls,
        img_array: ndarray,
        resize_dim: Tuple[int, int],
        resample_algo=Image.BICUBIC,
        flatten_img=True,
        dtype=np.uint8,
    ) -> ndarray:
        img = cls.get_image_from_array(np_image=img_array, dtype=dtype)
        return cls.resize(
            img=img,
            resize_dim=resize_dim,
            resample_algo=resample_algo,
            flatten_img=flatten_img,
        )

    @staticmethod
    @image_exception_handler
    def resize(
        img: PIL.Image,
        resize_dim: Tuple[int, int],
        resample_algo=Image.BICUBIC,
        flatten_img=True,
    ) -> ndarray:
        img = img.resize(resize_dim, resample=resample_algo)
        im_np = np.array(img)

        if flatten_img:
            im_arr = im_np.flatten()
            im_arr = im_arr / 255
            return im_arr

        return im_np
