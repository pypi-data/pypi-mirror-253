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
from .plane_slice_child import plane_slice_child

class plane_slice(NamedObject[plane_slice_child], _CreatableNamedObjectMixin[plane_slice_child]):
    """
    'plane_slice' child.
    """

    fluent_name = "plane-slice"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of plane_slice.
    """
    list: list_cls = list_cls
    """
    list command of plane_slice.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of plane_slice.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of plane_slice.
    """
    child_object_type: plane_slice_child = plane_slice_child
    """
    child_object_type of plane_slice.
    """
