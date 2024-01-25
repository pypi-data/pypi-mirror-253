#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .active import active as active_cls
from .x_min import x_min as x_min_cls
from .y_min import y_min as y_min_cls
from .z_min import z_min as z_min_cls
from .x_max import x_max as x_max_cls
from .y_max import y_max as y_max_cls
from .z_max import z_max as z_max_cls
class settings_child(Group):
    """
    'child_object_type' of settings.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['active', 'x_min', 'y_min', 'z_min', 'x_max', 'y_max', 'z_max']

    active: active_cls = active_cls
    """
    active child of settings_child.
    """
    x_min: x_min_cls = x_min_cls
    """
    x_min child of settings_child.
    """
    y_min: y_min_cls = y_min_cls
    """
    y_min child of settings_child.
    """
    z_min: z_min_cls = z_min_cls
    """
    z_min child of settings_child.
    """
    x_max: x_max_cls = x_max_cls
    """
    x_max child of settings_child.
    """
    y_max: y_max_cls = y_max_cls
    """
    y_max child of settings_child.
    """
    z_max: z_max_cls = z_max_cls
    """
    z_max child of settings_child.
    """
