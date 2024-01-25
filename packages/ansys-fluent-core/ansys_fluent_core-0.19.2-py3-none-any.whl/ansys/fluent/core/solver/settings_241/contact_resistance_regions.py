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

class contact_resistance_regions(ListObject[contact_resis_child]):
    """
    Contact Resistance Regions.
    """

    fluent_name = "contact-resistance-regions"

    command_names = \
        ['list_properties', 'add_zone', 'list_zone', 'delete_zone']

    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of contact_resistance_regions.
    """
    add_zone: add_zone_cls = add_zone_cls
    """
    add_zone command of contact_resistance_regions.
    """
    list_zone: list_zone_cls = list_zone_cls
    """
    list_zone command of contact_resistance_regions.
    """
    delete_zone: delete_zone_cls = delete_zone_cls
    """
    delete_zone command of contact_resistance_regions.
    """
    child_object_type: contact_resis_child = contact_resis_child
    """
    child_object_type of contact_resistance_regions.
    """
