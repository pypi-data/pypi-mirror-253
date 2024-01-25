#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .delete_1 import delete as delete_cls
from .list import list as list_cls
from .list_properties_1 import list_properties as list_properties_cls
from .make_a_copy import make_a_copy as make_a_copy_cls
from .reference_frame_velocity_child import reference_frame_velocity_child

class mass_flow_multiplier(NamedObject[reference_frame_velocity_child], _NonCreatableNamedObjectMixin[reference_frame_velocity_child]):
    """
    'mass_flow_multiplier' child.
    """

    fluent_name = "mass-flow-multiplier"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of mass_flow_multiplier.
    """
    list: list_cls = list_cls
    """
    list command of mass_flow_multiplier.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of mass_flow_multiplier.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of mass_flow_multiplier.
    """
    child_object_type: reference_frame_velocity_child = reference_frame_velocity_child
    """
    child_object_type of mass_flow_multiplier.
    """
