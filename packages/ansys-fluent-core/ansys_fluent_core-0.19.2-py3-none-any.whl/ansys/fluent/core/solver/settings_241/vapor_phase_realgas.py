#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

class vapor_phase_realgas(Integer, _HasAllowedValuesMixin):
    """
    Set zone real-gas state:
    
    	-1:use global setting
    
    	 0:liquid
    	 1:vapor.
    """

    fluent_name = "vapor-phase-realgas"

