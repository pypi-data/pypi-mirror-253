#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .kw_vorticity_based_production import kw_vorticity_based_production as kw_vorticity_based_production_cls
from .kw_add_sas import kw_add_sas as kw_add_sas_cls
from .kw_add_des import kw_add_des as kw_add_des_cls
from .turbulence_damping import turbulence_damping as turbulence_damping_cls
from .rke_cmu_rotation_term import rke_cmu_rotation_term as rke_cmu_rotation_term_cls
from .turb_non_newtonian import turb_non_newtonian as turb_non_newtonian_cls
from .non_newtonian_modification import non_newtonian_modification as non_newtonian_modification_cls
from .turb_pk_compressible import turb_pk_compressible as turb_pk_compressible_cls
from .thermal_p_function import thermal_p_function as thermal_p_function_cls
from .restore_sst_v61 import restore_sst_v61 as restore_sst_v61_cls
class turbulence_expert(Group):
    """
    'turbulence_expert' child.
    """

    fluent_name = "turbulence-expert"

    child_names = \
        ['kw_vorticity_based_production', 'kw_add_sas', 'kw_add_des',
         'turbulence_damping', 'rke_cmu_rotation_term', 'turb_non_newtonian',
         'non_newtonian_modification', 'turb_pk_compressible',
         'thermal_p_function', 'restore_sst_v61']

    kw_vorticity_based_production: kw_vorticity_based_production_cls = kw_vorticity_based_production_cls
    """
    kw_vorticity_based_production child of turbulence_expert.
    """
    kw_add_sas: kw_add_sas_cls = kw_add_sas_cls
    """
    kw_add_sas child of turbulence_expert.
    """
    kw_add_des: kw_add_des_cls = kw_add_des_cls
    """
    kw_add_des child of turbulence_expert.
    """
    turbulence_damping: turbulence_damping_cls = turbulence_damping_cls
    """
    turbulence_damping child of turbulence_expert.
    """
    rke_cmu_rotation_term: rke_cmu_rotation_term_cls = rke_cmu_rotation_term_cls
    """
    rke_cmu_rotation_term child of turbulence_expert.
    """
    turb_non_newtonian: turb_non_newtonian_cls = turb_non_newtonian_cls
    """
    turb_non_newtonian child of turbulence_expert.
    """
    non_newtonian_modification: non_newtonian_modification_cls = non_newtonian_modification_cls
    """
    non_newtonian_modification child of turbulence_expert.
    """
    turb_pk_compressible: turb_pk_compressible_cls = turb_pk_compressible_cls
    """
    turb_pk_compressible child of turbulence_expert.
    """
    thermal_p_function: thermal_p_function_cls = thermal_p_function_cls
    """
    thermal_p_function child of turbulence_expert.
    """
    restore_sst_v61: restore_sst_v61_cls = restore_sst_v61_cls
    """
    restore_sst_v61 child of turbulence_expert.
    """
