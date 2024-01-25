#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .report_name import report_name as report_name_cls
from .file_name_1 import file_name as file_name_cls
class export_simulation_report_as_pdf(Command):
    """
    Export the provided simulation report as a PDF file.
    
    Parameters
    ----------
        report_name : str
            'report_name' child.
        file_name : str
            'file_name' child.
    
    """

    fluent_name = "export-simulation-report-as-pdf"

    argument_names = \
        ['report_name', 'file_name']

    report_name: report_name_cls = report_name_cls
    """
    report_name argument of export_simulation_report_as_pdf.
    """
    file_name: file_name_cls = file_name_cls
    """
    file_name argument of export_simulation_report_as_pdf.
    """
