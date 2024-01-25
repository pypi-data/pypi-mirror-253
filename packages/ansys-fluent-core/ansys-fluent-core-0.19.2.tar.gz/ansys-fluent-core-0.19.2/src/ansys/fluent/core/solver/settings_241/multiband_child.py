#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .start_1 import start as start_cls
from .end import end as end_cls
class multiband_child(Group):
    """
    'child_object_type' of multiband.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'start', 'end']

    name: name_cls = name_cls
    """
    name child of multiband_child.
    """
    start: start_cls = start_cls
    """
    start child of multiband_child.
    """
    end: end_cls = end_cls
    """
    end child of multiband_child.
    """
