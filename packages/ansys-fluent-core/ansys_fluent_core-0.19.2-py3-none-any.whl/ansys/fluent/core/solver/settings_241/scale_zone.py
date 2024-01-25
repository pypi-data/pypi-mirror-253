#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .zone_names_1 import zone_names as zone_names_cls
from .scale import scale as scale_cls
class scale_zone(Command):
    """
    Scale nodal coordinates of input cell zones.
    
    Parameters
    ----------
        zone_names : typing.List[str]
            Scale specified cell zones.
        scale : typing.List[real]
            'scale' child.
    
    """

    fluent_name = "scale-zone"

    argument_names = \
        ['zone_names', 'scale']

    zone_names: zone_names_cls = zone_names_cls
    """
    zone_names argument of scale_zone.
    """
    scale: scale_cls = scale_cls
    """
    scale argument of scale_zone.
    """
