#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import yaml
from pathlib import Path
import os


def list_materials() -> None:
    """
    Prints the list of SellMeier material files.

    :returns:   No return
    :rtype:     None
    """
    cwd = Path(__file__).parent

    material_folder = cwd.joinpath('./material_files')

    list_of_material = os.listdir(material_folder)

    list_of_material = [
        material_name[:-5] + '\n' for material_name in list_of_material
    ]

    print('\n', *list_of_material)


def load_material_parameters(material_name: str) -> dict:
    """
    Loads a material parameters from a yaml file.

    :param      material_name:  The wavelength in unit of meters
    :type       material_name:  str

    :returns:   The material parameters
    :rtype:     dict
    """
    cwd = Path(__file__).parent

    file = cwd.joinpath(f'./material_files/{material_name}.yaml')

    if not file.exists():
        material_folder = cwd.joinpath('./material_files')
        list_of_material = os.listdir(material_folder)
        raise ValueError(
            f'Material file: {file} does not exist. Valid file list is {list_of_material}'
        )

    configuration = yaml.safe_load(file.read_text())

    return configuration


def dispersion_formula(sellmeier_parameters: dict, wavelength: float) -> float:
    """
    Returns refractve index according to the dispersion formula

    :param      sellmeier_parameters:  The sellmeier parameters
    :type       sellmeier_parameters:  dict
    :param      wavelength:            The wavelength in unit of meters
    :type       wavelength:            float

    :returns:   The refractive index
    :rtype:     float
    """
    B_1 = sellmeier_parameters.get('B_1')
    B_2 = sellmeier_parameters.get('B_2')
    B_3 = sellmeier_parameters.get('B_3')
    C_1 = sellmeier_parameters.get('C_1')
    C_2 = sellmeier_parameters.get('C_2')
    C_3 = sellmeier_parameters.get('C_3')

    wavelength *= 1e6  # wavelength converted to micro-meter

    if sellmeier_parameters['C_squared']:
        C_1 = C_1**2
        C_2 = C_2**2
        C_3 = C_3**2

    term_0 = (B_1 * wavelength**2) / (wavelength**2 - C_1**2)
    term_1 = (B_2 * wavelength**2) / (wavelength**2 - C_2**2)
    term_2 = (B_3 * wavelength**2) / (wavelength**2 - C_3**2)

    index_squared = term_0 + term_1 + term_2 + 1

    index = numpy.sqrt(index_squared)

    return index


def get_material_index(material_name: str, wavelength: float) -> float:
    """
    Gets the material refractive index using the dispersion formula.

    :param      material_name:  The material name
    :type       material_name:  str
    :param      wavelength:     The wavelength in unit of meters
    :type       wavelength:     float

    :returns:   The material refractive index.
    :rtype:     float
    """
    material_parameters = load_material_parameters(material_name=material_name)

    index = dispersion_formula(
        sellmeier_parameters=material_parameters['sellmeier'],
        wavelength=wavelength
    )

    return index


def get_silica_index(wavelength: float) -> float:
    """
    Gets the silica refractive index using the dispersion formula.

    :param      material_name:  The material name
    :type       material_name:  str
    :param      wavelength:     The wavelength in unit of meters
    :type       wavelength:     float

    :returns:   The material refractive index.
    :rtype:     float
    """
    index = get_material_index(
        material_name='silica',
        wavelength=wavelength
    )

    return index

# -
