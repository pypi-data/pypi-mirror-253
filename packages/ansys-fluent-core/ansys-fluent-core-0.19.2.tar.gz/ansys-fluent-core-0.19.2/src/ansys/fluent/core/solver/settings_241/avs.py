#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .file_name_1 import file_name as file_name_cls
from .cell_func_domain_export import cell_func_domain_export as cell_func_domain_export_cls
class avs(Command):
    """
    Write an AVS UCD file.
    
    Parameters
    ----------
        file_name : str
            'file_name' child.
        cell_func_domain_export : typing.List[str]
            'cell_func_domain_export' child.
    
    """

    fluent_name = "avs"

    argument_names = \
        ['file_name', 'cell_func_domain_export']

    file_name: file_name_cls = file_name_cls
    """
    file_name argument of avs.
    """
    cell_func_domain_export: cell_func_domain_export_cls = cell_func_domain_export_cls
    """
    cell_func_domain_export argument of avs.
    """
