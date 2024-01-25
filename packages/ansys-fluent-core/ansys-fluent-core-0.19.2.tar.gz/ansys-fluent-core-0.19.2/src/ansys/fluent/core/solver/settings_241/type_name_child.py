#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .color_1 import color as color_cls
from .material import material as material_cls
class type_name_child(Group):
    """
    'child_object_type' of type_name.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['color', 'material']

    color: color_cls = color_cls
    """
    color child of type_name_child.
    """
    material: material_cls = material_cls
    """
    material child of type_name_child.
    """
