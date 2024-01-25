#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .upstream_torque_integral import upstream_torque_integral as upstream_torque_integral_cls
from .upstream_total_enthalpy_integral import upstream_total_enthalpy_integral as upstream_total_enthalpy_integral_cls
from .discrete_phase_bc_type import discrete_phase_bc_type as discrete_phase_bc_type_cls
from .dem_collision_partner import dem_collision_partner as dem_collision_partner_cls
from .reinj_inj import reinj_inj as reinj_inj_cls
from .discrete_phase_bc_function import discrete_phase_bc_function as discrete_phase_bc_function_cls
from .mixing_plane_thread import mixing_plane_thread as mixing_plane_thread_cls
class dpm(Group):
    """
    Help not available.
    """

    fluent_name = "dpm"

    child_names = \
        ['upstream_torque_integral', 'upstream_total_enthalpy_integral',
         'discrete_phase_bc_type', 'dem_collision_partner', 'reinj_inj',
         'discrete_phase_bc_function', 'mixing_plane_thread']

    upstream_torque_integral: upstream_torque_integral_cls = upstream_torque_integral_cls
    """
    upstream_torque_integral child of dpm.
    """
    upstream_total_enthalpy_integral: upstream_total_enthalpy_integral_cls = upstream_total_enthalpy_integral_cls
    """
    upstream_total_enthalpy_integral child of dpm.
    """
    discrete_phase_bc_type: discrete_phase_bc_type_cls = discrete_phase_bc_type_cls
    """
    discrete_phase_bc_type child of dpm.
    """
    dem_collision_partner: dem_collision_partner_cls = dem_collision_partner_cls
    """
    dem_collision_partner child of dpm.
    """
    reinj_inj: reinj_inj_cls = reinj_inj_cls
    """
    reinj_inj child of dpm.
    """
    discrete_phase_bc_function: discrete_phase_bc_function_cls = discrete_phase_bc_function_cls
    """
    discrete_phase_bc_function child of dpm.
    """
    mixing_plane_thread: mixing_plane_thread_cls = mixing_plane_thread_cls
    """
    mixing_plane_thread child of dpm.
    """
