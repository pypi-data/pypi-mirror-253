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
from .network_end_child import network_end_child

class network_end(NamedObject[network_end_child], _NonCreatableNamedObjectMixin[network_end_child]):
    """
    'network_end' child.
    """

    fluent_name = "network-end"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of network_end.
    """
    list: list_cls = list_cls
    """
    list command of network_end.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of network_end.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of network_end.
    """
    child_object_type: network_end_child = network_end_child
    """
    child_object_type of network_end.
    """
