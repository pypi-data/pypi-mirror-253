#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enabled_12 import enabled as enabled_cls
from .value_input import value_input as value_input_cls
class orthotropic_k(Group):
    """
    'orthotropic_k' child.
    """

    fluent_name = "orthotropic-k"

    child_names = \
        ['enabled', 'value_input']

    enabled: enabled_cls = enabled_cls
    """
    enabled child of orthotropic_k.
    """
    value_input: value_input_cls = value_input_cls
    """
    value_input child of orthotropic_k.
    """
