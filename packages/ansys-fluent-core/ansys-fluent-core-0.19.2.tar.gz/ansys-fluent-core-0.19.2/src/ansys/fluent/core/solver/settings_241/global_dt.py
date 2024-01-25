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
from .global_dt_child import global_dt_child

class global_dt(NamedObject[global_dt_child], _NonCreatableNamedObjectMixin[global_dt_child]):
    """
    Enter global time step method menu.
    """

    fluent_name = "global-dt"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of global_dt.
    """
    list: list_cls = list_cls
    """
    list command of global_dt.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of global_dt.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of global_dt.
    """
    child_object_type: global_dt_child = global_dt_child
    """
    child_object_type of global_dt.
    """
