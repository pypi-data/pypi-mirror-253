#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .file_name_1 import file_name as file_name_cls
from .surface_name_list_1 import surface_name_list as surface_name_list_cls
from .delimiter import delimiter as delimiter_cls
from .cell_func_domain import cell_func_domain as cell_func_domain_cls
from .location import location as location_cls
class ascii(Command):
    """
    Write an ASCII file.
    
    Parameters
    ----------
        file_name : str
            'file_name' child.
        surface_name_list : typing.List[str]
            List of surfaces to export.
        delimiter : str
            'delimiter' child.
        cell_func_domain : typing.List[str]
            'cell_func_domain' child.
        location : str
            'location' child.
    
    """

    fluent_name = "ascii"

    argument_names = \
        ['file_name', 'surface_name_list', 'delimiter', 'cell_func_domain',
         'location']

    file_name: file_name_cls = file_name_cls
    """
    file_name argument of ascii.
    """
    surface_name_list: surface_name_list_cls = surface_name_list_cls
    """
    surface_name_list argument of ascii.
    """
    delimiter: delimiter_cls = delimiter_cls
    """
    delimiter argument of ascii.
    """
    cell_func_domain: cell_func_domain_cls = cell_func_domain_cls
    """
    cell_func_domain argument of ascii.
    """
    location: location_cls = location_cls
    """
    location argument of ascii.
    """
