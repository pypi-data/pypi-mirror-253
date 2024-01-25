#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .output_quantity import output_quantity as output_quantity_cls
from .rotor_name import rotor_name as rotor_name_cls
from .scale_output import scale_output as scale_output_cls
from .write_to_file_1 import write_to_file as write_to_file_cls
from .file_name_1 import file_name as file_name_cls
from .append import append as append_cls
class vbm(Command):
    """
    'vbm' command.
    
    Parameters
    ----------
        output_quantity : str
            'output_quantity' child.
        rotor_name : str
            'rotor_name' child.
        scale_output : bool
            'scale_output' child.
        write_to_file : bool
            'write_to_file' child.
        file_name : str
            'file_name' child.
        append : bool
            'append' child.
    
    """

    fluent_name = "vbm"

    argument_names = \
        ['output_quantity', 'rotor_name', 'scale_output', 'write_to_file',
         'file_name', 'append']

    output_quantity: output_quantity_cls = output_quantity_cls
    """
    output_quantity argument of vbm.
    """
    rotor_name: rotor_name_cls = rotor_name_cls
    """
    rotor_name argument of vbm.
    """
    scale_output: scale_output_cls = scale_output_cls
    """
    scale_output argument of vbm.
    """
    write_to_file: write_to_file_cls = write_to_file_cls
    """
    write_to_file argument of vbm.
    """
    file_name: file_name_cls = file_name_cls
    """
    file_name argument of vbm.
    """
    append: append_cls = append_cls
    """
    append argument of vbm.
    """
