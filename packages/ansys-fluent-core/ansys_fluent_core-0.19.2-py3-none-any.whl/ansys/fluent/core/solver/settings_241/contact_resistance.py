#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .add_contact_resistance import add_contact_resistance as add_contact_resistance_cls
from .list_contact_face import list_contact_face as list_contact_face_cls
from .delete_contact_face import delete_contact_face as delete_contact_face_cls
class contact_resistance(Group):
    """
    'contact_resistance' child.
    """

    fluent_name = "contact-resistance"

    command_names = \
        ['add_contact_resistance', 'list_contact_face', 'delete_contact_face']

    add_contact_resistance: add_contact_resistance_cls = add_contact_resistance_cls
    """
    add_contact_resistance command of contact_resistance.
    """
    list_contact_face: list_contact_face_cls = list_contact_face_cls
    """
    list_contact_face command of contact_resistance.
    """
    delete_contact_face: delete_contact_face_cls = delete_contact_face_cls
    """
    delete_contact_face command of contact_resistance.
    """
