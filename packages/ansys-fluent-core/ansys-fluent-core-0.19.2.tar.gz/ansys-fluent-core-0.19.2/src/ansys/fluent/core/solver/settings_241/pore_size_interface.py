#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .list_properties import list_properties as list_properties_cls
from .add_zone import add_zone as add_zone_cls
from .list_zone import list_zone as list_zone_cls
from .delete_zone import delete_zone as delete_zone_cls
from .contact_resis_child import contact_resis_child

class pore_size_interface(ListObject[contact_resis_child]):
    """
    Pore Size Interface.
    """

    fluent_name = "pore-size-interface"

    command_names = \
        ['list_properties', 'add_zone', 'list_zone', 'delete_zone']

    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of pore_size_interface.
    """
    add_zone: add_zone_cls = add_zone_cls
    """
    add_zone command of pore_size_interface.
    """
    list_zone: list_zone_cls = list_zone_cls
    """
    list_zone command of pore_size_interface.
    """
    delete_zone: delete_zone_cls = delete_zone_cls
    """
    delete_zone command of pore_size_interface.
    """
    child_object_type: contact_resis_child = contact_resis_child
    """
    child_object_type of pore_size_interface.
    """
