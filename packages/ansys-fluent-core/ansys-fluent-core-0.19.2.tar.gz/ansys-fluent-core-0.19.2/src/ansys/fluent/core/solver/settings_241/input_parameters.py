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
from .cone_axis_vector_child import cone_axis_vector_child

class input_parameters(NamedObject[cone_axis_vector_child], _NonCreatableNamedObjectMixin[cone_axis_vector_child]):
    """
    Input Parameter Values of Design Point.
    """

    fluent_name = "input-parameters"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of input_parameters.
    """
    list: list_cls = list_cls
    """
    list command of input_parameters.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of input_parameters.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of input_parameters.
    """
    child_object_type: cone_axis_vector_child = cone_axis_vector_child
    """
    child_object_type of input_parameters.
    """
