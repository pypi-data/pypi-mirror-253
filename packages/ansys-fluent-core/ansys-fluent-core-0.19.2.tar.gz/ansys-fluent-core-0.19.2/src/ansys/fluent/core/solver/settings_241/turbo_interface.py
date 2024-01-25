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
from .turbo_interface_child import turbo_interface_child

class turbo_interface(NamedObject[turbo_interface_child], _CreatableNamedObjectMixin[turbo_interface_child]):
    """
    'turbo_interface' child.
    """

    fluent_name = "turbo-interface"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of turbo_interface.
    """
    list: list_cls = list_cls
    """
    list command of turbo_interface.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of turbo_interface.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of turbo_interface.
    """
    child_object_type: turbo_interface_child = turbo_interface_child
    """
    child_object_type of turbo_interface.
    """
