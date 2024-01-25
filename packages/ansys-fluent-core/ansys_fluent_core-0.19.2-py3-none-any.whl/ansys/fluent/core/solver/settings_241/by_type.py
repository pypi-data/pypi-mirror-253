#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .only_list_case_boundaries import only_list_case_boundaries as only_list_case_boundaries_cls
from .use_inherent_material_color import use_inherent_material_color as use_inherent_material_color_cls
from .type_name import type_name as type_name_cls
from .reset_2 import reset as reset_cls
class by_type(Group):
    """
    'by_type' child.
    """

    fluent_name = "by-type"

    child_names = \
        ['only_list_case_boundaries', 'use_inherent_material_color',
         'type_name']

    only_list_case_boundaries: only_list_case_boundaries_cls = only_list_case_boundaries_cls
    """
    only_list_case_boundaries child of by_type.
    """
    use_inherent_material_color: use_inherent_material_color_cls = use_inherent_material_color_cls
    """
    use_inherent_material_color child of by_type.
    """
    type_name: type_name_cls = type_name_cls
    """
    type_name child of by_type.
    """
    command_names = \
        ['reset']

    reset: reset_cls = reset_cls
    """
    reset command of by_type.
    """
