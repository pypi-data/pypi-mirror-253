from asap3.md.verlet import VelocityVerlet
from asap3.md.langevin import Langevin
from asap3.md.velocitydistribution import MaxwellBoltzmannDistribution
from asap3 import EMT
from asap3.testtools import ReportTest
from ase.build import bulk
from ase import units
import numpy as np

# Global parameters:
T=300
timestep=5

def testmd(atoms, dynclass, name, dynkwargs={}):
    MaxwellBoltzmannDistribution(atoms, temperature_K=T*2, force_temp=True)
    atoms.set_calculator(EMT())
    dyn = dynclass(atoms, timestep=timestep*units.fs, **dynkwargs)
    tt =  atoms.get_temperature()
    print("Initial temperature:", tt)
    ReportTest(f"Initial temperature ({name})", tt, 2*T, 1e-9)
    p = atoms.get_momenta()
    print("Initial square momenta:", (p*p).sum())
    dyn.run(500)
    tt =  atoms.get_temperature()
    print("Final temperature:", tt)
    ReportTest(f"Final temperature ({name})", tt, T, 20.0)
    p = atoms.get_momenta()
    print("Final square momenta:", (p*p).sum())
    print()

mass_Cu = 63.546
size = 7

atoms = bulk('Cu', cubic=True).repeat((size,size,size))
assert len(atoms) == 4*size**3
testmd(atoms, VelocityVerlet, "Verlet - normal")

atoms = bulk('Cu', cubic=True).repeat((size,size,size))
atoms.set_masses(0.5*mass_Cu*np.ones(len(atoms)))
testmd(atoms, VelocityVerlet, "Verlet - low mass")

lgvkw = {'temperature_K': T, 'friction':0.05}
atoms = bulk('Cu', cubic=True).repeat((size,size,size))
testmd(atoms, Langevin, "Langevin - normal", lgvkw)

atoms = bulk('Cu', cubic=True).repeat((size,size,size))
atoms.set_masses(0.5*mass_Cu*np.ones(len(atoms)))
testmd(atoms, Langevin, "Langevin - low mass", lgvkw)

ReportTest.Summary()
