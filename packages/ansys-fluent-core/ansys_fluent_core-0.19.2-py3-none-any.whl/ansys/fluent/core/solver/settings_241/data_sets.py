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
from .data_sets_child import data_sets_child

class data_sets(NamedObject[data_sets_child], _NonCreatableNamedObjectMixin[data_sets_child]):
    """
    Enter data sampling datasets menu.
    """

    fluent_name = "data-sets"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of data_sets.
    """
    list: list_cls = list_cls
    """
    list command of data_sets.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of data_sets.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of data_sets.
    """
    child_object_type: data_sets_child = data_sets_child
    """
    child_object_type of data_sets.
    """
