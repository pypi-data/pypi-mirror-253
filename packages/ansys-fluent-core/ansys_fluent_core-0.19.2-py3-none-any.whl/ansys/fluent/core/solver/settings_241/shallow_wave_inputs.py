#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .list_properties import list_properties as list_properties_cls
from .shallow_wave_inputs_child import shallow_wave_inputs_child

class shallow_wave_inputs(ListObject[shallow_wave_inputs_child]):
    """
    Shallow Wave Inputs.
    """

    fluent_name = "shallow-wave-inputs"

    command_names = \
        ['list_properties']

    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of shallow_wave_inputs.
    """
    child_object_type: shallow_wave_inputs_child = shallow_wave_inputs_child
    """
    child_object_type of shallow_wave_inputs.
    """
