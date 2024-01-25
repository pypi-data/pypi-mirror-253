#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .options_4 import options as options_cls
from .parameters import parameters as parameters_cls
from .anode import anode as anode_cls
from .electrolyte import electrolyte as electrolyte_cls
from .cathode import cathode as cathode_cls
from .electrical_tab import electrical_tab as electrical_tab_cls
from .advanced import advanced as advanced_cls
class electrolysis(Group):
    """
    'electrolysis' child.
    """

    fluent_name = "electrolysis"

    child_names = \
        ['options', 'parameters', 'anode', 'electrolyte', 'cathode',
         'electrical_tab', 'advanced']

    options: options_cls = options_cls
    """
    options child of electrolysis.
    """
    parameters: parameters_cls = parameters_cls
    """
    parameters child of electrolysis.
    """
    anode: anode_cls = anode_cls
    """
    anode child of electrolysis.
    """
    electrolyte: electrolyte_cls = electrolyte_cls
    """
    electrolyte child of electrolysis.
    """
    cathode: cathode_cls = cathode_cls
    """
    cathode child of electrolysis.
    """
    electrical_tab: electrical_tab_cls = electrical_tab_cls
    """
    electrical_tab child of electrolysis.
    """
    advanced: advanced_cls = advanced_cls
    """
    advanced child of electrolysis.
    """
