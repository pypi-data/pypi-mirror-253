#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .cursys_1 import cursys as cursys_cls
from .cursys_name import cursys_name as cursys_name_cls
class material_orientation(Group):
    """
    Help not available.
    """

    fluent_name = "material-orientation"

    child_names = \
        ['cursys', 'cursys_name']

    cursys: cursys_cls = cursys_cls
    """
    cursys child of material_orientation.
    """
    cursys_name: cursys_name_cls = cursys_name_cls
    """
    cursys_name child of material_orientation.
    """
