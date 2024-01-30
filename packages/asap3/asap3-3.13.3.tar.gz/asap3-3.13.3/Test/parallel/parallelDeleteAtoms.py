from asap3 import *
from ase.cluster.cubic import FaceCenteredCubic
from asap3.testtools import ReportTest
from asap3.md.velocitydistribution import *
from asap3.analysis import CoordinationNumbers
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution as ASE_MaxwellBoltzmannDistribution
from ase.parallel import world

debug = 0
if debug == 1:
    DebugOutput("deleteatoms%d.log", nomaster=True)
elif debug == 2:
    time.sleep(world.rank)
    print("PID:", os.getpid())
    time.sleep(20)

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
if ismaster:
    atoms = FaceCenteredCubic('Au', surfaces, layers, latticeconstant=lc)
    atoms.center(vacuum=3.0)
else:
    atoms = None

atoms = MakeParallelAtoms(atoms, cpulayout)
MaxwellBoltzmannDistribution(atoms, temperature_K=600)
atoms.calc = EMT()

dyn = Langevin(atoms, 0.5*units.fs, temperature_K=600, friction=0.01)
dyn.run(1)

natoms = atoms.get_global_number_of_atoms()
zap = [0, natoms//2, natoms-1]
print(f"Atoms on {world.rank} (before):", len(atoms))
atoms.delete_atoms_globally(global_indices=zap)
print(f"Atoms on {world.rank} (after):", len(atoms))

ReportTest("Number of atoms reduced by 3", atoms.get_global_number_of_atoms(), natoms - len(zap), 0)
cn = CoordinationNumbers(atoms)
ReportTest("Number of coordination numbers", len(cn), len(atoms), 0)

dyn.run(15)
print("Simulation 1 completed without crashing.")

natoms = atoms.get_global_number_of_atoms()

# Try with different info on different tasks.
if world.size == 2:
    if world.rank == 0:
        zap = [0, natoms//2]
    else:
        zap = [natoms//2, natoms-1]
else:
    if world.rank == 1:
        zap = (natoms//2, natoms-1)
    elif world.rank == 2:
        zap = np.array([natoms//2, 0])
    else:
        zap = []
atoms.delete_atoms_globally(global_indices=zap)

dyn.run(15)

ReportTest("Number of atoms reduced by 3 (inhomogeneous case)", atoms.get_global_number_of_atoms(), natoms - 3, 0)
print("Simulation 2 completed without crashing.")







ReportTest.Summary()
