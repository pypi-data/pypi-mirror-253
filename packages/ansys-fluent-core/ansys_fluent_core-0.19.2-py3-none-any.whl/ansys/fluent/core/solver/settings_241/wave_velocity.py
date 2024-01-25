#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .list_properties import list_properties as list_properties_cls
from .reference_frame_velocity_child import reference_frame_velocity_child

class wave_velocity(ListObject[reference_frame_velocity_child]):
    """
    'wave_velocity' child.
    """

    fluent_name = "wave-velocity"

    command_names = \
        ['list_properties']

    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of wave_velocity.
    """
    child_object_type: reference_frame_velocity_child = reference_frame_velocity_child
    """
    child_object_type of wave_velocity.
    """
