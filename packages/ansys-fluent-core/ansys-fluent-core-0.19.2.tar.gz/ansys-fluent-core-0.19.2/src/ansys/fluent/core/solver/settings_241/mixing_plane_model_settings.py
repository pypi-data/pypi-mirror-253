#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .bands_type import bands_type as bands_type_cls
from .number_of_bands import number_of_bands as number_of_bands_cls
from .list_mixing_planes import list_mixing_planes as list_mixing_planes_cls
class mixing_plane_model_settings(Group):
    """
    Set the expert parameters for turbo interfaces.
    """

    fluent_name = "mixing-plane-model-settings"

    child_names = \
        ['bands_type', 'number_of_bands']

    bands_type: bands_type_cls = bands_type_cls
    """
    bands_type child of mixing_plane_model_settings.
    """
    number_of_bands: number_of_bands_cls = number_of_bands_cls
    """
    number_of_bands child of mixing_plane_model_settings.
    """
    command_names = \
        ['list_mixing_planes']

    list_mixing_planes: list_mixing_planes_cls = list_mixing_planes_cls
    """
    list_mixing_planes command of mixing_plane_model_settings.
    """
