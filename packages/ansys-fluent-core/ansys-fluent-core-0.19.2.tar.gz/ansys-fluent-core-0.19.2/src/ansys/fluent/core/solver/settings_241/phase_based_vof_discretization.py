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
from .phase_based_vof_discretization_child import phase_based_vof_discretization_child

class phase_based_vof_discretization(NamedObject[phase_based_vof_discretization_child], _NonCreatableNamedObjectMixin[phase_based_vof_discretization_child]):
    """
    Set phase-based vof discretization.
    """

    fluent_name = "phase-based-vof-discretization"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of phase_based_vof_discretization.
    """
    list: list_cls = list_cls
    """
    list command of phase_based_vof_discretization.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of phase_based_vof_discretization.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of phase_based_vof_discretization.
    """
    child_object_type: phase_based_vof_discretization_child = phase_based_vof_discretization_child
    """
    child_object_type of phase_based_vof_discretization.
    """
