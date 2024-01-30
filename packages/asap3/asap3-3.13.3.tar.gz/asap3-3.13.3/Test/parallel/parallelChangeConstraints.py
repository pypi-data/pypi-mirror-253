"""Test the FixAtoms constraint and the Subset filter."""

from asap3 import *
from ase.lattice.cubic import FaceCenteredCubic
from asap3.md.velocitydistribution import MaxwellBoltzmannDistribution
from asap3.md.verlet import VelocityVerlet
from asap3.md.nvtberendsen import NVTBerendsen
from asap3.constraints import Filter, FixAtoms
from ase.constraints import FixAtoms as ASE_FixAtoms
from asap3.testtools import ReportTest
from asap3.mpi import world
import numpy as np

debug = 0
if debug == 1:
    DebugOutput("parallelconstraints%d.log", nomaster=True)
elif debug == 2:
    time.sleep(world.rank)
    print("PID:", os.getpid())
    time.sleep(20)

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

def sanity(name, atoms):
    initial = atoms.arrays['r_init']
    final = atoms.get_positions()
    fixed = atoms.get_tags().astype(bool)
    
    print(f"Sanity check, {name}:")
    ok = (final == initial) + np.logical_not(fixed)[:,np.newaxis]
    if ok.all():
        print("  Stationary atoms have not moved: OK")
    else:
        raise RuntimeError(f"Stationary atoms have moved ({name})")
    ok = (final != initial) + fixed[:,np.newaxis]
    if ok.all():
        print("  Mobile atoms have moved: OK")
    else:
        raise RuntimeError(f"Mobile atoms have not moved ({name})")

for dynamics in ("Verlet", "NVTBerendsen", "Langevin",):
    
    if ismaster:
        size = 5 * np.array(cpulayout)
        init = FaceCenteredCubic(size=size, symbol='Cu', pbc=False)
        z = init.get_positions()[:,2]
        fixedatoms = np.less(z, 0.501*z.max())
        print(len(init), sum(fixedatoms))
        MaxwellBoltzmannDistribution(init, temperature_K=6000)
        init.set_tags(fixedatoms)
    else:
        init = None


    print()
    print("Running simulation with Asap's FixAtoms")
    atoms2 = MakeParallelAtoms(init, cpulayout)
    atoms2.arrays['r_init'] = atoms2.get_positions()
    atoms2.set_calculator(EMT())
    atoms2.set_constraint(FixAtoms(mask=atoms2.get_tags().astype(bool)))

    if dynamics == "Verlet":
        dyn = VelocityVerlet(atoms2, 3*units.fs)
    elif dynamics == "NVTBerendsen":
        dyn = NVTBerendsen(atoms2, 3*units.fs, temperature_K=2000, taut=200*units.fs)
    elif dynamics == "Langevin":
        dyn = Langevin(atoms2, 3*units.fs, temperature_K=2000, friction=1e-3)
    else:
        assert False
    dyn.run(1000)

    sanity(dynamics+"+FixAtoms", atoms2)

    x = atoms2.get_positions()[:,0]
    fixedatoms2 = np.less(x, 0.501 * x.max())
    atoms2.set_tags(fixedatoms2)
    atoms2.arrays['r_init'] = atoms2.get_positions()
    atoms2.set_constraint(FixAtoms(mask=fixedatoms2))

    dyn.run(1000)

    sanity(dynamics+"+new-FixAtoms", atoms2)

print("ALL TESTS SUCCEEDED!")



