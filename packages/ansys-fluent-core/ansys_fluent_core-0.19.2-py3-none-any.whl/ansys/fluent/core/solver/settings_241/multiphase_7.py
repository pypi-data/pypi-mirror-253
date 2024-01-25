#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .gtemp_bc import gtemp_bc as gtemp_bc_cls
from .g_temperature import g_temperature as g_temperature_cls
from .g_qflux import g_qflux as g_qflux_cls
from .wall_restitution_coeff import wall_restitution_coeff as wall_restitution_coeff_cls
from .contact_angles import contact_angles as contact_angles_cls
class multiphase(Group):
    """
    Help not available.
    """

    fluent_name = "multiphase"

    child_names = \
        ['gtemp_bc', 'g_temperature', 'g_qflux', 'wall_restitution_coeff',
         'contact_angles']

    gtemp_bc: gtemp_bc_cls = gtemp_bc_cls
    """
    gtemp_bc child of multiphase.
    """
    g_temperature: g_temperature_cls = g_temperature_cls
    """
    g_temperature child of multiphase.
    """
    g_qflux: g_qflux_cls = g_qflux_cls
    """
    g_qflux child of multiphase.
    """
    wall_restitution_coeff: wall_restitution_coeff_cls = wall_restitution_coeff_cls
    """
    wall_restitution_coeff child of multiphase.
    """
    contact_angles: contact_angles_cls = contact_angles_cls
    """
    contact_angles child of multiphase.
    """
