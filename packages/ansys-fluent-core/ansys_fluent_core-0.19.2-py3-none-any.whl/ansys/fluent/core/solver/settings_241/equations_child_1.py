#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .monitor import monitor as monitor_cls
from .normalization_factor import normalization_factor as normalization_factor_cls
from .check_convergence import check_convergence as check_convergence_cls
from .absolute_criteria import absolute_criteria as absolute_criteria_cls
from .relative_criteria import relative_criteria as relative_criteria_cls
class equations_child(Group):
    """
    'child_object_type' of equations.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['monitor', 'normalization_factor', 'check_convergence',
         'absolute_criteria', 'relative_criteria']

    monitor: monitor_cls = monitor_cls
    """
    monitor child of equations_child.
    """
    normalization_factor: normalization_factor_cls = normalization_factor_cls
    """
    normalization_factor child of equations_child.
    """
    check_convergence: check_convergence_cls = check_convergence_cls
    """
    check_convergence child of equations_child.
    """
    absolute_criteria: absolute_criteria_cls = absolute_criteria_cls
    """
    absolute_criteria child of equations_child.
    """
    relative_criteria: relative_criteria_cls = relative_criteria_cls
    """
    relative_criteria child of equations_child.
    """
