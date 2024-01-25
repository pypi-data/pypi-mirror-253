#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .injection_thread import injection_thread as injection_thread_cls
from .coupled import coupled as coupled_cls
from .extraction_thread import extraction_thread as extraction_thread_cls
from .uniform import uniform as uniform_cls
from .injection_hole_count import injection_hole_count as injection_hole_count_cls
from .discrete_ext import discrete_ext as discrete_ext_cls
from .static import static as static_cls
from .formulation import formulation as formulation_cls
from .holes_setup import holes_setup as holes_setup_cls
from .dynamic_setup import dynamic_setup as dynamic_setup_cls
from .static_setup import static_setup as static_setup_cls
class injection_child(Group):
    """
    'child_object_type' of injection.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['injection_thread', 'coupled', 'extraction_thread', 'uniform',
         'injection_hole_count', 'discrete_ext', 'static', 'formulation',
         'holes_setup', 'dynamic_setup', 'static_setup']

    injection_thread: injection_thread_cls = injection_thread_cls
    """
    injection_thread child of injection_child.
    """
    coupled: coupled_cls = coupled_cls
    """
    coupled child of injection_child.
    """
    extraction_thread: extraction_thread_cls = extraction_thread_cls
    """
    extraction_thread child of injection_child.
    """
    uniform: uniform_cls = uniform_cls
    """
    uniform child of injection_child.
    """
    injection_hole_count: injection_hole_count_cls = injection_hole_count_cls
    """
    injection_hole_count child of injection_child.
    """
    discrete_ext: discrete_ext_cls = discrete_ext_cls
    """
    discrete_ext child of injection_child.
    """
    static: static_cls = static_cls
    """
    static child of injection_child.
    """
    formulation: formulation_cls = formulation_cls
    """
    formulation child of injection_child.
    """
    holes_setup: holes_setup_cls = holes_setup_cls
    """
    holes_setup child of injection_child.
    """
    dynamic_setup: dynamic_setup_cls = dynamic_setup_cls
    """
    dynamic_setup child of injection_child.
    """
    static_setup: static_setup_cls = static_setup_cls
    """
    static_setup child of injection_child.
    """
