from typing import Union
from pathlib import Path
import pydicom
from pydicom.dataset import FileDataset
from rdsr_navigator.sr_element import SrElement


def read_file(file: Union[str, Path, FileDataset], *, warnings:bool=True):
    '''
        Reads the RDSR content of a DICOM file.

        Parameters
        ----------
        file:
            Path to an RDSR file or pydicom FileDataset.
    '''

    if isinstance(file, str):
        return SrElement(pydicom.read_file(file), warnings=warnings)

    if isinstance(file, Path):
        return SrElement(pydicom.read_file(str(file)), warnings=warnings)

    if isinstance(file, FileDataset):
        return SrElement(file, warnings=warnings)

    raise TypeError('Unsupported type. Supported types: str, pathlib.Path, or pydicom.dataset.FileDataset')
