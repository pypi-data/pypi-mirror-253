#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .file_name_1 import file_name as file_name_cls
from .surfaces_1 import surfaces as surfaces_cls
from .cellzones import cellzones as cellzones_cls
from .cell_func_domain import cell_func_domain as cell_func_domain_cls
class fieldview_unstruct_mesh(Command):
    """
    Write a Fieldview unstructured mesh only file.
    
    Parameters
    ----------
        file_name : str
            'file_name' child.
        surfaces : typing.List[str]
            List of surfaces to export.
        cellzones : typing.List[str]
            List of cell zones to export.
        cell_func_domain : typing.List[str]
            'cell_func_domain' child.
    
    """

    fluent_name = "fieldview-unstruct-mesh"

    argument_names = \
        ['file_name', 'surfaces', 'cellzones', 'cell_func_domain']

    file_name: file_name_cls = file_name_cls
    """
    file_name argument of fieldview_unstruct_mesh.
    """
    surfaces: surfaces_cls = surfaces_cls
    """
    surfaces argument of fieldview_unstruct_mesh.
    """
    cellzones: cellzones_cls = cellzones_cls
    """
    cellzones argument of fieldview_unstruct_mesh.
    """
    cell_func_domain: cell_func_domain_cls = cell_func_domain_cls
    """
    cell_func_domain argument of fieldview_unstruct_mesh.
    """
