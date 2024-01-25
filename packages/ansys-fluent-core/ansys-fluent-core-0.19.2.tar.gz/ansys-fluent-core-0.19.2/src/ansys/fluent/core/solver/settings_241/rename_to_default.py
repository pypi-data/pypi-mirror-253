#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .zone_name_6 import zone_name as zone_name_cls
from .abbrev import abbrev as abbrev_cls
from .exclude import exclude as exclude_cls
class rename_to_default(Command):
    """
    Rename zone to default name.
    
    Parameters
    ----------
        zone_name : typing.List[str]
            Enter zone name list.
        abbrev : bool
            'abbrev' child.
        exclude : bool
            'exclude' child.
    
    """

    fluent_name = "rename-to-default"

    argument_names = \
        ['zone_name', 'abbrev', 'exclude']

    zone_name: zone_name_cls = zone_name_cls
    """
    zone_name argument of rename_to_default.
    """
    abbrev: abbrev_cls = abbrev_cls
    """
    abbrev argument of rename_to_default.
    """
    exclude: exclude_cls = exclude_cls
    """
    exclude argument of rename_to_default.
    """
