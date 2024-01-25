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
from .defaults_child import defaults_child

class defaults(NamedObject[defaults_child], _NonCreatableNamedObjectMixin[defaults_child]):
    """
    Enter defaults menu.
    """

    fluent_name = "defaults"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of defaults.
    """
    list: list_cls = list_cls
    """
    list command of defaults.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of defaults.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of defaults.
    """
    child_object_type: defaults_child = defaults_child
    """
    child_object_type of defaults.
    """
