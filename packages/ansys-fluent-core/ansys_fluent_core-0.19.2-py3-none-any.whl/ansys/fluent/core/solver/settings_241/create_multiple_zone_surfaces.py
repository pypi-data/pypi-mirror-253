#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .zone_names_4 import zone_names as zone_names_cls
class create_multiple_zone_surfaces(Command):
    """
    'create_multiple_zone_surfaces' command.
    
    Parameters
    ----------
        zone_names : typing.List[str]
            Enter zone name list.
    
    """

    fluent_name = "create-multiple-zone-surfaces"

    argument_names = \
        ['zone_names']

    zone_names: zone_names_cls = zone_names_cls
    """
    zone_names argument of create_multiple_zone_surfaces.
    """
