#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .periodic_zone_name_1 import periodic_zone_name as periodic_zone_name_cls
class make_phaselag_from_periodic(Command):
    """
    Convert periodic interface to phase lagged.
    
    Parameters
    ----------
        periodic_zone_name : str
            Enter a periodic zone name.
    
    """

    fluent_name = "make-phaselag-from-periodic"

    argument_names = \
        ['periodic_zone_name']

    periodic_zone_name: periodic_zone_name_cls = periodic_zone_name_cls
    """
    periodic_zone_name argument of make_phaselag_from_periodic.
    """
