#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .selection_type import selection_type as selection_type_cls
from .settings_4 import settings as settings_cls
from .reset_1 import reset as reset_cls
class clip_box_options(Group):
    """
    'clip_box_options' child.
    """

    fluent_name = "clip-box-options"

    child_names = \
        ['selection_type', 'settings']

    selection_type: selection_type_cls = selection_type_cls
    """
    selection_type child of clip_box_options.
    """
    settings: settings_cls = settings_cls
    """
    settings child of clip_box_options.
    """
    command_names = \
        ['reset']

    reset: reset_cls = reset_cls
    """
    reset command of clip_box_options.
    """
