#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

class blending_factor(Integer):
    """
    The pressure blend factor(f), blends between specified pressure and average pressure conditions.
    If f = 1 recovers specified pressure, f = 0 recovers fully averaged pressure.
    """

    fluent_name = "blending-factor"

