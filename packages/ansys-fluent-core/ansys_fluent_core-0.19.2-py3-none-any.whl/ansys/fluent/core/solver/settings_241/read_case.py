#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .file_name_1 import file_name as file_name_cls
from .pdf_file_name import pdf_file_name as pdf_file_name_cls
class read_case(Command):
    """
    'read_case' command.
    
    Parameters
    ----------
        file_name : str
            'file_name' child.
        pdf_file_name : str
            'pdf_file_name' child.
    
    """

    fluent_name = "read-case"

    argument_names = \
        ['file_name', 'pdf_file_name']

    file_name: file_name_cls = file_name_cls
    """
    file_name argument of read_case.
    """
    pdf_file_name: pdf_file_name_cls = pdf_file_name_cls
    """
    pdf_file_name argument of read_case.
    """
