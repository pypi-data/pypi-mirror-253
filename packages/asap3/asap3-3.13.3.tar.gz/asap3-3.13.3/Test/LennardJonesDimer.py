from asap3 import *
from asap3.testtools import ReportTest
from ase.optimize import QuasiNewton
import numpy as np

# Parameters for Ne-Ar system
# The off-diagonal values are calculated in the test function,
# so we can test the wrong way is caught.
elements = [10, 18]

epsilon = [[0.0036471, 0],
           [0, 0.0123529]]

sigma = [[1.0334400, 0],
         [0, 1.8887100]]

cutoff = 7.55

def runtest(atoms, elements, epsilon, sigma, cutoff, correct=True):
    # Make a copy of the parameters
    epsilon = np.array(epsilon)
    sigma = np.array(sigma)
    if correct:
        # Fill in the cross term
        for p in (epsilon, sigma):
            p[1,0] = np.sqrt(p[0,0] * p[1,1])
    else:
        # Fill in the cross term
        for p in (epsilon, sigma):
            p[0,1] = np.sqrt(p[0,0] * p[1,1])
    print("Epsilon:")
    print(epsilon)
    print("Sigma:")
    print(sigma)
    print("Symbols:", atoms.get_chemical_symbols())

    atoms.set_calculator(LennardJones(elements, epsilon, sigma, cutoff, False))
    dyn = QuasiNewton(atoms)
    dyn.run(fmax=1e-6)
    energy = atoms.get_potential_energy()
    pos = atoms.positions
    diff = pos[1] - pos[0]
    distance = np.linalg.norm(diff)
    print("Distance:", distance)
    print("Energy:", energy)
    return distance, energy

a = Atoms(symbols="Ne2", positions=[[0,0,0], [1.8, 0, 0]], pbc=False)
a.center(vacuum=5.0)
d, e = runtest(a, elements, epsilon, sigma, cutoff)
ReportTest("Energy of Ne2:", e, -epsilon[0][0], 1e-5)
ReportTest("Distance of Ne2:", d, 2**(1/6) * sigma[0][0], 1e-4)

a = Atoms(symbols="Ar2", positions=[[0,0,0], [1.8, 0, 0]], pbc=False)
a.center(vacuum=5.0)
d, e = runtest(a, elements, epsilon, sigma, cutoff)
ReportTest("Energy of Ar2:", e, -epsilon[1][1], 1e-5)
ReportTest("Distance of Ar2:", d, 2**(1/6) * sigma[1][1], 1e-5)

a = Atoms(symbols="NeAr", positions=[[0,0,0], [1.8, 0, 0]], pbc=False)
a.center(vacuum=5.0)
d, e = runtest(a, elements, epsilon, sigma, cutoff)
ReportTest("Energy of NeAr:", e, -np.sqrt(epsilon[0][0]*epsilon[1][1]), 1e-5)
ReportTest("Distance of NeAr:", d, 2**(1/6) * np.sqrt(sigma[0][0]*sigma[1][1]), 1e-5)

try:
    a = Atoms(symbols="NeAr", positions=[[0,0,0], [1.8, 0, 0]], pbc=False)
    a.center(vacuum=5.0)
    d, e = runtest(a, elements, epsilon, sigma, cutoff, correct=False)
except ValueError:
    pass
else:
    raise RuntimeError("LennardJones failed to throw error on incorrect matrix.")

ReportTest.Summary()
