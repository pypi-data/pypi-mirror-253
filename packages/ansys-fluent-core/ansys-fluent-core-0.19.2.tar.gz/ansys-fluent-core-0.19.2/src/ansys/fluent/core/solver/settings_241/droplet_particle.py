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
from .droplet_particle_child import droplet_particle_child

class droplet_particle(NamedObject[droplet_particle_child], _CreatableNamedObjectMixin[droplet_particle_child]):
    """
    'droplet_particle' child.
    """

    fluent_name = "droplet-particle"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of droplet_particle.
    """
    list: list_cls = list_cls
    """
    list command of droplet_particle.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of droplet_particle.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of droplet_particle.
    """
    child_object_type: droplet_particle_child = droplet_particle_child
    """
    child_object_type of droplet_particle.
    """
