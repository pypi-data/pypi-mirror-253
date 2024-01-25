#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .file_name_1 import file_name as file_name_cls
from .binary_format import binary_format as binary_format_cls
from .surfaces import surfaces as surfaces_cls
from .cell_centered import cell_centered as cell_centered_cls
from .cell_function import cell_function as cell_function_cls
class ensight_gold_parallel_surfaces(Command):
    """
    Write EnSight Gold geometry, velocity and scalar files for surfaces. Fluent will write files suitable for EnSight Parallel.
    
    Parameters
    ----------
        file_name : str
            'file_name' child.
        binary_format : bool
            'binary_format' child.
        surfaces : typing.List[str]
            Select surface.
        cell_centered : bool
            'cell_centered' child.
        cell_function : typing.List[str]
            'cell_function' child.
    
    """

    fluent_name = "ensight-gold-parallel-surfaces"

    argument_names = \
        ['file_name', 'binary_format', 'surfaces', 'cell_centered',
         'cell_function']

    file_name: file_name_cls = file_name_cls
    """
    file_name argument of ensight_gold_parallel_surfaces.
    """
    binary_format: binary_format_cls = binary_format_cls
    """
    binary_format argument of ensight_gold_parallel_surfaces.
    """
    surfaces: surfaces_cls = surfaces_cls
    """
    surfaces argument of ensight_gold_parallel_surfaces.
    """
    cell_centered: cell_centered_cls = cell_centered_cls
    """
    cell_centered argument of ensight_gold_parallel_surfaces.
    """
    cell_function: cell_function_cls = cell_function_cls
    """
    cell_function argument of ensight_gold_parallel_surfaces.
    """
