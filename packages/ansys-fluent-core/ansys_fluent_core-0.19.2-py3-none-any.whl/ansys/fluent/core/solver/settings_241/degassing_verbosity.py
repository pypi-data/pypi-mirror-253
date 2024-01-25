#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

class degassing_verbosity(Integer, _HasAllowedValuesMixin):
    """
    Set the verbosity level of the total mass flow rate at the degassing boundary. The acceptable values are:
      0 - off
      1 - report per time step.
    """

    fluent_name = "degassing-verbosity"

