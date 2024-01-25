#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .active import active as active_cls
from .value_1 import value as value_cls
from .transparency import transparency as transparency_cls
from .color_2 import color as color_cls
class settings_child(Group):
    """
    'child_object_type' of settings.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['active', 'value', 'transparency', 'color']

    active: active_cls = active_cls
    """
    active child of settings_child.
    """
    value: value_cls = value_cls
    """
    value child of settings_child.
    """
    transparency: transparency_cls = transparency_cls
    """
    transparency child of settings_child.
    """
    color: color_cls = color_cls
    """
    color child of settings_child.
    """
