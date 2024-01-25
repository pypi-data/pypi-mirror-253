#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enabled_2 import enabled as enabled_cls
from .drag_law import drag_law as drag_law_cls
from .lift_law import lift_law as lift_law_cls
class particle_rotation(Group):
    """
    'particle_rotation' child.
    """

    fluent_name = "particle-rotation"

    child_names = \
        ['enabled', 'drag_law', 'lift_law']

    enabled: enabled_cls = enabled_cls
    """
    enabled child of particle_rotation.
    """
    drag_law: drag_law_cls = drag_law_cls
    """
    drag_law child of particle_rotation.
    """
    lift_law: lift_law_cls = lift_law_cls
    """
    lift_law child of particle_rotation.
    """
