#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .file_name_1 import file_name as file_name_cls
from .surfaces import surfaces as surfaces_cls
from .structural_analysis import structural_analysis as structural_analysis_cls
from .write_loads import write_loads as write_loads_cls
from .loads import loads as loads_cls
from .cell_func_domain_export import cell_func_domain_export as cell_func_domain_export_cls
class patran_neutral(Command):
    """
    Write a PATRAN neutral file.
    
    Parameters
    ----------
        file_name : str
            'file_name' child.
        surfaces : typing.List[str]
            Select surface.
        structural_analysis : bool
            'structural_analysis' child.
        write_loads : bool
            'write_loads' child.
        loads : typing.List[str]
            'loads' child.
        cell_func_domain_export : typing.List[str]
            'cell_func_domain_export' child.
    
    """

    fluent_name = "patran-neutral"

    argument_names = \
        ['file_name', 'surfaces', 'structural_analysis', 'write_loads',
         'loads', 'cell_func_domain_export']

    file_name: file_name_cls = file_name_cls
    """
    file_name argument of patran_neutral.
    """
    surfaces: surfaces_cls = surfaces_cls
    """
    surfaces argument of patran_neutral.
    """
    structural_analysis: structural_analysis_cls = structural_analysis_cls
    """
    structural_analysis argument of patran_neutral.
    """
    write_loads: write_loads_cls = write_loads_cls
    """
    write_loads argument of patran_neutral.
    """
    loads: loads_cls = loads_cls
    """
    loads argument of patran_neutral.
    """
    cell_func_domain_export: cell_func_domain_export_cls = cell_func_domain_export_cls
    """
    cell_func_domain_export argument of patran_neutral.
    """
