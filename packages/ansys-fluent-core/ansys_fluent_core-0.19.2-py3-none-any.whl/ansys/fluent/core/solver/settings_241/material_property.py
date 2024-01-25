#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .cathode_cmax import cathode_cmax as cathode_cmax_cls
from .anode_cmax import anode_cmax as anode_cmax_cls
from .cathode_c_init import cathode_c_init as cathode_c_init_cls
from .anode_c_init import anode_c_init as anode_c_init_cls
from .electrolyte_c_init import electrolyte_c_init as electrolyte_c_init_cls
from .tplus import tplus as tplus_cls
from .activity_term import activity_term as activity_term_cls
class material_property(Group):
    """
    'material_property' child.
    """

    fluent_name = "material-property"

    child_names = \
        ['cathode_cmax', 'anode_cmax', 'cathode_c_init', 'anode_c_init',
         'electrolyte_c_init', 'tplus', 'activity_term']

    cathode_cmax: cathode_cmax_cls = cathode_cmax_cls
    """
    cathode_cmax child of material_property.
    """
    anode_cmax: anode_cmax_cls = anode_cmax_cls
    """
    anode_cmax child of material_property.
    """
    cathode_c_init: cathode_c_init_cls = cathode_c_init_cls
    """
    cathode_c_init child of material_property.
    """
    anode_c_init: anode_c_init_cls = anode_c_init_cls
    """
    anode_c_init child of material_property.
    """
    electrolyte_c_init: electrolyte_c_init_cls = electrolyte_c_init_cls
    """
    electrolyte_c_init child of material_property.
    """
    tplus: tplus_cls = tplus_cls
    """
    tplus child of material_property.
    """
    activity_term: activity_term_cls = activity_term_cls
    """
    activity_term child of material_property.
    """
