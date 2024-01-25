#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .active import active as active_cls
from .x_center import x_center as x_center_cls
from .y_center import y_center as y_center_cls
from .z_center import z_center as z_center_cls
from .radius import radius as radius_cls
class settings_child(Group):
    """
    'child_object_type' of settings.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['active', 'x_center', 'y_center', 'z_center', 'radius']

    active: active_cls = active_cls
    """
    active child of settings_child.
    """
    x_center: x_center_cls = x_center_cls
    """
    x_center child of settings_child.
    """
    y_center: y_center_cls = y_center_cls
    """
    y_center child of settings_child.
    """
    z_center: z_center_cls = z_center_cls
    """
    z_center child of settings_child.
    """
    radius: radius_cls = radius_cls
    """
    radius child of settings_child.
    """
