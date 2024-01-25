#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .mixture_fraction_1 import mixture_fraction as mixture_fraction_cls
from .mode_2_probability_1 import mode_2_probability as mode_2_probability_cls
from .mode_3_probability_1 import mode_3_probability as mode_3_probability_cls
from .equ_required import equ_required as equ_required_cls
from .mean_mixture_fraction import mean_mixture_fraction as mean_mixture_fraction_cls
from .mixture_fraction_variance import mixture_fraction_variance as mixture_fraction_variance_cls
from .secondary_mean_mixture_fraction import secondary_mean_mixture_fraction as secondary_mean_mixture_fraction_cls
from .secondary_mixture_fraction_variance import secondary_mixture_fraction_variance as secondary_mixture_fraction_variance_cls
from .specify_species_in_mole_fractions import specify_species_in_mole_fractions as specify_species_in_mole_fractions_cls
from .mf import mf as mf_cls
from .progress_variable_1 import progress_variable as progress_variable_cls
from .progress_variable_variance_1 import progress_variable_variance as progress_variable_variance_cls
from .flame_area_density_1 import flame_area_density as flame_area_density_cls
from .inert_stream_1 import inert_stream as inert_stream_cls
from .pollutant_no_mass_fraction_1 import pollutant_no_mass_fraction as pollutant_no_mass_fraction_cls
from .fraction_1 import fraction as fraction_cls
from .pollutant_nh3_mass_fraction_1 import pollutant_nh3_mass_fraction as pollutant_nh3_mass_fraction_cls
from .pollutant_n2o_mass_fraction_1 import pollutant_n2o_mass_fraction as pollutant_n2o_mass_fraction_cls
from .pollut_urea_1 import pollut_urea as pollut_urea_cls
from .pollut_hnco_1 import pollut_hnco as pollut_hnco_cls
from .pollut_nco_1 import pollut_nco as pollut_nco_cls
from .pollut_so2_1 import pollut_so2 as pollut_so2_cls
from .pollut_h2s_1 import pollut_h2s as pollut_h2s_cls
from .pollut_so3_1 import pollut_so3 as pollut_so3_cls
from .pollut_sh_1 import pollut_sh as pollut_sh_cls
from .pollut_so_1 import pollut_so as pollut_so_cls
from .soot_mass_fraction_1 import soot_mass_fraction as soot_mass_fraction_cls
from .nuclei_1 import nuclei as nuclei_cls
from .tar_mass_fraction_1 import tar_mass_fraction as tar_mass_fraction_cls
from .pollut_hg_1 import pollut_hg as pollut_hg_cls
from .pollut_hgcl2_1 import pollut_hgcl2 as pollut_hgcl2_cls
from .pollut_hcl_1 import pollut_hcl as pollut_hcl_cls
from .pollut_hgo_1 import pollut_hgo as pollut_hgo_cls
from .pollut_cl_1 import pollut_cl as pollut_cl_cls
from .pollut_cl2_1 import pollut_cl2 as pollut_cl2_cls
from .pollut_hgcl_1 import pollut_hgcl as pollut_hgcl_cls
from .pollut_hocl_1 import pollut_hocl as pollut_hocl_cls
from .tss_scalar import tss_scalar as tss_scalar_cls
class species(Group):
    """
    Help not available.
    """

    fluent_name = "species"

    child_names = \
        ['mixture_fraction', 'mode_2_probability', 'mode_3_probability',
         'equ_required', 'mean_mixture_fraction', 'mixture_fraction_variance',
         'secondary_mean_mixture_fraction',
         'secondary_mixture_fraction_variance',
         'specify_species_in_mole_fractions', 'mf', 'progress_variable',
         'progress_variable_variance', 'flame_area_density', 'inert_stream',
         'pollutant_no_mass_fraction', 'fraction',
         'pollutant_nh3_mass_fraction', 'pollutant_n2o_mass_fraction',
         'pollut_urea', 'pollut_hnco', 'pollut_nco', 'pollut_so2',
         'pollut_h2s', 'pollut_so3', 'pollut_sh', 'pollut_so',
         'soot_mass_fraction', 'nuclei', 'tar_mass_fraction', 'pollut_hg',
         'pollut_hgcl2', 'pollut_hcl', 'pollut_hgo', 'pollut_cl',
         'pollut_cl2', 'pollut_hgcl', 'pollut_hocl', 'tss_scalar']

    mixture_fraction: mixture_fraction_cls = mixture_fraction_cls
    """
    mixture_fraction child of species.
    """
    mode_2_probability: mode_2_probability_cls = mode_2_probability_cls
    """
    mode_2_probability child of species.
    """
    mode_3_probability: mode_3_probability_cls = mode_3_probability_cls
    """
    mode_3_probability child of species.
    """
    equ_required: equ_required_cls = equ_required_cls
    """
    equ_required child of species.
    """
    mean_mixture_fraction: mean_mixture_fraction_cls = mean_mixture_fraction_cls
    """
    mean_mixture_fraction child of species.
    """
    mixture_fraction_variance: mixture_fraction_variance_cls = mixture_fraction_variance_cls
    """
    mixture_fraction_variance child of species.
    """
    secondary_mean_mixture_fraction: secondary_mean_mixture_fraction_cls = secondary_mean_mixture_fraction_cls
    """
    secondary_mean_mixture_fraction child of species.
    """
    secondary_mixture_fraction_variance: secondary_mixture_fraction_variance_cls = secondary_mixture_fraction_variance_cls
    """
    secondary_mixture_fraction_variance child of species.
    """
    specify_species_in_mole_fractions: specify_species_in_mole_fractions_cls = specify_species_in_mole_fractions_cls
    """
    specify_species_in_mole_fractions child of species.
    """
    mf: mf_cls = mf_cls
    """
    mf child of species.
    """
    progress_variable: progress_variable_cls = progress_variable_cls
    """
    progress_variable child of species.
    """
    progress_variable_variance: progress_variable_variance_cls = progress_variable_variance_cls
    """
    progress_variable_variance child of species.
    """
    flame_area_density: flame_area_density_cls = flame_area_density_cls
    """
    flame_area_density child of species.
    """
    inert_stream: inert_stream_cls = inert_stream_cls
    """
    inert_stream child of species.
    """
    pollutant_no_mass_fraction: pollutant_no_mass_fraction_cls = pollutant_no_mass_fraction_cls
    """
    pollutant_no_mass_fraction child of species.
    """
    fraction: fraction_cls = fraction_cls
    """
    fraction child of species.
    """
    pollutant_nh3_mass_fraction: pollutant_nh3_mass_fraction_cls = pollutant_nh3_mass_fraction_cls
    """
    pollutant_nh3_mass_fraction child of species.
    """
    pollutant_n2o_mass_fraction: pollutant_n2o_mass_fraction_cls = pollutant_n2o_mass_fraction_cls
    """
    pollutant_n2o_mass_fraction child of species.
    """
    pollut_urea: pollut_urea_cls = pollut_urea_cls
    """
    pollut_urea child of species.
    """
    pollut_hnco: pollut_hnco_cls = pollut_hnco_cls
    """
    pollut_hnco child of species.
    """
    pollut_nco: pollut_nco_cls = pollut_nco_cls
    """
    pollut_nco child of species.
    """
    pollut_so2: pollut_so2_cls = pollut_so2_cls
    """
    pollut_so2 child of species.
    """
    pollut_h2s: pollut_h2s_cls = pollut_h2s_cls
    """
    pollut_h2s child of species.
    """
    pollut_so3: pollut_so3_cls = pollut_so3_cls
    """
    pollut_so3 child of species.
    """
    pollut_sh: pollut_sh_cls = pollut_sh_cls
    """
    pollut_sh child of species.
    """
    pollut_so: pollut_so_cls = pollut_so_cls
    """
    pollut_so child of species.
    """
    soot_mass_fraction: soot_mass_fraction_cls = soot_mass_fraction_cls
    """
    soot_mass_fraction child of species.
    """
    nuclei: nuclei_cls = nuclei_cls
    """
    nuclei child of species.
    """
    tar_mass_fraction: tar_mass_fraction_cls = tar_mass_fraction_cls
    """
    tar_mass_fraction child of species.
    """
    pollut_hg: pollut_hg_cls = pollut_hg_cls
    """
    pollut_hg child of species.
    """
    pollut_hgcl2: pollut_hgcl2_cls = pollut_hgcl2_cls
    """
    pollut_hgcl2 child of species.
    """
    pollut_hcl: pollut_hcl_cls = pollut_hcl_cls
    """
    pollut_hcl child of species.
    """
    pollut_hgo: pollut_hgo_cls = pollut_hgo_cls
    """
    pollut_hgo child of species.
    """
    pollut_cl: pollut_cl_cls = pollut_cl_cls
    """
    pollut_cl child of species.
    """
    pollut_cl2: pollut_cl2_cls = pollut_cl2_cls
    """
    pollut_cl2 child of species.
    """
    pollut_hgcl: pollut_hgcl_cls = pollut_hgcl_cls
    """
    pollut_hgcl child of species.
    """
    pollut_hocl: pollut_hocl_cls = pollut_hocl_cls
    """
    pollut_hocl child of species.
    """
    tss_scalar: tss_scalar_cls = tss_scalar_cls
    """
    tss_scalar child of species.
    """
