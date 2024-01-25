#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .periodic_zone_name import periodic_zone_name as periodic_zone_name_cls
from .slit_periodic import slit_periodic as slit_periodic_cls
class slit_periodic(Command):
    """
    Slit a periodic zone into two symmetry zones.
    
    Parameters
    ----------
        periodic_zone_name : str
            Enter id/name of periodic zone to slit.
        slit_periodic : bool
            'slit_periodic' child.
    
    """

    fluent_name = "slit-periodic"

    argument_names = \
        ['periodic_zone_name', 'slit_periodic']

    periodic_zone_name: periodic_zone_name_cls = periodic_zone_name_cls
    """
    periodic_zone_name argument of slit_periodic.
    """
    slit_periodic: slit_periodic_cls = slit_periodic_cls
    """
    slit_periodic argument of slit_periodic.
    """
