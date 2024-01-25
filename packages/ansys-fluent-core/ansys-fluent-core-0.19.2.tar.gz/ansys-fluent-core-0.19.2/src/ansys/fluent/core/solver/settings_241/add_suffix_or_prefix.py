#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .zone_name_6 import zone_name as zone_name_cls
from .append import append as append_cls
from .text import text as text_cls
class add_suffix_or_prefix(Command):
    """
    Add suffix or prefix to zone name.
    
    Parameters
    ----------
        zone_name : typing.List[str]
            Enter zone name list.
        append : bool
            'append' child.
        text : str
            'text' child.
    
    """

    fluent_name = "add-suffix-or-prefix"

    argument_names = \
        ['zone_name', 'append', 'text']

    zone_name: zone_name_cls = zone_name_cls
    """
    zone_name argument of add_suffix_or_prefix.
    """
    append: append_cls = append_cls
    """
    append argument of add_suffix_or_prefix.
    """
    text: text_cls = text_cls
    """
    text argument of add_suffix_or_prefix.
    """
