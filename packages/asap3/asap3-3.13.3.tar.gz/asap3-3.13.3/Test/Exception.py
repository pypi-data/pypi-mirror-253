from asap3 import *
from ase.lattice.cubic import *

testname = "Illegal elements are an error."
atoms = FaceCenteredCubic(size=(10, 10, 10), symbol="Cu")
z = atoms.get_atomic_numbers()
z[7]=8
atoms.set_atomic_numbers(z)

try:
    atoms.set_calculator(EMT())
except AsapError:
    print("Test passed:", testname)
else:
    raise RuntimeError("Test failed: "+testname)
    
testname = "Atoms on top of each other."
atoms = FaceCenteredCubic(size=(10, 10, 10), symbol="Cu")
r = atoms.get_positions()
r[10] = r[11]
atoms.set_positions(r)
atoms.set_calculator(EMT())
try:
    e = atoms.get_potential_energy()
except AsapError:
    print("Test passed:", testname)
else:
    raise RuntimeError("Test failed: "+testname)

testname = "Atoms with malformed array (size)."
atoms = FaceCenteredCubic(size=(10, 10, 10), symbol="Cu")
atoms.arrays['numbers'] = atoms.arrays['numbers'][:len(atoms)//2]

try:
    atoms.set_calculator(EMT())
    e = atoms.get_potential_energy()
except AsapError:
    print("Test passed:", testname)
else:
    raise RuntimeError("Test failed: "+testname)

testname = "Atoms with malformed array (type)."
atoms = FaceCenteredCubic(size=(10, 10, 10), symbol="Cu")
atoms.arrays['positions'] = atoms.arrays['positions'].astype(int)

try:
    atoms.set_calculator(EMT())
    e = atoms.get_potential_energy()
except AsapError:
    print("Test passed:", testname)
else:
    raise RuntimeError("Test failed: "+testname)

