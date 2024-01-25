#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .face_name import face_name as face_name_cls
class delete_zone(Command):
    """
    'delete_zone' command.
    
    Parameters
    ----------
        face_name : str
            Pick ~a zone you want to delete.
    
    """

    fluent_name = "delete-zone"

    argument_names = \
        ['face_name']

    face_name: face_name_cls = face_name_cls
    """
    face_name argument of delete_zone.
    """
