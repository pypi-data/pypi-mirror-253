#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .relaxation import relaxation as relaxation_cls
from .flux import flux as flux_cls
from .gradient import gradient as gradient_cls
class anisotropic_solid_heat_transfer(Group):
    """
    Enter anisotropic solid heat transfer menu.
    """

    fluent_name = "anisotropic-solid-heat-transfer"

    child_names = \
        ['relaxation', 'flux', 'gradient']

    relaxation: relaxation_cls = relaxation_cls
    """
    relaxation child of anisotropic_solid_heat_transfer.
    """
    flux: flux_cls = flux_cls
    """
    flux child of anisotropic_solid_heat_transfer.
    """
    gradient: gradient_cls = gradient_cls
    """
    gradient child of anisotropic_solid_heat_transfer.
    """
