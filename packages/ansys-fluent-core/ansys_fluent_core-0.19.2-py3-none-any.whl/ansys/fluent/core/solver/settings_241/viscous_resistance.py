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

class viscous_resistance(ListObject[reference_frame_velocity_child]):
    """
    'viscous_resistance' child.
    """

    fluent_name = "viscous-resistance"

    command_names = \
        ['list_properties']

    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of viscous_resistance.
    """
    child_object_type: reference_frame_velocity_child = reference_frame_velocity_child
    """
    child_object_type of viscous_resistance.
    """
