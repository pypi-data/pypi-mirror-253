"""Test the FixAtoms constraint and the Subset filter."""

from asap3 import *
from ase.lattice.cubic import FaceCenteredCubic
from asap3.md.velocitydistribution import MaxwellBoltzmannDistribution
from asap3.md.verlet import VelocityVerlet
from asap3.md.nvtberendsen import NVTBerendsen
from ase.constraints import Filter
from asap3.constraints import FixAtoms
from ase.constraints import FixAtoms as ASE_FixAtoms
from asap3.testtools import ReportTest
import numpy as np

def sanity(name, initial, final, fixed):
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

for dynamics in ("Verlet", "NVTBerendsen", "Langevin"):
    init = FaceCenteredCubic(size=(10,10,10), symbol='Cu', pbc=False)
    z = init.get_positions()[:,2]
    fixedatoms = np.less(z, 0.501*z.max())
    print(len(init), sum(fixedatoms))
    MaxwellBoltzmannDistribution(init, temperature_K=2000)
    r_init = init.get_positions()

    print()
    print("Running simulation with Asap's FixAtoms")
    atoms2 = Atoms(init)
    atoms2.set_calculator(EMT())
    atoms2.set_constraint(FixAtoms(mask=fixedatoms))

    if dynamics == "Verlet":
        dyn = VelocityVerlet(atoms2, 3*units.fs)
    elif dynamics == "NVTBerendsen":
        dyn = NVTBerendsen(atoms2, 3*units.fs, temperature_K=2000, taut=200*units.fs)
    elif dynamics == "Langevin":
        dyn = Langevin(atoms2, 3*units.fs, temperature_K=2000, friction=1e-3)
    else:
        assert False
    dyn.run(50)
    r2 = atoms2.get_positions()

    sanity(dynamics+"+FixAtoms", r_init, r2, fixedatoms)

    x = r2[:,0]
    fixedatoms2 = np.less(x, 0.501 * x.max())
    print(len(atoms2), sum(fixedatoms2))

    print("Running simulation with new FixAtoms")
    atoms2.set_constraint(FixAtoms(mask=fixedatoms2))
    #dyn = VelocityVerlet(atoms2, 2*units.fs)

    dyn.run(50)
    r3 = atoms2.get_positions()

    sanity(dynamics+"+new-FixAtoms", r2, r3, fixedatoms2)



print("ALL TESTS SUCCEEDED")



