"""Module containing DICOMSource class.

DICOMSource class handles loading of DICOM data.
"""
from __future__ import annotations

import logging
import os
from pathlib import Path
import shutil
from typing import Any, Dict, List, NamedTuple, Optional, Set, TypedDict, Union, cast

from PIL import Image
import numpy as np
import pandas as pd
import pydicom
from typing_extensions import NotRequired

from bitfount.data.datasources.base_source import FileSystemIterableSourceInferrable
from bitfount.utils import delegates

logger = logging.getLogger(__name__)

DICOM_TEXT_REPRESENTATIONS = ["AS", "LO", "LT", "OW", "PN", "SH", "ST", "UN", "UT"]
DICOM_DATETIME = ["DT", "DA"]
DICOM_IMAGE_ATTRIBUTE = "Pixel Data"


class _DICOMField(NamedTuple):
    """Type definition for a DICOM field."""

    name: str
    value: Any


class _DICOMImage(TypedDict):
    """Type definition for a DICOM image.

    None of the fields are required. The only other field-related assumption we are
    making is that if there is a field called "Pixel Data", that must mean there is
    also an attribute called `pixel_array` which is a numpy array. This should be a
    safe assumption based on the pydicom documentation.
    """

    NumberOfFrames: NotRequired[_DICOMField]
    PatientID: NotRequired[_DICOMField]
    StudyDate: NotRequired[_DICOMField]
    StudyTime: NotRequired[_DICOMField]


@delegates()
class DICOMSource(FileSystemIterableSourceInferrable):
    """Data source for loading DICOM files.

    Args:
        path: The path to the directory containing the DICOM files.
        file_extension: The file extension of the DICOM files. Defaults to '.dcm'.
        images_only: If True, only dicom files containing image data will be loaded.
            If the file does not contain any image data, or it does but there was an
            error loading or saving the image(s), the whole file will be skipped.
        **kwargs: Keyword arguments passed to the parent base classes.
    """

    _datetime_columns: Set[str] = set()

    def __init__(
        self,
        path: Union[os.PathLike, str],
        file_extension: Optional[str] = ".dcm",
        images_only: bool = False,
        **kwargs: Any,
    ) -> None:
        super().__init__(path=path, file_extension=file_extension, **kwargs)
        self.images_only = images_only

    def _process_file(
        self, filename: str, full_data: bool, **kwargs: Any
    ) -> List[Dict[str, Any]]:
        """Loads the DICOM file specified by `filename`.

        Args:
            filename: The name of the file to process.
            full_data: True if we're loading all data and want to append to existing
                data.

        Returns:
            The processed DICOM as a dictionary of keys and values within a list
            containing just that element.
        """
        try:
            save_prefix = self._recreate_file_structure(filename, exist_ok=False)
        except FileExistsError:
            # If the directory already exists, this means it has already been parsed
            # and is already part of `self.data` which we will append to our
            # dataframe at the end of this method if `full_data` is True. It doesn't
            # matter if the contents of the directory actually exist or not here.
            if self._data_is_loaded and full_data:
                return []

            # If the data has not been loaded but the file already exists, it must
            # have been created by a previous run. We will therefore load the data
            # from the file and append it to the dataframe.
            else:
                save_prefix = self._recreate_file_structure(filename, exist_ok=True)

        try:
            # This should already return None if there was an error in processing
            # the file
            data = self._process_dicom_file(filename, save_prefix)
        except Exception as e:
            # However, just in case there is an unexpected error that we didn't
            # catch, we will log it here and skip the file.
            logger.warning(f"Unexpected error when processing file {filename}: {e}.")
            # Delete the directory we created for this file
            shutil.rmtree(save_prefix)
            data = None

        # Skip file if specified or empty
        if not data:
            # There should already be another logger message explaining why the file
            # was skipped, so we don't need to log anything extra here.
            logger.warning(f"Skipping file {filename}.")
            self.skipped_files.add(filename)
            return []

        # Skip files that don't contain any image data if images_only is True or
        # simply log this fact if images_only is False as it is not necessarily an
        # error but is probably unexpected.
        if not any(key.startswith(DICOM_IMAGE_ATTRIBUTE) for key in data):
            if self.images_only:
                logger.warning(
                    f"File {filename} does not contain any image data, skipping."
                )
                self.skipped_files.add(filename)
                return []

            logger.warning(
                f"File {filename} does not contain any image data but contains "
                "other data. If this is not expected, please check the file."
            )

        return [data]

    def _process_dataset(self, dataframe: pd.DataFrame, **kwargs: Any) -> pd.DataFrame:
        """Converts the datetime columns to datetime."""
        self._datetime_columns.add("_last_modified")
        return self._convert_datetime_columns(dataframe)

    def _convert_datetime_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Converts the datetime columns to datetime.

        Args:
            df: The dataframe to convert.

        Returns:
            The converted dataframe.
        """
        for col_name in self._datetime_columns:
            try:
                df[col_name] = pd.to_datetime(df[col_name])
            except Exception as e:
                # if not a 'standard' date, get the first 8 characters,
                # assuming it is in the format %Y%m%d. If this doesn't work
                # ignore errors and pass-through the original string.
                logger.debug(
                    f"Field `{col_name}` not in a standard date format. "
                    f"Raised error: `{e}`"
                )
                try:
                    df[col_name] = pd.to_datetime(df[col_name].str[:8], format="%Y%m%d")
                except Exception as e:
                    logger.debug(f"Error when converting to datetime: {e}")
                    logger.warning(
                        f"Field `{col_name}` cannot be loaded as datetime, "
                        "loading as string."
                    )

        return df

    def _process_dicom_file(
        self, filename: str, save_prefix: Path
    ) -> Optional[Dict[str, Any]]:
        """Read and process the dicom file.

        Args:
            filename: The filename of the file to be processed.
            save_prefix: The path to the directory where the images will be saved.
        """
        try:
            ds = pydicom.dcmread(filename, force=True)
        except Exception as e:
            logger.warning(
                f"Skipping file {filename} as it could not be loaded. "
                f"Raised error: {e}."
            )
            return None

        data: Dict[str, Any] = {}
        skip_file = False
        for elem in ds:
            if elem.name not in self._ignore_cols:
                if elem.VR == "SQ":
                    # A DICOM file has different Value Representation (VR).
                    # Unfortunately we cannot support sequence data (SQ)
                    # for using it in dataframes, so we ignore those columns.
                    self._ignore_cols.append(elem.name)
                    logger.info(
                        f"Cannot process sequence data, ignoring column {elem.name}"
                    )
                elif elem.name == DICOM_IMAGE_ATTRIBUTE:
                    try:
                        arr = ds.pixel_array
                    except Exception as e:
                        logger.warning(
                            f"Error when reading pixel data from file {filename}: "
                            f"{e}"
                        )
                        # If we are only loading images, we don't want to add
                        # the file data to the dataframe if there is an error
                        # saving the image.
                        if self.images_only:
                            # Set skip_file to True so we don't add any of the
                            # file data to the dataframe - including fields that
                            # have already been processed.
                            skip_file = True
                            break
                        else:
                            # If we are not only loading images, we will just
                            # continue to the next field instead of breaking
                            continue

                    # Once we have the pixel array, we can cast the dicom image to
                    # the DICOMImage type, which is a TypedDict. This allows us to
                    # access the NumberOfFrames, PatientID, StudyDate and StudyTime
                    # fields with type safety.
                    ds_dict = cast(_DICOMImage, ds)

                    # If the image is 3D, we need to save each frame separately.
                    num_frames = self._get_num_frames(ds_dict, filename)

                    # Get the filename to use when saving the image
                    save_path_filename = self._get_save_path_filename(ds_dict, filename)

                    # If there is just one frame, the loop will simply only run once
                    for iter in range(num_frames):
                        save_path = save_prefix / f"{save_path_filename}-{iter}.png"
                        # Save the image to the specified path and add the path to
                        # the dictionary
                        try:
                            if num_frames > 1:
                                frame_data = arr[iter]
                            else:
                                frame_data = arr
                            data = self._add_image_to_data(
                                ds=ds,
                                data=data,
                                arr=frame_data,
                                save_path=save_path,
                                iter=iter,
                            )
                        except Exception as e:
                            logger.warning(
                                f"Error when saving image {iter} from file "
                                f"{filename}: {e}"
                            )
                            # If we are only loading images, we don't want to add
                            # the file data to the dataframe if there is an error
                            # saving the image, even if there are other frames which
                            # could be saved successfully.
                            if self.images_only:
                                # Set skip_file to True so we don't add any of the
                                # file data to the dataframe - including fields that
                                # have already been processed.
                                skip_file = True
                                break

                    # No need to continue iterating through the file's other fields
                    # if we are only loading images and there was an error saving
                    # an image.
                    if skip_file:
                        break

                elif elem.VR in DICOM_TEXT_REPRESENTATIONS:
                    data[elem.name] = str(elem.value)
                elif elem.VR in DICOM_DATETIME:
                    self._datetime_columns.add(elem.name)
                    data[elem.name] = elem.value
                elif hasattr(elem, "VM") and elem.VM > 1:
                    # The Value Multiplicity of a Data Element specifies the number
                    # of Values that can be encoded in the Value Field of that Data
                    # Element. The VM of each Data Element is specified explicitly
                    # in PS3.6. If the number of Values that may be encoded in a
                    # Data Element is variable, it shall be represented by two
                    # numbers separated by a dash; e.g., "1-10" means that there
                    # may be 1 to 10 Values in the Data Element. Similar to the
                    # SQ case, dataframes do not support sequence data, so we only
                    # take the first element.
                    data[elem.name] = elem[0]
                else:
                    # For all other fields, we just take the value of the column
                    data[elem.name] = elem.value

        if skip_file:
            # Delete the directory we created for this file and
            # stop iterating through the file's other fields
            shutil.rmtree(save_prefix)
            return None

        if not data:
            logger.warning(f"File {filename} is empty.")

        return data

    @staticmethod
    def _get_LUT_value(data: np.ndarray, window: int, level: int) -> np.ndarray:
        """Apply the RGB Look-Up Table for the given data and window/level value."""
        return np.piecewise(
            data,
            [
                data <= (level - 0.5 - (window - 1) / 2),
                data > (level - 0.5 + (window - 1) / 2),
            ],
            [
                0,
                255,
                lambda data: ((data - (level - 0.5)) / (window - 1) + 0.5) * 255,
            ],
        )

    @classmethod
    def _save_image_to_path(
        cls,
        dataset: pydicom.FileDataset,
        pixel_array: np.ndarray,
        filename: Union[Path, str],
    ) -> None:
        """Save the specified pixel array as a PNG image to the specified path.

        Args:
            dataset: The DICOM data.
            pixel_array: The pixel array from the dataset.
            filename: The filepath where to save the image.
        """
        window = 1
        if "WindowWidth" in dataset:
            window = (
                dataset["WindowWidth"].value[0]
                if dataset["WindowWidth"].VM > 1
                else dataset["WindowWidth"].value
            )
            # if Window is 1 will have to divide by 0, which
            # will raise an error, so accounting for this case as well.
        # We can only apply LUT if these window info exists
        if (window == 1) or ("WindowCenter" not in dataset):
            bits = dataset.BitsAllocated
            samples = dataset.SamplesPerPixel
            # Different bits and samples configurations have different
            # modes for loading the images.
            if bits == 8 and samples == 1:
                mode = "L"
            elif bits == 8 and samples == 3:
                mode = "RGB"
            elif bits == 16:
                mode = "I;16"
            else:
                raise TypeError(
                    f"Cannot determine PIL mode for {bits} BitsAllocated "
                    f"and {samples} SamplesPerPixel."
                )

            size = (dataset.Columns, dataset.Rows)
            # Recommended to specify all details
            # by http://www.pythonware.com/library/pil/handbook/image.htm
            im = Image.frombuffer(mode, size, pixel_array, "raw", mode, 0, 1)
            im.save(filename, "PNG", compress_level=0)
        else:
            level = (
                dataset["WindowCenter"].value[0]
                if dataset["WindowCenter"].VM > 1
                else dataset["WindowCenter"].value
            )
            image = cls._get_LUT_value(pixel_array, int(window), int(level))
            # Convert mode to L since LUT has only 256 values:
            #   http://www.pythonware.com/library/pil/handbook/image.htm
            im = Image.fromarray(image).convert("L")
            im.save(filename, "PNG", compress_level=0)

    def _add_image_to_data(
        self,
        ds: pydicom.FileDataset,
        data: Dict[str, Any],
        arr: np.ndarray,
        save_path: Path,
        iter: int,
    ) -> Dict[str, Any]:
        """Add the image to the data dictionary and possibly save it to disk.

        To avoid unnecessary latency, we will only write the raw images to disk if
        Args:
            ds: The DICOM data.
            data: The dictionary containing the data.
            arr: The pixel array from the dataset.
            save_path: The path to the absolute filename where the image will be saved.
            iter: The frame number of the image.

        Returns:
            The updated data dictionary.
        """
        # For each image we assign a column according to the
        # frames order and write in the df the path where
        # the image is saved.They need to be converted to
        # string, so they can be used in the pod's sql database
        image_col_name = f"{DICOM_IMAGE_ATTRIBUTE} {iter}"
        if self.cache_images is True:
            if not save_path.exists():
                # But don't save images again if they have
                # already been saved once.
                self._save_image_to_path(ds, arr, save_path)
            data[image_col_name] = str(save_path)
        else:
            data[image_col_name] = arr
            self.image_columns.add(image_col_name)
        return data

    @staticmethod
    def _get_save_path_filename(image: _DICOMImage, filename: str) -> str:
        """Get the filename to use when saving the image.

        We need to create a unique filename for each image. We use the
        PatientID, StudyDate and StudyTime fields if they are present.
        If not, we just use the original filename but append the frame
        number and use a .png extension.

        Args:
            image: The DICOM image.
            filename: The filename of the file to be processed.

        Returns:
            The filename to use when saving the image.
        """

        try:
            patient_id = str(image["PatientID"].value)
            study_date = str(image["StudyDate"].value)
            study_time = str(image["StudyTime"].value)
            save_path_filename = f"{patient_id}-{study_date}-{study_time}"
        except KeyError:
            save_path_filename = Path(filename).stem

        return save_path_filename

    @staticmethod
    def _get_num_frames(image: _DICOMImage, filename: str) -> int:
        """Get the number of frames in the image.

        If `NumberOfFrames` is not present, we assume it is a 2D image.

        Args:
            image: The DICOM image.
            filename: The filename of the file to be processed.

        Returns:
            The number of frames in the image.
        """

        try:
            num_frames = int(image["NumberOfFrames"].value)
        except KeyError:
            logger.debug(
                f"NumberOfFrames attribute not present on {filename}, "
                "assuming 2D image."
            )
            num_frames = 1

        return num_frames
