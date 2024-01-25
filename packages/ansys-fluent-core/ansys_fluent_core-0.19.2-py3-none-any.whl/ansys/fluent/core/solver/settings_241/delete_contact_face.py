#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .face_name_1 import face_name as face_name_cls
class delete_contact_face(Command):
    """
    'delete_contact_face' command.
    
    Parameters
    ----------
        face_name : str
            Pick contact face you want to delete.
    
    """

    fluent_name = "delete-contact-face"

    argument_names = \
        ['face_name']

    face_name: face_name_cls = face_name_cls
    """
    face_name argument of delete_contact_face.
    """
