#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .option import option as option_cls
from .file_name_1 import file_name as file_name_cls
from .surfaces import surfaces as surfaces_cls
from .cell_func_domain import cell_func_domain as cell_func_domain_cls
class fieldview_unstruct_surfaces(Command):
    """
    Write a Fieldview unstructured surface mesh, data.
    
    Parameters
    ----------
        option : str
            'option' child.
        file_name : str
            'file_name' child.
        surfaces : typing.List[str]
            Select surface.
        cell_func_domain : typing.List[str]
            'cell_func_domain' child.
    
    """

    fluent_name = "fieldview-unstruct-surfaces"

    argument_names = \
        ['option', 'file_name', 'surfaces', 'cell_func_domain']

    option: option_cls = option_cls
    """
    option argument of fieldview_unstruct_surfaces.
    """
    file_name: file_name_cls = file_name_cls
    """
    file_name argument of fieldview_unstruct_surfaces.
    """
    surfaces: surfaces_cls = surfaces_cls
    """
    surfaces argument of fieldview_unstruct_surfaces.
    """
    cell_func_domain: cell_func_domain_cls = cell_func_domain_cls
    """
    cell_func_domain argument of fieldview_unstruct_surfaces.
    """
