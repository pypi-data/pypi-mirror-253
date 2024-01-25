#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .option import option as option_cls
from .y0 import y0 as y0_cls
from .number_of_child_droplets import number_of_child_droplets as number_of_child_droplets_cls
from .b1 import b1 as b1_cls
from .b0 import b0 as b0_cls
from .cl import cl as cl_cls
from .ctau import ctau as ctau_cls
from .crt import crt as crt_cls
from .critical_weber_number import critical_weber_number as critical_weber_number_cls
from .core_b1 import core_b1 as core_b1_cls
from .xi import xi as xi_cls
from .target_number_in_parcel import target_number_in_parcel as target_number_in_parcel_cls
from .c0 import c0 as c0_cls
from .column_drag_coeff import column_drag_coeff as column_drag_coeff_cls
from .ligament_factor import ligament_factor as ligament_factor_cls
from .jet_diameter import jet_diameter as jet_diameter_cls
from .k1 import k1 as k1_cls
from .k2 import k2 as k2_cls
from .tb import tb as tb_cls
class droplet_breakup(Group):
    """
    'droplet_breakup' child.
    """

    fluent_name = "droplet-breakup"

    child_names = \
        ['option', 'y0', 'number_of_child_droplets', 'b1', 'b0', 'cl', 'ctau',
         'crt', 'critical_weber_number', 'core_b1', 'xi',
         'target_number_in_parcel', 'c0', 'column_drag_coeff',
         'ligament_factor', 'jet_diameter', 'k1', 'k2', 'tb']

    option: option_cls = option_cls
    """
    option child of droplet_breakup.
    """
    y0: y0_cls = y0_cls
    """
    y0 child of droplet_breakup.
    """
    number_of_child_droplets: number_of_child_droplets_cls = number_of_child_droplets_cls
    """
    number_of_child_droplets child of droplet_breakup.
    """
    b1: b1_cls = b1_cls
    """
    b1 child of droplet_breakup.
    """
    b0: b0_cls = b0_cls
    """
    b0 child of droplet_breakup.
    """
    cl: cl_cls = cl_cls
    """
    cl child of droplet_breakup.
    """
    ctau: ctau_cls = ctau_cls
    """
    ctau child of droplet_breakup.
    """
    crt: crt_cls = crt_cls
    """
    crt child of droplet_breakup.
    """
    critical_weber_number: critical_weber_number_cls = critical_weber_number_cls
    """
    critical_weber_number child of droplet_breakup.
    """
    core_b1: core_b1_cls = core_b1_cls
    """
    core_b1 child of droplet_breakup.
    """
    xi: xi_cls = xi_cls
    """
    xi child of droplet_breakup.
    """
    target_number_in_parcel: target_number_in_parcel_cls = target_number_in_parcel_cls
    """
    target_number_in_parcel child of droplet_breakup.
    """
    c0: c0_cls = c0_cls
    """
    c0 child of droplet_breakup.
    """
    column_drag_coeff: column_drag_coeff_cls = column_drag_coeff_cls
    """
    column_drag_coeff child of droplet_breakup.
    """
    ligament_factor: ligament_factor_cls = ligament_factor_cls
    """
    ligament_factor child of droplet_breakup.
    """
    jet_diameter: jet_diameter_cls = jet_diameter_cls
    """
    jet_diameter child of droplet_breakup.
    """
    k1: k1_cls = k1_cls
    """
    k1 child of droplet_breakup.
    """
    k2: k2_cls = k2_cls
    """
    k2 child of droplet_breakup.
    """
    tb: tb_cls = tb_cls
    """
    tb child of droplet_breakup.
    """
