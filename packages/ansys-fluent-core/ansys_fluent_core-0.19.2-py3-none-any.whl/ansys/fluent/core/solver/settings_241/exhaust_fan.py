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
from .exhaust_fan_child import exhaust_fan_child

class exhaust_fan(NamedObject[exhaust_fan_child], _NonCreatableNamedObjectMixin[exhaust_fan_child]):
    """
    'exhaust_fan' child.
    """

    fluent_name = "exhaust-fan"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of exhaust_fan.
    """
    list: list_cls = list_cls
    """
    list command of exhaust_fan.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of exhaust_fan.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of exhaust_fan.
    """
    child_object_type: exhaust_fan_child = exhaust_fan_child
    """
    child_object_type of exhaust_fan.
    """
