#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .from_ import from_ as from__cls
from .to import to as to_cls
class make_a_copy(Command):
    """
    Create a copy of the object.
    
    Parameters
    ----------
        from_ : str
            Select the object to duplicate.
        to : str
            Specify the name of the new object.
    
    """

    fluent_name = "make-a-copy"

    argument_names = \
        ['from_', 'to']

    from_: from__cls = from__cls
    """
    from_ argument of make_a_copy.
    """
    to: to_cls = to_cls
    """
    to argument of make_a_copy.
    """
