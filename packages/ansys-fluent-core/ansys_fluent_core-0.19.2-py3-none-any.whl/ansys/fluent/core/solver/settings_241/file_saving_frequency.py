#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .volume_heat_run import volume_heat_run as volume_heat_run_cls
from .face_heat_run import face_heat_run as face_heat_run_cls
from .face_temperature_run import face_temperature_run as face_temperature_run_cls
from .joule_heat_run import joule_heat_run as joule_heat_run_cls
class file_saving_frequency(Group):
    """
    'file_saving_frequency' child.
    """

    fluent_name = "file-saving-frequency"

    child_names = \
        ['volume_heat_run', 'face_heat_run', 'face_temperature_run',
         'joule_heat_run']

    volume_heat_run: volume_heat_run_cls = volume_heat_run_cls
    """
    volume_heat_run child of file_saving_frequency.
    """
    face_heat_run: face_heat_run_cls = face_heat_run_cls
    """
    face_heat_run child of file_saving_frequency.
    """
    face_temperature_run: face_temperature_run_cls = face_temperature_run_cls
    """
    face_temperature_run child of file_saving_frequency.
    """
    joule_heat_run: joule_heat_run_cls = joule_heat_run_cls
    """
    joule_heat_run child of file_saving_frequency.
    """
