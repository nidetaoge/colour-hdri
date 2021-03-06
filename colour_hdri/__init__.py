# -*- coding: utf-8 -*-
"""
Colour - HDRI
=============

HDRI - Radiance image processing algorithms for *Python*.

Subpackages
-----------
-   calibration: Camera calibration computations.
-   examples: Examples for the sub-packages.
-   generation: HDRI / radiance image generation.
-   models: Colour models conversion.
-   plotting: Diagrams, figures, etc...
-   process: Image conversion helpers.
-   recovery: Clipped highlights recovery.
-   resources: Resources sub-modules.
-   sampling: Image sampling routines.
-   tonemapping: Tonemapping operators.
-   utilities: Various utilities and data structures.
"""

from __future__ import absolute_import

import os

from .utilities import (
    EXIF_EXECUTABLE, ExifTag, adjust_exposure, average_luminance,
    copy_exif_tags, delete_exif_tags, exposure_value, filter_files, Image,
    ImageStack, Metadata, parse_exif_array, parse_exif_data,
    parse_exif_fraction, parse_exif_numeric, parse_exif_string, path_exists,
    read_exif_tag, read_exif_tags, update_exif_tags, vivification,
    vivified_to_dict, write_exif_tag)
from .sampling import (
    light_probe_sampling_variance_minimization_Viriyothai2009,
    samples_Grossberg2003)
from .generation import (normal_distribution_function, hat_function,
                         weighting_function_Debevec1997,
                         image_stack_to_radiance_image)
from .calibration import (absolute_luminance_calibration_Lagarde2016,
                          camera_response_functions_Debevec1997, g_solve,
                          upper_hemisphere_illuminance_weights_Lagarde2016)
from .models import (camera_neutral_to_xy, camera_space_to_RGB,
                     camera_space_to_sRGB, camera_space_to_XYZ_matrix,
                     xy_to_camera_neutral, XYZ_to_camera_space_matrix)
from .process import (DNG_CONVERSION_ARGUMENTS, DNG_CONVERTER,
                      DNG_EXIF_TAGS_BINDING, RAW_CONVERSION_ARGUMENTS,
                      RAW_CONVERTER, RAW_D_CONVERSION_ARGUMENTS,
                      convert_dng_files_to_intermediate_files,
                      convert_raw_files_to_dng_files, read_dng_files_exif_tags)
from .recovery import (highlights_recovery_blend, highlights_recovery_LCHab)
from .tonemapping import (
    tonemapping_operator_exponential,
    tonemapping_operator_exponentiation_mapping, tonemapping_operator_filmic,
    tonemapping_operator_gamma, tonemapping_operator_logarithmic,
    tonemapping_operator_logarithmic_mapping,
    tonemapping_operator_normalisation, tonemapping_operator_Reinhard2004,
    tonemapping_operator_Schlick1994, tonemapping_operator_simple,
    tonemapping_operator_Tumblin1999)

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2015-2018 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = [
    'EXIF_EXECUTABLE', 'ExifTag', 'adjust_exposure', 'average_luminance',
    'copy_exif_tags', 'delete_exif_tags', 'exposure_value', 'filter_files',
    'Image', 'ImageStack', 'Metadata', 'parse_exif_array', 'parse_exif_data',
    'parse_exif_fraction', 'parse_exif_numeric', 'parse_exif_string',
    'path_exists', 'read_exif_tag', 'read_exif_tags', 'update_exif_tags',
    'vivification', 'vivified_to_dict', 'write_exif_tag'
]
__all__ += [
    'light_probe_sampling_variance_minimization_Viriyothai2009',
    'samples_Grossberg2003'
]
__all__ += [
    'normal_distribution_function', 'hat_function',
    'weighting_function_Debevec1997', 'image_stack_to_radiance_image'
]
__all__ += [
    'absolute_luminance_calibration_Lagarde2016',
    'camera_response_functions_Debevec1997', 'g_solve',
    'upper_hemisphere_illuminance_weights_Lagarde2016'
]
__all__ += [
    'camera_neutral_to_xy', 'camera_space_to_RGB', 'camera_space_to_sRGB',
    'camera_space_to_XYZ_matrix', 'xy_to_camera_neutral',
    'XYZ_to_camera_space_matrix'
]
__all__ += [
    'DNG_CONVERSION_ARGUMENTS', 'DNG_CONVERTER', 'DNG_EXIF_TAGS_BINDING',
    'RAW_CONVERSION_ARGUMENTS', 'RAW_CONVERTER', 'RAW_D_CONVERSION_ARGUMENTS',
    'convert_dng_files_to_intermediate_files',
    'convert_raw_files_to_dng_files', 'read_dng_files_exif_tags'
]
__all__ += ['highlights_recovery_blend', 'highlights_recovery_LCHab']
__all__ += [
    'tonemapping_operator_exponential',
    'tonemapping_operator_exponentiation_mapping',
    'tonemapping_operator_filmic', 'tonemapping_operator_gamma',
    'tonemapping_operator_logarithmic',
    'tonemapping_operator_logarithmic_mapping',
    'tonemapping_operator_normalisation', 'tonemapping_operator_Reinhard2004',
    'tonemapping_operator_Schlick1994', 'tonemapping_operator_simple',
    'tonemapping_operator_Tumblin1999'
]

RESOURCES_DIRECTORY = os.path.join(os.path.dirname(__file__), 'resources')
EXAMPLES_RESOURCES_DIRECTORY = os.path.join(RESOURCES_DIRECTORY,
                                            'colour-hdri-examples-dataset')
TESTS_RESOURCES_DIRECTORY = os.path.join(RESOURCES_DIRECTORY,
                                         'colour-hdri-tests-dataset')

__application_name__ = 'Colour - HDRI'

__major_version__ = '0'
__minor_version__ = '1'
__change_version__ = '4'
__version__ = '.'.join(
    (__major_version__,
     __minor_version__,
     __change_version__))  # yapf: disable
