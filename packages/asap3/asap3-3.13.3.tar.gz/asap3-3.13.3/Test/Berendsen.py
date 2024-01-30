from ase.units import fs, GPa
from ase.build import bulk
import asap3
from asap3.md.nvtberendsen import NVTBerendsen
from asap3.md.nptberendsen import NPTBerendsen, Inhomogeneous_NPTBerendsen
from asap3.md import MDLogger
from asap3.md.velocitydistribution import (MaxwellBoltzmannDistribution,
                                             Stationary)
from asap3.testtools import ReportTest
import numpy as np


def test_berendsen(pressure, homog=True):
    """Test NVT or NPT Berendsen dynamics.

    The pressure should be in atomic units.
    """
    rng = np.random.RandomState(None)
    a = bulk('Cu', orthorhombic=True).repeat((5, 5, 4))
    # Introduce an inhomogeneity
    a[7].symbol = 'Au'
    a[8].symbol = 'Au'
    del a[101]
    del a[100]
    print(a)
    a.calc = asap3.EMT()
    # Set temperature to 10 K
    MaxwellBoltzmannDistribution(a, temperature_K=10, force_temp=True, rng=rng)
    Stationary(a)
    ReportTest("Initial temperature", a.get_temperature(), 10, 0.0001)
    # Berendsen dynamics should raise this to 300 K
    T = 300
    if pressure is None:
        md = NVTBerendsen(a, timestep=4 * fs, temperature_K=T,
                              taut=2000*fs,
                              logfile='-', loginterval=500)
    elif homog:
        md = NPTBerendsen(a, timestep=4 * fs, temperature_K=T,
                              taut=2000*fs,
                              pressure_au=pressure, taup=2000*fs,
                              compressibility_au=1 / (140 * GPa))
        # We want logging with stress included
        md.attach(MDLogger(md, a, '-', stress=True), interval=500)
    else:
        md = Inhomogeneous_NPTBerendsen(
            a, timestep=4 * fs, temperature_K=T, taut=2000*fs,
            pressure_au=pressure, taup=2000*fs,
            compressibility_au=1 / (140 * GPa)
            )
        # We want logging with stress included
        md.attach(MDLogger(md, a, '-', stress=True), interval=500)
    md.run(steps=3000)
    # Now gather the temperature over 10000 timesteps, collecting it
    # every 5 steps
    temp = []
    press = []
    for i in range(1000):
        md.run(steps=5)
        temp.append(a.get_temperature())
        p = -a.get_stress(include_ideal_gas=True)[:3].sum() / 3.0
        press.append(p)
    temp = np.array(temp)
    avgtemp = np.mean(temp)
    fluct = np.std(temp)
    avgpressure = np.mean(press)
    print(f"Temperature is {avgtemp:.2f} K +/- {fluct:.2f} K.")
    print(f"Pressure is {avgpressure / GPa:.4f} GPa.")
    ReportTest(f"Temperarure ({md.__class__})", avgtemp, T, 10.0)
    if pressure is not None:
        ReportTest(f"Pressure ({md.__class__})", avgpressure, pressure, 0.05 * GPa)

test_berendsen(None)

test_berendsen(1.0 * GPa)

test_berendsen(1.0 * GPa, False)

ReportTest.Summary()
