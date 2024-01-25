#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .permeation_enabled import permeation_enabled as permeation_enabled_cls
from .permeation_n import permeation_n as permeation_n_cls
from .permeation_name import permeation_name as permeation_name_cls
from .permeation_rate import permeation_rate as permeation_rate_cls
from .permeation_ea import permeation_ea as permeation_ea_cls
class species_permeation(Group):
    """
    'species_permeation' child.
    """

    fluent_name = "species-permeation"

    child_names = \
        ['permeation_enabled', 'permeation_n', 'permeation_name',
         'permeation_rate', 'permeation_ea']

    permeation_enabled: permeation_enabled_cls = permeation_enabled_cls
    """
    permeation_enabled child of species_permeation.
    """
    permeation_n: permeation_n_cls = permeation_n_cls
    """
    permeation_n child of species_permeation.
    """
    permeation_name: permeation_name_cls = permeation_name_cls
    """
    permeation_name child of species_permeation.
    """
    permeation_rate: permeation_rate_cls = permeation_rate_cls
    """
    permeation_rate child of species_permeation.
    """
    permeation_ea: permeation_ea_cls = permeation_ea_cls
    """
    permeation_ea child of species_permeation.
    """
