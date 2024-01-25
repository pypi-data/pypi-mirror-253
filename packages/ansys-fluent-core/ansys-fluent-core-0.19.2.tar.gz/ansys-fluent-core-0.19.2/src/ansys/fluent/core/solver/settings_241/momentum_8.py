#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .velocity_specification_method import velocity_specification_method as velocity_specification_method_cls
from .reference_frame_2 import reference_frame as reference_frame_cls
from .velocity_1 import velocity as velocity_cls
from .initial_gauge_pressure import initial_gauge_pressure as initial_gauge_pressure_cls
from .coordinate_system import coordinate_system as coordinate_system_cls
from .velocity_components import velocity_components as velocity_components_cls
from .flow_direction import flow_direction as flow_direction_cls
from .axis_direction_2 import axis_direction as axis_direction_cls
from .axis_origin_2 import axis_origin as axis_origin_cls
from .swirl_angular_velocity import swirl_angular_velocity as swirl_angular_velocity_cls
from .gauge_pressure_1 import gauge_pressure as gauge_pressure_cls
from .ac_options import ac_options as ac_options_cls
from .impedance_0 import impedance_0 as impedance_0_cls
from .impedance_1 import impedance_1 as impedance_1_cls
from .impedance_2 import impedance_2 as impedance_2_cls
from .ac_wave import ac_wave as ac_wave_cls
class momentum(Group):
    """
    Help not available.
    """

    fluent_name = "momentum"

    child_names = \
        ['velocity_specification_method', 'reference_frame', 'velocity',
         'initial_gauge_pressure', 'coordinate_system', 'velocity_components',
         'flow_direction', 'axis_direction', 'axis_origin',
         'swirl_angular_velocity', 'gauge_pressure', 'ac_options',
         'impedance_0', 'impedance_1', 'impedance_2', 'ac_wave']

    velocity_specification_method: velocity_specification_method_cls = velocity_specification_method_cls
    """
    velocity_specification_method child of momentum.
    """
    reference_frame: reference_frame_cls = reference_frame_cls
    """
    reference_frame child of momentum.
    """
    velocity: velocity_cls = velocity_cls
    """
    velocity child of momentum.
    """
    initial_gauge_pressure: initial_gauge_pressure_cls = initial_gauge_pressure_cls
    """
    initial_gauge_pressure child of momentum.
    """
    coordinate_system: coordinate_system_cls = coordinate_system_cls
    """
    coordinate_system child of momentum.
    """
    velocity_components: velocity_components_cls = velocity_components_cls
    """
    velocity_components child of momentum.
    """
    flow_direction: flow_direction_cls = flow_direction_cls
    """
    flow_direction child of momentum.
    """
    axis_direction: axis_direction_cls = axis_direction_cls
    """
    axis_direction child of momentum.
    """
    axis_origin: axis_origin_cls = axis_origin_cls
    """
    axis_origin child of momentum.
    """
    swirl_angular_velocity: swirl_angular_velocity_cls = swirl_angular_velocity_cls
    """
    swirl_angular_velocity child of momentum.
    """
    gauge_pressure: gauge_pressure_cls = gauge_pressure_cls
    """
    gauge_pressure child of momentum.
    """
    ac_options: ac_options_cls = ac_options_cls
    """
    ac_options child of momentum.
    """
    impedance_0: impedance_0_cls = impedance_0_cls
    """
    impedance_0 child of momentum.
    """
    impedance_1: impedance_1_cls = impedance_1_cls
    """
    impedance_1 child of momentum.
    """
    impedance_2: impedance_2_cls = impedance_2_cls
    """
    impedance_2 child of momentum.
    """
    ac_wave: ac_wave_cls = ac_wave_cls
    """
    ac_wave child of momentum.
    """
