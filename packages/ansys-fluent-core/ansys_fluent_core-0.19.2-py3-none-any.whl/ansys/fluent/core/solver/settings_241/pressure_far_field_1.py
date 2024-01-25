#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .riemann_invariants_tangency_correction import riemann_invariants_tangency_correction as riemann_invariants_tangency_correction_cls
from .type_3 import type as type_cls
class pressure_far_field(Group):
    """
    Select presure-far-field boundary-condition options.
    """

    fluent_name = "pressure-far-field"

    child_names = \
        ['riemann_invariants_tangency_correction', 'type']

    riemann_invariants_tangency_correction: riemann_invariants_tangency_correction_cls = riemann_invariants_tangency_correction_cls
    """
    riemann_invariants_tangency_correction child of pressure_far_field.
    """
    type: type_cls = type_cls
    """
    type child of pressure_far_field.
    """
