#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .active_zone import active_zone as active_zone_cls
from .passive_zone import passive_zone as passive_zone_cls
from .positive_tab import positive_tab as positive_tab_cls
from .negative_tab import negative_tab as negative_tab_cls
from .virtual_connection import virtual_connection as virtual_connection_cls
from .print_battery_connection import print_battery_connection as print_battery_connection_cls
class zone_assignment(Group):
    """
    'zone_assignment' child.
    """

    fluent_name = "zone-assignment"

    child_names = \
        ['active_zone', 'passive_zone', 'positive_tab', 'negative_tab']

    active_zone: active_zone_cls = active_zone_cls
    """
    active_zone child of zone_assignment.
    """
    passive_zone: passive_zone_cls = passive_zone_cls
    """
    passive_zone child of zone_assignment.
    """
    positive_tab: positive_tab_cls = positive_tab_cls
    """
    positive_tab child of zone_assignment.
    """
    negative_tab: negative_tab_cls = negative_tab_cls
    """
    negative_tab child of zone_assignment.
    """
    command_names = \
        ['virtual_connection', 'print_battery_connection']

    virtual_connection: virtual_connection_cls = virtual_connection_cls
    """
    virtual_connection command of zone_assignment.
    """
    print_battery_connection: print_battery_connection_cls = print_battery_connection_cls
    """
    print_battery_connection command of zone_assignment.
    """
