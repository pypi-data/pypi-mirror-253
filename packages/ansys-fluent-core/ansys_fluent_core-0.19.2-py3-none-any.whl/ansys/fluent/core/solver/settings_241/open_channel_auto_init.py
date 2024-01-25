#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .boundary_zone import boundary_zone as boundary_zone_cls
from .flat_init import flat_init as flat_init_cls
from .wavy_surface_init import wavy_surface_init as wavy_surface_init_cls
class open_channel_auto_init(Group):
    """
    Open channel automatic initialization.
    """

    fluent_name = "open-channel-auto-init"

    child_names = \
        ['boundary_zone', 'flat_init', 'wavy_surface_init']

    boundary_zone: boundary_zone_cls = boundary_zone_cls
    """
    boundary_zone child of open_channel_auto_init.
    """
    flat_init: flat_init_cls = flat_init_cls
    """
    flat_init child of open_channel_auto_init.
    """
    wavy_surface_init: wavy_surface_init_cls = wavy_surface_init_cls
    """
    wavy_surface_init child of open_channel_auto_init.
    """
