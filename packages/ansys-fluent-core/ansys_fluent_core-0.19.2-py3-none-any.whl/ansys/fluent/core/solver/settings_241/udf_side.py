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
from .udf_side_child import udf_side_child

class udf_side(NamedObject[udf_side_child], _CreatableNamedObjectMixin[udf_side_child]):
    """
    Use input parameter in solver-udf.
    """

    fluent_name = "udf-side"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of udf_side.
    """
    list: list_cls = list_cls
    """
    list command of udf_side.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of udf_side.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of udf_side.
    """
    child_object_type: udf_side_child = udf_side_child
    """
    child_object_type of udf_side.
    """
