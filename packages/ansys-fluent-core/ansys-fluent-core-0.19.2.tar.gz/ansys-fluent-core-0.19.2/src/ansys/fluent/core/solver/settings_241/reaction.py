#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .react import react as react_cls
from .reaction_mechs_1 import reaction_mechs as reaction_mechs_cls
from .surface_volume_ratio import surface_volume_ratio as surface_volume_ratio_cls
from .electrolyte_1 import electrolyte as electrolyte_cls
class reaction(Group):
    """
    Help not available.
    """

    fluent_name = "reaction"

    child_names = \
        ['react', 'reaction_mechs', 'surface_volume_ratio', 'electrolyte']

    react: react_cls = react_cls
    """
    react child of reaction.
    """
    reaction_mechs: reaction_mechs_cls = reaction_mechs_cls
    """
    reaction_mechs child of reaction.
    """
    surface_volume_ratio: surface_volume_ratio_cls = surface_volume_ratio_cls
    """
    surface_volume_ratio child of reaction.
    """
    electrolyte: electrolyte_cls = electrolyte_cls
    """
    electrolyte child of reaction.
    """
