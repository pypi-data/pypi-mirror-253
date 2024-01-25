#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .zone_names_3 import zone_names as zone_names_cls
from .offset import offset as offset_cls
class translate_zone(Command):
    """
    Translate nodal coordinates of input cell zones.
    
    Parameters
    ----------
        zone_names : typing.List[str]
            Translate specified cell zones.
        offset : typing.List[real]
            'offset' child.
    
    """

    fluent_name = "translate-zone"

    argument_names = \
        ['zone_names', 'offset']

    zone_names: zone_names_cls = zone_names_cls
    """
    zone_names argument of translate_zone.
    """
    offset: offset_cls = offset_cls
    """
    offset argument of translate_zone.
    """
