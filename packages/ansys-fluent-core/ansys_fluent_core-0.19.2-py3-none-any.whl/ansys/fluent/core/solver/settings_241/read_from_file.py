#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .filename_2 import filename as filename_cls
class read_from_file(Command):
    """
    Read data from file.
    
    Parameters
    ----------
        filename : str
            Enter file name.
    
    """

    fluent_name = "read-from-file"

    argument_names = \
        ['filename']

    filename: filename_cls = filename_cls
    """
    filename argument of read_from_file.
    """
