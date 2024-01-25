#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .mass_flow_rate_2 import mass_flow_rate as mass_flow_rate_cls
from .flow_direction_1 import flow_direction as flow_direction_cls
from .temperature_3 import temperature as temperature_cls
from .mixture_fraction_2 import mixture_fraction as mixture_fraction_cls
from .progress_variable_2 import progress_variable as progress_variable_cls
from .species_10 import species as species_cls
class static_injection_child(Group):
    """
    'child_object_type' of static_injection.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['mass_flow_rate', 'flow_direction', 'temperature',
         'mixture_fraction', 'progress_variable', 'species']

    mass_flow_rate: mass_flow_rate_cls = mass_flow_rate_cls
    """
    mass_flow_rate child of static_injection_child.
    """
    flow_direction: flow_direction_cls = flow_direction_cls
    """
    flow_direction child of static_injection_child.
    """
    temperature: temperature_cls = temperature_cls
    """
    temperature child of static_injection_child.
    """
    mixture_fraction: mixture_fraction_cls = mixture_fraction_cls
    """
    mixture_fraction child of static_injection_child.
    """
    progress_variable: progress_variable_cls = progress_variable_cls
    """
    progress_variable child of static_injection_child.
    """
    species: species_cls = species_cls
    """
    species child of static_injection_child.
    """
