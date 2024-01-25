#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .radiation_bc import radiation_bc as radiation_bc_cls
from .radial_direction import radial_direction as radial_direction_cls
from .theta_width_of_beam import theta_width_of_beam as theta_width_of_beam_cls
from .phi_width_of_beam import phi_width_of_beam as phi_width_of_beam_cls
from .direct_irradiation import direct_irradiation as direct_irradiation_cls
from .diffuse_irradiation import diffuse_irradiation as diffuse_irradiation_cls
from .parallel_collimated_beam import parallel_collimated_beam as parallel_collimated_beam_cls
from .use_beeam_direction_from_solar_load_model_settings import use_beeam_direction_from_solar_load_model_settings as use_beeam_direction_from_solar_load_model_settings_cls
from .use_irradiation_from_solar_soad_model_settings import use_irradiation_from_solar_soad_model_settings as use_irradiation_from_solar_soad_model_settings_cls
from .participates_in_solar_ray_tracing import participates_in_solar_ray_tracing as participates_in_solar_ray_tracing_cls
from .solar_transmissivity_factor import solar_transmissivity_factor as solar_transmissivity_factor_cls
from .radiating_s2s_surface import radiating_s2s_surface as radiating_s2s_surface_cls
from .external_black_body_temperature_method import external_black_body_temperature_method as external_black_body_temperature_method_cls
from .black_body_temperature import black_body_temperature as black_body_temperature_cls
from .internal_emissivity import internal_emissivity as internal_emissivity_cls
class radiation(Group):
    """
    Help not available.
    """

    fluent_name = "radiation"

    child_names = \
        ['radiation_bc', 'radial_direction', 'theta_width_of_beam',
         'phi_width_of_beam', 'direct_irradiation', 'diffuse_irradiation',
         'parallel_collimated_beam',
         'use_beeam_direction_from_solar_load_model_settings',
         'use_irradiation_from_solar_soad_model_settings',
         'participates_in_solar_ray_tracing', 'solar_transmissivity_factor',
         'radiating_s2s_surface', 'external_black_body_temperature_method',
         'black_body_temperature', 'internal_emissivity']

    radiation_bc: radiation_bc_cls = radiation_bc_cls
    """
    radiation_bc child of radiation.
    """
    radial_direction: radial_direction_cls = radial_direction_cls
    """
    radial_direction child of radiation.
    """
    theta_width_of_beam: theta_width_of_beam_cls = theta_width_of_beam_cls
    """
    theta_width_of_beam child of radiation.
    """
    phi_width_of_beam: phi_width_of_beam_cls = phi_width_of_beam_cls
    """
    phi_width_of_beam child of radiation.
    """
    direct_irradiation: direct_irradiation_cls = direct_irradiation_cls
    """
    direct_irradiation child of radiation.
    """
    diffuse_irradiation: diffuse_irradiation_cls = diffuse_irradiation_cls
    """
    diffuse_irradiation child of radiation.
    """
    parallel_collimated_beam: parallel_collimated_beam_cls = parallel_collimated_beam_cls
    """
    parallel_collimated_beam child of radiation.
    """
    use_beeam_direction_from_solar_load_model_settings: use_beeam_direction_from_solar_load_model_settings_cls = use_beeam_direction_from_solar_load_model_settings_cls
    """
    use_beeam_direction_from_solar_load_model_settings child of radiation.
    """
    use_irradiation_from_solar_soad_model_settings: use_irradiation_from_solar_soad_model_settings_cls = use_irradiation_from_solar_soad_model_settings_cls
    """
    use_irradiation_from_solar_soad_model_settings child of radiation.
    """
    participates_in_solar_ray_tracing: participates_in_solar_ray_tracing_cls = participates_in_solar_ray_tracing_cls
    """
    participates_in_solar_ray_tracing child of radiation.
    """
    solar_transmissivity_factor: solar_transmissivity_factor_cls = solar_transmissivity_factor_cls
    """
    solar_transmissivity_factor child of radiation.
    """
    radiating_s2s_surface: radiating_s2s_surface_cls = radiating_s2s_surface_cls
    """
    radiating_s2s_surface child of radiation.
    """
    external_black_body_temperature_method: external_black_body_temperature_method_cls = external_black_body_temperature_method_cls
    """
    external_black_body_temperature_method child of radiation.
    """
    black_body_temperature: black_body_temperature_cls = black_body_temperature_cls
    """
    black_body_temperature child of radiation.
    """
    internal_emissivity: internal_emissivity_cls = internal_emissivity_cls
    """
    internal_emissivity child of radiation.
    """
