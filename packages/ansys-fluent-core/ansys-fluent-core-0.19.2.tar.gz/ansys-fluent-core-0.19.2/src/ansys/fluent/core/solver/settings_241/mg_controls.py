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
from .mg_controls_child import mg_controls_child

class mg_controls(NamedObject[mg_controls_child], _NonCreatableNamedObjectMixin[mg_controls_child]):
    """
    Enter multi-grid controls menu.
    """

    fluent_name = "mg-controls"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of mg_controls.
    """
    list: list_cls = list_cls
    """
    list command of mg_controls.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of mg_controls.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of mg_controls.
    """
    child_object_type: mg_controls_child = mg_controls_child
    """
    child_object_type of mg_controls.
    """
