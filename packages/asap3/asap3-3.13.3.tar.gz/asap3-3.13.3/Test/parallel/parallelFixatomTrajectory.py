from asap3 import *
from asap3.md.verlet import VelocityVerlet
from ase.lattice.cubic import FaceCenteredCubic
from asap3.io.trajectory import *
from ase.parallel import world
from asap3.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from asap3.constraints import FixAtoms
from ase.io import read
import os

print_version(1)
#set_verbose(1)

ismaster = world.rank == 0
isparallel = world.size != 1
if world.size == 1:
    cpulayout = None
elif world.size == 2:
    cpulayout = [2,1,1]
elif world.size == 3:
    cpulayout = [1,3,1]
elif world.size == 4:
    cpulayout = [2,1,2]
else:
    cpulayout = 'auto'

delete = True
filename = "fixatoms.traj"

if ismaster:
    initial = FaceCenteredCubic(size=(10,10,10), symbol="Cu", pbc=(1,0,0))
else:
    initial = None
if isparallel:
    atoms = MakeParallelAtoms(initial, cpulayout)
    atoms.set_constraint(FixAtoms(mask=(atoms.get_ids() < 5)))
else:
    atoms = initial.copy()
    atoms.set_constraint(FixAtoms(indices=range(5)))

atoms.set_calculator(EMT())
MaxwellBoltzmannDistribution(atoms, temperature_K=5000)
Stationary(atoms)

dyn = VelocityVerlet(atoms, 3*units.fs)
traj = Trajectory(filename, "w", atoms)
dyn.attach(traj, interval=10)
dyn.run(50)

e = atoms.get_potential_energy()

atoms2 = read(filename)
e2 = atoms2.get_potential_energy()

world.barrier()
if delete and world.rank == 0:
    os.remove(filename)
    
world.barrier()
