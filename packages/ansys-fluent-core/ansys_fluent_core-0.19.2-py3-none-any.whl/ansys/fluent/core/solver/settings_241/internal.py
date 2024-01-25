#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .pcb_zone_info import pcb_zone_info as pcb_zone_info_cls
from .pcb_model import pcb_model as pcb_model_cls
from .vapor_phase_realgas import vapor_phase_realgas as vapor_phase_realgas_cls
from .active_wetsteam_zone import active_wetsteam_zone as active_wetsteam_zone_cls
from .contact_property import contact_property as contact_property_cls
class internal(Group):
    """
    Help not available.
    """

    fluent_name = "internal"

    child_names = \
        ['pcb_zone_info', 'pcb_model', 'vapor_phase_realgas',
         'active_wetsteam_zone', 'contact_property']

    pcb_zone_info: pcb_zone_info_cls = pcb_zone_info_cls
    """
    pcb_zone_info child of internal.
    """
    pcb_model: pcb_model_cls = pcb_model_cls
    """
    pcb_model child of internal.
    """
    vapor_phase_realgas: vapor_phase_realgas_cls = vapor_phase_realgas_cls
    """
    vapor_phase_realgas child of internal.
    """
    active_wetsteam_zone: active_wetsteam_zone_cls = active_wetsteam_zone_cls
    """
    active_wetsteam_zone child of internal.
    """
    contact_property: contact_property_cls = contact_property_cls
    """
    contact_property child of internal.
    """
