#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .point1 import point1 as point1_cls
from .point2_or_vector import point2_or_vector as point2_or_vector_cls
from .diameter_1 import diameter as diameter_cls
class injection_hole_child(Group):
    """
    'child_object_type' of injection_hole.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['point1', 'point2_or_vector', 'diameter']

    point1: point1_cls = point1_cls
    """
    point1 child of injection_hole_child.
    """
    point2_or_vector: point2_or_vector_cls = point2_or_vector_cls
    """
    point2_or_vector child of injection_hole_child.
    """
    diameter: diameter_cls = diameter_cls
    """
    diameter child of injection_hole_child.
    """
