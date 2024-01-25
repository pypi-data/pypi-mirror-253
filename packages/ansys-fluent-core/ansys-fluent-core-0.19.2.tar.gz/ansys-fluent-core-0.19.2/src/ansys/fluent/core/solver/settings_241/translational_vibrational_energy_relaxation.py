#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .model import model as model_cls
from .expert import expert as expert_cls
class translational_vibrational_energy_relaxation(Group):
    """
    Define translational-vibrational energy relaxation model.
    """

    fluent_name = "translational-vibrational-energy-relaxation"

    child_names = \
        ['model', 'expert']

    model: model_cls = model_cls
    """
    model child of translational_vibrational_energy_relaxation.
    """
    expert: expert_cls = expert_cls
    """
    expert child of translational_vibrational_energy_relaxation.
    """
