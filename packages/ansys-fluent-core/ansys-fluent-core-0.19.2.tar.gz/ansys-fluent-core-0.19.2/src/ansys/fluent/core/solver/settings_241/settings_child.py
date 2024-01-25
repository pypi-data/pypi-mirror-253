#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .active import active as active_cls
from .min_value import min_value as min_value_cls
from .max_value import max_value as max_value_cls
from .min_transparency_value import min_transparency_value as min_transparency_value_cls
from .max_transparency_value import max_transparency_value as max_transparency_value_cls
class settings_child(Group):
    """
    'child_object_type' of settings.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['active', 'min_value', 'max_value', 'min_transparency_value',
         'max_transparency_value']

    active: active_cls = active_cls
    """
    active child of settings_child.
    """
    min_value: min_value_cls = min_value_cls
    """
    min_value child of settings_child.
    """
    max_value: max_value_cls = max_value_cls
    """
    max_value child of settings_child.
    """
    min_transparency_value: min_transparency_value_cls = min_transparency_value_cls
    """
    min_transparency_value child of settings_child.
    """
    max_transparency_value: max_transparency_value_cls = max_transparency_value_cls
    """
    max_transparency_value child of settings_child.
    """
