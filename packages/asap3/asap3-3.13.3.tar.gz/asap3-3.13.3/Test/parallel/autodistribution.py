from asap3 import *
from asap3.testtools import ReportTest
from asap3.mpi import world
from asap3.io import Trajectory
from ase.io import write
from ase.build import bulk

print_version(1)

if world.rank == 0:
    atoms1 = bulk("Cu", cubic=True).repeat((20,20,20))
    atoms1.set_pbc = False
    atoms1.center(vacuum=5.)
    ReportTest("Number of atoms", len(atoms1), 32000, 0)
    atoms1.set_calculator(EMT())
    e0 = atoms1.get_potential_energy()
    write("serialatoms.traj", atoms1, parallel=False)
else:
    atoms1 = None

world.barrier()
# atoms = MakeParallelAtoms(atoms1, 'auto')
# atoms.set_calculator(EMT())
# e = atoms.get_potential_energy()
# ReportTest("Energy of distributed atoms", e, e0, 1e-3)

atoms = Trajectory("serialatoms.traj").get_atoms(-1, 'auto')
atoms.set_calculator(EMT())
e = atoms.get_potential_energy()
world.barrier()   # Protects cleanup
if world.rank == 0:
    os.unlink('serialatoms.traj')
    ReportTest("Energy of saved atoms", e, e0, 1e-3)

world.barrier()
    
ReportTest.Summary()
