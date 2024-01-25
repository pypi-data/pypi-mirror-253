#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .cathode_cc_zone_list import cathode_cc_zone_list as cathode_cc_zone_list_cls
from .cathode_cc_update import cathode_cc_update as cathode_cc_update_cls
from .cathode_cc_material import cathode_cc_material as cathode_cc_material_cls
class cathode_cc_zone(Group):
    """
    'cathode_cc_zone' child.
    """

    fluent_name = "cathode-cc-zone"

    child_names = \
        ['cathode_cc_zone_list', 'cathode_cc_update', 'cathode_cc_material']

    cathode_cc_zone_list: cathode_cc_zone_list_cls = cathode_cc_zone_list_cls
    """
    cathode_cc_zone_list child of cathode_cc_zone.
    """
    cathode_cc_update: cathode_cc_update_cls = cathode_cc_update_cls
    """
    cathode_cc_update child of cathode_cc_zone.
    """
    cathode_cc_material: cathode_cc_material_cls = cathode_cc_material_cls
    """
    cathode_cc_material child of cathode_cc_zone.
    """
