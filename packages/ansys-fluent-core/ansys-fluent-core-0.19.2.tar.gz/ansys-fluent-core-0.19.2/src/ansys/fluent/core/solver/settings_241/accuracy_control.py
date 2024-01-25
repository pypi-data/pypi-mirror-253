#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enabled_4 import enabled as enabled_cls
from .tolerance import tolerance as tolerance_cls
from .max_num_refinements import max_num_refinements as max_num_refinements_cls
from .step_size_fraction import step_size_fraction as step_size_fraction_cls
class accuracy_control(Group):
    """
    'accuracy_control' child.
    """

    fluent_name = "accuracy-control"

    child_names = \
        ['enabled', 'tolerance', 'max_num_refinements', 'step_size_fraction']

    enabled: enabled_cls = enabled_cls
    """
    enabled child of accuracy_control.
    """
    tolerance: tolerance_cls = tolerance_cls
    """
    tolerance child of accuracy_control.
    """
    max_num_refinements: max_num_refinements_cls = max_num_refinements_cls
    """
    max_num_refinements child of accuracy_control.
    """
    step_size_fraction: step_size_fraction_cls = step_size_fraction_cls
    """
    step_size_fraction child of accuracy_control.
    """
