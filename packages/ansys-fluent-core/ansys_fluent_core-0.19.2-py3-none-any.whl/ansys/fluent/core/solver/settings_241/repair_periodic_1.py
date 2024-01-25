#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .repair_angle import repair_angle as repair_angle_cls
from .periodic_input import periodic_input as periodic_input_cls
from .angle_input import angle_input as angle_input_cls
from .repair_periodic import repair_periodic as repair_periodic_cls
class repair_periodic(Command):
    """
    Modify mesh to enforce specified periodic rotation angle.
    
    Parameters
    ----------
        repair_angle : bool
            'repair_angle' child.
        periodic_input : str
            Enter id/name of zone to repair.
        angle_input : real
            Enter desired angle of rotation in degrees.
        repair_periodic : bool
            'repair_periodic' child.
    
    """

    fluent_name = "repair-periodic"

    argument_names = \
        ['repair_angle', 'periodic_input', 'angle_input', 'repair_periodic']

    repair_angle: repair_angle_cls = repair_angle_cls
    """
    repair_angle argument of repair_periodic.
    """
    periodic_input: periodic_input_cls = periodic_input_cls
    """
    periodic_input argument of repair_periodic.
    """
    angle_input: angle_input_cls = angle_input_cls
    """
    angle_input argument of repair_periodic.
    """
    repair_periodic: repair_periodic_cls = repair_periodic_cls
    """
    repair_periodic argument of repair_periodic.
    """
