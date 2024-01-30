from ase.units import fs, kB
from ase.build import bulk
import asap3
from asap3.md.langevin import Langevin
from asap3.md.velocitydistribution import (MaxwellBoltzmannDistribution,
                                             Stationary)
from asap3.testtools import ReportTest

import numpy as np

# rng = np.random.RandomState(0)
a = bulk('Au', cubic=True).repeat((5, 5, 5))
a.pbc = (False, False, False)
a.center(vacuum=2.0)
print(a)
a.calc = asap3.EMT()
# Set temperature to 10 K
MaxwellBoltzmannDistribution(a, temperature_K=10, force_temp=True)
Stationary(a)
ReportTest("Initial temperature", a.get_temperature(), 10, 0.0001)
# Langevin dynamics should raise this to 300 K
T = 300
md = Langevin(a, timestep=4 * fs, temperature_K=T, friction=0.01,
                  logfile='-', loginterval=500)
md.run(steps=5000)
# Now gather the temperature over 10000 timesteps, collecting it
# every 5 steps
temp = []
energy = []
com = a.get_center_of_mass()
for i in range(2000):
    md.run(steps=5)
    temp.append(a.get_temperature())
    energy.append(a.get_potential_energy() + a.get_kinetic_energy())
temp = np.array(temp)
avgtemp = np.mean(temp)
fluct = np.std(temp)
avgenergy = np.mean(energy)
print(f"Temperature is {avgtemp:.2f} K +/- {fluct:.2f} K")
ReportTest("Average temperature", avgtemp, T, 10.0)

delta = np.linalg.norm(a.get_center_of_mass() - com)
ReportTest("Change in center of mass", delta, 0.0, 1e-9)

ReportTest.Summary()

