#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .filename import filename as filename_cls
from .unit import unit as unit_cls
class read_surface_mesh(Command):
    """
    Read surface meshes.
    
    Parameters
    ----------
        filename : str
            Path to surface mesh file.
        unit : str
            Unit in which the mesh was created.
    
    """

    fluent_name = "read-surface-mesh"

    argument_names = \
        ['filename', 'unit']

    filename: filename_cls = filename_cls
    """
    filename argument of read_surface_mesh.
    """
    unit: unit_cls = unit_cls
    """
    unit argument of read_surface_mesh.
    """
