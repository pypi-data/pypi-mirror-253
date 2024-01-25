#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .anode_fc_zone_list import anode_fc_zone_list as anode_fc_zone_list_cls
class anode_fc_zone(Group):
    """
    'anode_fc_zone' child.
    """

    fluent_name = "anode-fc-zone"

    child_names = \
        ['anode_fc_zone_list']

    anode_fc_zone_list: anode_fc_zone_list_cls = anode_fc_zone_list_cls
    """
    anode_fc_zone_list child of anode_fc_zone.
    """
