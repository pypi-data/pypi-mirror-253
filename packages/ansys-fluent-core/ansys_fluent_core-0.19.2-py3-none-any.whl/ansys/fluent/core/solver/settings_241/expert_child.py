#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .species_1 import species_1 as species_1_cls
from .species_2 import species_2 as species_2_cls
from .coefficient_1 import coefficient_1 as coefficient_1_cls
from .coefficient_2 import coefficient_2 as coefficient_2_cls
class expert_child(Group):
    """
    'child_object_type' of expert.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['species_1', 'species_2', 'coefficient_1', 'coefficient_2']

    species_1: species_1_cls = species_1_cls
    """
    species_1 child of expert_child.
    """
    species_2: species_2_cls = species_2_cls
    """
    species_2 child of expert_child.
    """
    coefficient_1: coefficient_1_cls = coefficient_1_cls
    """
    coefficient_1 child of expert_child.
    """
    coefficient_2: coefficient_2_cls = coefficient_2_cls
    """
    coefficient_2 child of expert_child.
    """
