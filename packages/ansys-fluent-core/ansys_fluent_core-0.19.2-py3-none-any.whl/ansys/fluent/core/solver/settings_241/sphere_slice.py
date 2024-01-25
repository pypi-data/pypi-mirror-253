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
from .sphere_slice_child import sphere_slice_child

class sphere_slice(NamedObject[sphere_slice_child], _CreatableNamedObjectMixin[sphere_slice_child]):
    """
    'sphere_slice' child.
    """

    fluent_name = "sphere-slice"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of sphere_slice.
    """
    list: list_cls = list_cls
    """
    list command of sphere_slice.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of sphere_slice.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of sphere_slice.
    """
    child_object_type: sphere_slice_child = sphere_slice_child
    """
    child_object_type of sphere_slice.
    """
