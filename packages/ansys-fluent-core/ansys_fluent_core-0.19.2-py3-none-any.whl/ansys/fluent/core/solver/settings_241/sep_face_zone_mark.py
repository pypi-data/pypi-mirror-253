#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .face_zone_name import face_zone_name as face_zone_name_cls
from .register_name import register_name as register_name_cls
from .move_faces import move_faces as move_faces_cls
class sep_face_zone_mark(Command):
    """
    Separate a face zone based on cell marking.
    
    Parameters
    ----------
        face_zone_name : str
            Enter a zone name.
        register_name : str
            'register_name' child.
        move_faces : bool
            'move_faces' child.
    
    """

    fluent_name = "sep-face-zone-mark"

    argument_names = \
        ['face_zone_name', 'register_name', 'move_faces']

    face_zone_name: face_zone_name_cls = face_zone_name_cls
    """
    face_zone_name argument of sep_face_zone_mark.
    """
    register_name: register_name_cls = register_name_cls
    """
    register_name argument of sep_face_zone_mark.
    """
    move_faces: move_faces_cls = move_faces_cls
    """
    move_faces argument of sep_face_zone_mark.
    """
