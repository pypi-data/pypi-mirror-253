#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .write_to_file_1 import write_to_file as write_to_file_cls
from .file_name_1 import file_name as file_name_cls
from .include_in_domains_particles import include_in_domains_particles as include_in_domains_particles_cls
from .pick_injection import pick_injection as pick_injection_cls
from .injection_2 import injection as injection_cls
class extended_summary(Command):
    """
    Print extended discrete phase summary report of particle fates, with options.
    
    Parameters
    ----------
        write_to_file : bool
            'write_to_file' child.
        file_name : str
            'file_name' child.
        include_in_domains_particles : bool
            'include_in_domains_particles' child.
        pick_injection : bool
            'pick_injection' child.
        injection : str
            'injection' child.
    
    """

    fluent_name = "extended-summary"

    argument_names = \
        ['write_to_file', 'file_name', 'include_in_domains_particles',
         'pick_injection', 'injection']

    write_to_file: write_to_file_cls = write_to_file_cls
    """
    write_to_file argument of extended_summary.
    """
    file_name: file_name_cls = file_name_cls
    """
    file_name argument of extended_summary.
    """
    include_in_domains_particles: include_in_domains_particles_cls = include_in_domains_particles_cls
    """
    include_in_domains_particles argument of extended_summary.
    """
    pick_injection: pick_injection_cls = pick_injection_cls
    """
    pick_injection argument of extended_summary.
    """
    injection: injection_cls = injection_cls
    """
    injection argument of extended_summary.
    """
