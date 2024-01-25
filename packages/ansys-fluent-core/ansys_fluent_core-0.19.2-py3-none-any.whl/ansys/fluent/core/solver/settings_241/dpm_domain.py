#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enabled_5 import enabled as enabled_cls
from .partitioning_method import partitioning_method as partitioning_method_cls
class dpm_domain(Group):
    """
    'dpm_domain' child.
    """

    fluent_name = "dpm-domain"

    child_names = \
        ['enabled', 'partitioning_method']

    enabled: enabled_cls = enabled_cls
    """
    enabled child of dpm_domain.
    """
    partitioning_method: partitioning_method_cls = partitioning_method_cls
    """
    partitioning_method child of dpm_domain.
    """
