#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enabled_12 import enabled as enabled_cls
from .h import h as h_cls
from .a import a as a_cls
from .e import e as e_cls
from .trigger_t import trigger_t as trigger_t_cls
from .e0 import e0 as e0_cls
class internal_short(Group):
    """
    'internal_short' child.
    """

    fluent_name = "internal-short"

    child_names = \
        ['enabled', 'h', 'a', 'e', 'trigger_t', 'e0']

    enabled: enabled_cls = enabled_cls
    """
    enabled child of internal_short.
    """
    h: h_cls = h_cls
    """
    h child of internal_short.
    """
    a: a_cls = a_cls
    """
    a child of internal_short.
    """
    e: e_cls = e_cls
    """
    e child of internal_short.
    """
    trigger_t: trigger_t_cls = trigger_t_cls
    """
    trigger_t child of internal_short.
    """
    e0: e0_cls = e0_cls
    """
    e0 child of internal_short.
    """
