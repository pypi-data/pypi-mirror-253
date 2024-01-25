#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .delete_1 import delete as delete_cls
from .list import list as list_cls
from .list_properties_1 import list_properties as list_properties_cls
from .make_a_copy import make_a_copy as make_a_copy_cls
from .multi_component_diffusion_mf_child import multi_component_diffusion_mf_child

class multi_component_diffusion_mf(NamedObject[multi_component_diffusion_mf_child], _NonCreatableNamedObjectMixin[multi_component_diffusion_mf_child]):
    """
    'multi_component_diffusion_mf' child.
    """

    fluent_name = "multi-component-diffusion-mf"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of multi_component_diffusion_mf.
    """
    list: list_cls = list_cls
    """
    list command of multi_component_diffusion_mf.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of multi_component_diffusion_mf.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of multi_component_diffusion_mf.
    """
    child_object_type: multi_component_diffusion_mf_child = multi_component_diffusion_mf_child
    """
    child_object_type of multi_component_diffusion_mf.
    """
