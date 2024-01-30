from ase.units import fs, GPa
from ase.build import bulk
import asap3
from asap3.md.npt import NPT
from asap3.md.nptberendsen import NPTBerendsen
from asap3.md import MDLogger
from asap3.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from asap3.testtools import ReportTest
import numpy as np


def test_npt_asap():
    pressure = 1.0 * GPa
    rng = np.random.RandomState(0)
    a = bulk('Cu', orthorhombic=True).repeat((6, 6, 4))
    print(a)
    a.calc = asap3.EMT()
    # NPT Dynamics is awful at setting correct pressure and
    # temperature, but should be good at maintaining it.  Use
    # NPTBerendsen to hit the right value.
    T = 300
    MaxwellBoltzmannDistribution(a, temperature_K=T, force_temp=True, rng=rng)
    Stationary(a)
    berend = NPTBerendsen(a, timestep=4 * fs, temperature_K=T,
                          taut=2000*fs,
                          pressure_au=pressure, taup=2000*fs,
                          compressibility_au=1 / (140 * GPa),
                          logfile='-', loginterval=500)
    berend.run(steps=3000)
    # Now gather the temperature over 10000 timesteps, collecting it every 5 steps
    ptime = 2000 * fs
    md = NPT(a, timestep=4 * fs, temperature_K=T, externalstress=pressure,
                 ttime=2000 * fs, pfactor=ptime**2/(140 / GPa))
    # We want logging with stress included
    md.attach(MDLogger(md, a, '-', stress=True), interval=500)
    temp = []
    press = []
    for i in range(2000):
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
    ReportTest("Temperature", avgtemp, T, 10.0)
    ReportTest("Pressure", avgpressure, pressure, 0.02 * GPa)


test_npt_asap()
