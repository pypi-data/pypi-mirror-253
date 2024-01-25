#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .contact_resis import contact_resis as contact_resis_cls
class advanced(Group):
    """
    'advanced' child.
    """

    fluent_name = "advanced"

    child_names = \
        ['contact_resis']

    contact_resis: contact_resis_cls = contact_resis_cls
    """
    contact_resis child of advanced.
    """
