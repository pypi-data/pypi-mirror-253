#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

class under_relaxation(Real):
    """
    Set turbo-specific non-reflecting b.c. under-relaxation factor.
     specify < 0 => use P/a_ave
     specify = 0 => use 1/N    
     specify > 0 => use specified.
    """

    fluent_name = "under-relaxation"

