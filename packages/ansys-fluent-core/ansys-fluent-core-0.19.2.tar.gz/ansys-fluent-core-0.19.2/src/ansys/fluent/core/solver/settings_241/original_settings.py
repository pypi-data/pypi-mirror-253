#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .active import active as active_cls
from .name_1 import name as name_cls
from .python_cmd import python_cmd as python_cmd_cls
from .command import command as command_cls
from .count import count as count_cls
from .ftselected import ftselected as ftselected_cls
from .flowtime import flowtime as flowtime_cls
class original_settings(Group):
    """
    'original_settings' child.
    """

    fluent_name = "original-settings"

    child_names = \
        ['active', 'name', 'python_cmd', 'command', 'count', 'ftselected',
         'flowtime']

    active: active_cls = active_cls
    """
    active child of original_settings.
    """
    name: name_cls = name_cls
    """
    name child of original_settings.
    """
    python_cmd: python_cmd_cls = python_cmd_cls
    """
    python_cmd child of original_settings.
    """
    command: command_cls = command_cls
    """
    command child of original_settings.
    """
    count: count_cls = count_cls
    """
    count child of original_settings.
    """
    ftselected: ftselected_cls = ftselected_cls
    """
    ftselected child of original_settings.
    """
    flowtime: flowtime_cls = flowtime_cls
    """
    flowtime child of original_settings.
    """
