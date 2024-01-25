#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .hide_volume import hide_volume as hide_volume_cls
from .settings_3 import settings as settings_cls
from .reset_1 import reset as reset_cls
class isovalue_options(Group):
    """
    'isovalue_options' child.
    """

    fluent_name = "isovalue-options"

    child_names = \
        ['hide_volume', 'settings']

    hide_volume: hide_volume_cls = hide_volume_cls
    """
    hide_volume child of isovalue_options.
    """
    settings: settings_cls = settings_cls
    """
    settings child of isovalue_options.
    """
    command_names = \
        ['reset']

    reset: reset_cls = reset_cls
    """
    reset command of isovalue_options.
    """
