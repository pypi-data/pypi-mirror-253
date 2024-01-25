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
class modifications_child(Group):
    """
    'child_object_type' of modifications.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['active', 'name', 'python_cmd', 'command', 'count', 'ftselected',
         'flowtime']

    active: active_cls = active_cls
    """
    active child of modifications_child.
    """
    name: name_cls = name_cls
    """
    name child of modifications_child.
    """
    python_cmd: python_cmd_cls = python_cmd_cls
    """
    python_cmd child of modifications_child.
    """
    command: command_cls = command_cls
    """
    command child of modifications_child.
    """
    count: count_cls = count_cls
    """
    count child of modifications_child.
    """
    ftselected: ftselected_cls = ftselected_cls
    """
    ftselected child of modifications_child.
    """
    flowtime: flowtime_cls = flowtime_cls
    """
    flowtime child of modifications_child.
    """
