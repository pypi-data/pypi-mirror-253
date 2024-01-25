#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .zone_name_6 import zone_name as zone_name_cls
from .abbreviate_types import abbreviate_types as abbreviate_types_cls
from .exclude import exclude as exclude_cls
class rename_by_adjacency(Command):
    """
    Rename zone to adjacent zones.
    
    Parameters
    ----------
        zone_name : typing.List[str]
            Enter zone name list.
        abbreviate_types : bool
            'abbreviate_types' child.
        exclude : bool
            'exclude' child.
    
    """

    fluent_name = "rename-by-adjacency"

    argument_names = \
        ['zone_name', 'abbreviate_types', 'exclude']

    zone_name: zone_name_cls = zone_name_cls
    """
    zone_name argument of rename_by_adjacency.
    """
    abbreviate_types: abbreviate_types_cls = abbreviate_types_cls
    """
    abbreviate_types argument of rename_by_adjacency.
    """
    exclude: exclude_cls = exclude_cls
    """
    exclude argument of rename_by_adjacency.
    """
