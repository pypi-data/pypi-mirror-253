#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .body_force import body_force as body_force_cls
from .source_terms_1 import source_terms as source_terms_cls
from .erosion_accretion import erosion_accretion as erosion_accretion_cls
from .output import output as output_cls
from .scalar_update import scalar_update as scalar_update_cls
from .collision import collision as collision_cls
from .dpm_time_step_size_1 import dpm_time_step_size as dpm_time_step_size_cls
from .impingement_model import impingement_model as impingement_model_cls
from .film_regime import film_regime as film_regime_cls
from .splashing_distribution import splashing_distribution as splashing_distribution_cls
from .num_scalars import num_scalars as num_scalars_cls
from .flow_interpolation_1 import flow_interpolation as flow_interpolation_cls
from .max_num_udf_species import max_num_udf_species as max_num_udf_species_cls
class user_functions(Group):
    """
    Main menu to set DPM user-defined functions. User-defined functions can be used to customize the discrete phase model 
    to include additional body forces, modify interphase exchange terms (sources), calculate or integrate scalar values 
    along the particle trajectory, and more.
    """

    fluent_name = "user-functions"

    child_names = \
        ['body_force', 'source_terms', 'erosion_accretion', 'output',
         'scalar_update', 'collision', 'dpm_time_step_size',
         'impingement_model', 'film_regime', 'splashing_distribution',
         'num_scalars', 'flow_interpolation', 'max_num_udf_species']

    body_force: body_force_cls = body_force_cls
    """
    body_force child of user_functions.
    """
    source_terms: source_terms_cls = source_terms_cls
    """
    source_terms child of user_functions.
    """
    erosion_accretion: erosion_accretion_cls = erosion_accretion_cls
    """
    erosion_accretion child of user_functions.
    """
    output: output_cls = output_cls
    """
    output child of user_functions.
    """
    scalar_update: scalar_update_cls = scalar_update_cls
    """
    scalar_update child of user_functions.
    """
    collision: collision_cls = collision_cls
    """
    collision child of user_functions.
    """
    dpm_time_step_size: dpm_time_step_size_cls = dpm_time_step_size_cls
    """
    dpm_time_step_size child of user_functions.
    """
    impingement_model: impingement_model_cls = impingement_model_cls
    """
    impingement_model child of user_functions.
    """
    film_regime: film_regime_cls = film_regime_cls
    """
    film_regime child of user_functions.
    """
    splashing_distribution: splashing_distribution_cls = splashing_distribution_cls
    """
    splashing_distribution child of user_functions.
    """
    num_scalars: num_scalars_cls = num_scalars_cls
    """
    num_scalars child of user_functions.
    """
    flow_interpolation: flow_interpolation_cls = flow_interpolation_cls
    """
    flow_interpolation child of user_functions.
    """
    max_num_udf_species: max_num_udf_species_cls = max_num_udf_species_cls
    """
    max_num_udf_species child of user_functions.
    """
