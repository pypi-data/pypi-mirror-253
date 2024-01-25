#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .surface_names_1 import surface_names as surface_names_cls
from .color_1 import color as color_cls
from .material import material as material_cls
class surfaces(Command):
    """
    Select the surface(s) to specify colors and/or materials.
    
    Parameters
    ----------
        surface_names : typing.List[str]
            Enter the list of surfaces to set color and material.
        color : str
            'color' child.
        material : str
            'material' child.
    
    """

    fluent_name = "surfaces"

    argument_names = \
        ['surface_names', 'color', 'material']

    surface_names: surface_names_cls = surface_names_cls
    """
    surface_names argument of surfaces.
    """
    color: color_cls = color_cls
    """
    color argument of surfaces.
    """
    material: material_cls = material_cls
    """
    material argument of surfaces.
    """
