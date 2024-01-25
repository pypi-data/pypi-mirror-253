#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .fixed import fixed as fixed_cls
from .fixes import fixes as fixes_cls
class fixed_values(Group):
    """
    Help not available.
    """

    fluent_name = "fixed-values"

    child_names = \
        ['fixed', 'fixes']

    fixed: fixed_cls = fixed_cls
    """
    fixed child of fixed_values.
    """
    fixes: fixes_cls = fixes_cls
    """
    fixes child of fixed_values.
    """
