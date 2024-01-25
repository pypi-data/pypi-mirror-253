#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .anode_tab import anode_tab as anode_tab_cls
from .cathode_tab import cathode_tab as cathode_tab_cls
class electrical_tab(Group):
    """
    'electrical_tab' child.
    """

    fluent_name = "electrical-tab"

    child_names = \
        ['anode_tab', 'cathode_tab']

    anode_tab: anode_tab_cls = anode_tab_cls
    """
    anode_tab child of electrical_tab.
    """
    cathode_tab: cathode_tab_cls = cathode_tab_cls
    """
    cathode_tab child of electrical_tab.
    """
