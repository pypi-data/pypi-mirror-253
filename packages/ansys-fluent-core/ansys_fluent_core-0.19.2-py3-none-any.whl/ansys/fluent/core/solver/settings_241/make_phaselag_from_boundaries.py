#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .side_1 import side_1 as side_1_cls
from .side_2 import side_2 as side_2_cls
from .angle import angle as angle_cls
from .interface_name_1 import interface_name as interface_name_cls
class make_phaselag_from_boundaries(Command):
    """
    Make interface zones phase lagged.
    
    Parameters
    ----------
        side_1 : str
            Enter id/name of zone to convert to phase lag side 1.
        side_2 : str
            Enter id/name of zone to convert to phase lag side 2.
        angle : real
            'angle' child.
        interface_name : str
            'interface_name' child.
    
    """

    fluent_name = "make-phaselag-from-boundaries"

    argument_names = \
        ['side_1', 'side_2', 'angle', 'interface_name']

    side_1: side_1_cls = side_1_cls
    """
    side_1 argument of make_phaselag_from_boundaries.
    """
    side_2: side_2_cls = side_2_cls
    """
    side_2 argument of make_phaselag_from_boundaries.
    """
    angle: angle_cls = angle_cls
    """
    angle argument of make_phaselag_from_boundaries.
    """
    interface_name: interface_name_cls = interface_name_cls
    """
    interface_name argument of make_phaselag_from_boundaries.
    """
