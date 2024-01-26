from ase import Atoms
import ase.io
import dpdata

from typing import List, Optional
from collections import OrderedDict
import os

from ai2_kit.core.util import list_split
from ai2_kit.domain.cp2k import dump_coord_n_cell
import ai2_kit.tool.dpdata  # register custom fields

class Cp2kTask:
    tag: str
    config_file: str
    wannier_file: str


class LabelTaskBuilder:
    """
    This this a builder to generate labeling task.
    """
    def __init__(self):
        self._atoms_list: List[Atoms] = []
        self._cp2k_tasks = OrderedDict()
        self._concurrency = 5

    def add_system(self, path):
        ...

    def set_cp2k_task(self, neutral: str, x: str, y: str, z: str):
        ...

    def set_script(self,
                   concurrency: int = 5,
                   batch_template: Optional[str] = None,
                   ):
        ...

    def make_dirs(self, out_dir: str):
        os.makedirs(out_dir, exist_ok=True)
        task_dirs = []
        for i, atoms in enumerate(self._atoms_list):
            task_name = f'{i:04d}-{atoms.get_chemical_formula()}'
            task_dir = os.path.join(out_dir, task_name)
            os.makedirs(task_dir, exist_ok=True)
            # create coord_n_cell.inc
            sys_file = os.path.join(task_dir, 'coord_n_cell.inc')
            with open(sys_file, 'w') as f:
                dump_coord_n_cell(f, atoms)
            #


            # create cp2k input file
            task_dirs.append(task_dir)



def dpdata_read_cp2k_data(cp2k_dir: str,
                          polar_x: str = 'polar_x.wannier',
                          polar_y: str = 'polar_y.wannier',
                          polar_z: str = 'polar_z.wannier',):
    dp_sys = dpdata.LabeledSystem(cp2k_dir , fmt='cp2k/output')
    nframes = dp_sys.get_nframes()
    natoms = dp_sys.get_natoms()

    wannier_x = ase.io.read(os.path.join(cp2k_dir, polar_x), index=0, format='extxyz')
    wannier_y = ase.io.read(os.path.join(cp2k_dir, polar_y), index=0, format='extxyz')
    wannier_z = ase.io.read(os.path.join(cp2k_dir, polar_z), index=0, format='extxyz')


