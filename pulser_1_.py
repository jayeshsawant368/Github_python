import pulser
import scipy as sp
import numpy as np
from matplotlib import pyplot as plt

device=pulser.AnalogDevice

#---------Defining the Register (only single atom)-----------

reg=pulser.Register.from_coordinates([(0,0)], prefix="q")
reg.draw()

#----------initializing the sequence for our programm---------

sequence=pulser.Sequence(reg,device)
sequence.declare_channel("rydberg_global", "rydberg_global")
print("The states used in the computation are", sequence.get_addressed_states())

#------------pulse code for real (global)---------------------

pi_pulse=pulser.Pulse.ConstantPulse(1000,np.pi,0,0)
sequence.add(pi_pulse, "rydberg_global")
sequence.draw(mode="input")

#------------backend in the QuTip------------------------------

backend=pulser.backends.QutipBackendV2(sequence)
result=backend.run()

result.final_bitstrings