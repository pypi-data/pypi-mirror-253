#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .geom_disable import geom_disable as geom_disable_cls
from .geom_dir_spec import geom_dir_spec as geom_dir_spec_cls
from .geom_dir_x import geom_dir_x as geom_dir_x_cls
from .geom_dir_y import geom_dir_y as geom_dir_y_cls
from .geom_dir_z import geom_dir_z as geom_dir_z_cls
from .geom_levels import geom_levels as geom_levels_cls
from .geom_bgthread import geom_bgthread as geom_bgthread_cls
from .mass_flow_specification import mass_flow_specification as mass_flow_specification_cls
from .mass_flow_rate_1 import mass_flow_rate as mass_flow_rate_cls
from .mass_flux import mass_flux as mass_flux_cls
from .participates_in_solar_ray_tracing import participates_in_solar_ray_tracing as participates_in_solar_ray_tracing_cls
from .solar_transmissivity_factor import solar_transmissivity_factor as solar_transmissivity_factor_cls
class phase_child(Group):
    """
    'child_object_type' of phase.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['geom_disable', 'geom_dir_spec', 'geom_dir_x', 'geom_dir_y',
         'geom_dir_z', 'geom_levels', 'geom_bgthread',
         'mass_flow_specification', 'mass_flow_rate', 'mass_flux',
         'participates_in_solar_ray_tracing', 'solar_transmissivity_factor']

    geom_disable: geom_disable_cls = geom_disable_cls
    """
    geom_disable child of phase_child.
    """
    geom_dir_spec: geom_dir_spec_cls = geom_dir_spec_cls
    """
    geom_dir_spec child of phase_child.
    """
    geom_dir_x: geom_dir_x_cls = geom_dir_x_cls
    """
    geom_dir_x child of phase_child.
    """
    geom_dir_y: geom_dir_y_cls = geom_dir_y_cls
    """
    geom_dir_y child of phase_child.
    """
    geom_dir_z: geom_dir_z_cls = geom_dir_z_cls
    """
    geom_dir_z child of phase_child.
    """
    geom_levels: geom_levels_cls = geom_levels_cls
    """
    geom_levels child of phase_child.
    """
    geom_bgthread: geom_bgthread_cls = geom_bgthread_cls
    """
    geom_bgthread child of phase_child.
    """
    mass_flow_specification: mass_flow_specification_cls = mass_flow_specification_cls
    """
    mass_flow_specification child of phase_child.
    """
    mass_flow_rate: mass_flow_rate_cls = mass_flow_rate_cls
    """
    mass_flow_rate child of phase_child.
    """
    mass_flux: mass_flux_cls = mass_flux_cls
    """
    mass_flux child of phase_child.
    """
    participates_in_solar_ray_tracing: participates_in_solar_ray_tracing_cls = participates_in_solar_ray_tracing_cls
    """
    participates_in_solar_ray_tracing child of phase_child.
    """
    solar_transmissivity_factor: solar_transmissivity_factor_cls = solar_transmissivity_factor_cls
    """
    solar_transmissivity_factor child of phase_child.
    """
