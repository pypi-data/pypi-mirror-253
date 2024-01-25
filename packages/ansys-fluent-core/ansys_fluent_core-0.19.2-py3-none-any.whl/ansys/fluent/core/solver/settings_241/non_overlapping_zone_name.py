#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .zone_name_1 import zone_name as zone_name_cls
class non_overlapping_zone_name(Command):
    """
    Get non-overlapping zone name from the associated interface zone.
    
    Parameters
    ----------
        zone_name : str
            Enter a zone name.
    
    """

    fluent_name = "non-overlapping-zone-name"

    argument_names = \
        ['zone_name']

    zone_name: zone_name_cls = zone_name_cls
    """
    zone_name argument of non_overlapping_zone_name.
    """
