#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .face_zone_name import face_zone_name as face_zone_name_cls
from .move_faces import move_faces as move_faces_cls
class sep_face_zone_face(Command):
    """
    Separate each face in a zone into unique zone.
    
    Parameters
    ----------
        face_zone_name : str
            Enter a zone name.
        move_faces : bool
            'move_faces' child.
    
    """

    fluent_name = "sep-face-zone-face"

    argument_names = \
        ['face_zone_name', 'move_faces']

    face_zone_name: face_zone_name_cls = face_zone_name_cls
    """
    face_zone_name argument of sep_face_zone_face.
    """
    move_faces: move_faces_cls = move_faces_cls
    """
    move_faces argument of sep_face_zone_face.
    """
