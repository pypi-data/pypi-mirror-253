import numpy as np

from ase import Atoms, units
from ase.data import atomic_numbers
from asap3 import Morse, PropertyNotImplementedError

# Copied from old version of ase.test.testsuite
class must_raise:
    """Context manager for checking raising of exceptions."""
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is None:
            raise RuntimeError('Failed to fail: ' + str(self.exception))
        return issubclass(exc_type, self.exception)

# Define constants and calculator
elements = np.array([atomic_numbers['Ru'], atomic_numbers['Ar']])
epsilon = np.array([[5.720, 0.092], [0.092, 0.008]])
alpha = np.array([[1.475, 2.719], [2.719, 1.472]])
rmin = np.array([[2.110, 2.563], [2.563, 4.185]])
rcut = rmin.max() + 6.0 / alpha.min()

calc = Morse(elements, epsilon, alpha, rmin)
atoms = Atoms(['Ar', 'Ar'], [[0.0, 0.0, 0.0], [rcut + 1.0, 0.0, 0.0]])
atoms.center(vacuum=10.0)
atoms.set_pbc(True)
atoms.set_calculator(calc)

# This should not fail
energy = atoms.get_potential_energy()

#This should fail
with must_raise(PropertyNotImplementedError):
    stress = atoms.get_stress()

