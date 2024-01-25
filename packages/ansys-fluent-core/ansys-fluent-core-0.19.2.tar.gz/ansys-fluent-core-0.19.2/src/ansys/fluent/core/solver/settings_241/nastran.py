#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .file_name_1 import file_name as file_name_cls
from .bndry_threads import bndry_threads as bndry_threads_cls
from .surfaces import surfaces as surfaces_cls
from .structural_analysis import structural_analysis as structural_analysis_cls
from .write_loads import write_loads as write_loads_cls
from .loads import loads as loads_cls
from .cell_func_domain_export import cell_func_domain_export as cell_func_domain_export_cls
class nastran(Command):
    """
    Write a NASTRAN file.
    
    Parameters
    ----------
        file_name : str
            'file_name' child.
        bndry_threads : typing.List[str]
            Enter boundary zone name list.
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

    fluent_name = "nastran"

    argument_names = \
        ['file_name', 'bndry_threads', 'surfaces', 'structural_analysis',
         'write_loads', 'loads', 'cell_func_domain_export']

    file_name: file_name_cls = file_name_cls
    """
    file_name argument of nastran.
    """
    bndry_threads: bndry_threads_cls = bndry_threads_cls
    """
    bndry_threads argument of nastran.
    """
    surfaces: surfaces_cls = surfaces_cls
    """
    surfaces argument of nastran.
    """
    structural_analysis: structural_analysis_cls = structural_analysis_cls
    """
    structural_analysis argument of nastran.
    """
    write_loads: write_loads_cls = write_loads_cls
    """
    write_loads argument of nastran.
    """
    loads: loads_cls = loads_cls
    """
    loads argument of nastran.
    """
    cell_func_domain_export: cell_func_domain_export_cls = cell_func_domain_export_cls
    """
    cell_func_domain_export argument of nastran.
    """
