from asap3 import *
from ase.cluster.cubic import FaceCenteredCubic
from asap3.testtools import ReportTest
from asap3.md.velocitydistribution import *
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution as ASE_MaxwellBoltzmannDistribution
from ase.parallel import world

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


# We need an asymmetric nanoparticle
surfaces = [(1, 0, 0), (1, 1, 1), (0, -1, 0), (-1, 0, 0)]
layers = [9, 7, 7, 8]
lc = 4.08000


###  Test the MaxwellBoltzmann distribution in parallel
if ismaster:
    atoms = FaceCenteredCubic('Au', surfaces, layers, latticeconstant=lc)
    atoms.center(vacuum=3.0)
else:
    atoms = None

atoms = MakeParallelAtoms(atoms, cpulayout)
MaxwellBoltzmannDistribution(atoms, temperature_K=300, force_temp=True)
ReportTest("Temperature of Maxwell-Boltzmann distribution", atoms.get_temperature(), 300, 1e-6)


### Test the following:
###    ParallelListOfAtoms.get_center_of_mass()
###    ParallelListOfAtoms.get_angular_momentum()
###    ParallelListOfAtoms.get_moments_of_inertial()
###    Stationary()
###    ZeroRotation()

# Create an atoms object with a nonzero angular momentum and center of mass momentum

if ismaster:
    atoms = FaceCenteredCubic('Au', surfaces, layers, latticeconstant=lc)
    atoms.center(vacuum=3.0)
    ASE_MaxwellBoltzmannDistribution(atoms, temperature_K=300, force_temp=True, communicator='serial')
    ReportTest("Temperature of serial Maxwell-Boltzmann distribution", atoms.get_temperature(), 300, 1e-6)
    atoms[0].momentum += np.array((0, 1.0, 0))
    init_com = atoms.get_center_of_mass()
    init_am = atoms.get_angular_momentum()
    init_mi = atoms.get_moments_of_inertia()
else:
    atoms = None

atoms = MakeParallelAtoms(atoms, cpulayout)
temp = atoms.get_temperature()
com = atoms.get_center_of_mass()
am = atoms.get_angular_momentum()
mi = atoms.get_moments_of_inertia()
if ismaster:
    for i, ax in enumerate('xyz'):
        ReportTest(f"Center of mass ({ax})", com[i], init_com[i], 1e-6)
        ReportTest(f"Angular momentum ({ax})", am[i], init_am[i], 1e-6)
        ReportTest(f"Moments of inertial ({ax})", mi[i], init_mi[i], 1e-6)
    print("Angular momentum:", am)
    
Stationary(atoms)
ReportTest("Temperature after Stationary(atoms)", atoms.get_temperature(), temp, 1e-6)
ZeroRotation(atoms)
ReportTest("Temperature after ZeroRotation(atoms)", atoms.get_temperature(), temp, 1e-6)
am = atoms.get_angular_momentum()
for i, ax in enumerate('xyz'):
    ReportTest(f"Angular momentum ({ax}) is zero", am[i], 0, 1e-6)


### Finalize

ReportTest.Summary()

