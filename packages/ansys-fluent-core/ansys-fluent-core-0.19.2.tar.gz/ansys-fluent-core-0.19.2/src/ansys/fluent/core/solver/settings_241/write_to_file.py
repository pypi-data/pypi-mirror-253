#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .filename_2 import filename as filename_cls
class write_to_file(Command):
    """
    Write data to file.
    
    Parameters
    ----------
        filename : str
            Enter file name.
    
    """

    fluent_name = "write-to-file"

    argument_names = \
        ['filename']

    filename: filename_cls = filename_cls
    """
    filename argument of write_to_file.
    """
