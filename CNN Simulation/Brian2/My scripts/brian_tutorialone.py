from brian2 import *

path = "C:\\Users\\pc1rss\\Dropbox\\NeuralCGI\\Brian2\\My scripts\\Results and plots\\"

# Make sure that any Brian objects created before the function is called aren't included in the next run

start_scope()

# In Brian, all models are defined by systems of differential equation #

#  In order to make v stay constant during the refractory period, we have to add (unless refractory) #

N = 500
tau = 100*ms
tau_t = 100*ms
duration = 500*ms

v0_max = 3.
vr = -70*mV  # Resting potential
vt0 = -50*mV  # Threshold

delta_vt0 = 5*mV
v_drive = 2*(vt0-vr)
sigma = 0.5*(vt0-vr)

eqs = '''
dv/dt = (v_drive+vr-v)/tau + sigma*xi*tau**-0.5 : volt
dvt/dt = (vt0-vt)/tau_t : volt
'''

reset = '''
v = vr
vt += delta_vt0
'''


print('Simulation started...')

# Creates the neuronal group #

# When v>0.8 we fire a spike, and immediately reset v = 0 after the spike. #

G = NeuronGroup(N, eqs, threshold='v>vt', reset=reset, method='euler', refractory=5*ms)

# 'exact' method that we used earlier is not applicable to stochastic differential equations #

#G.v = 'rand()'  # Initialises each neuron with a different uniform random value between 0 and 1
#G.v0 = 'i*v0_max/(N-1)'

G.v = 'rand()*(vt0-vr)+vr'
G.vt = vt0  # Initialising threshold as vt0?

M = StateMonitor(G, 'v', record=True)  # Used to record the values of a neuron variable when the simulation runs

spikemonitor = SpikeMonitor(G)  # Records the spikes of a group

# Runs the simulation for 1 second #

run(duration)

print('Spike times: %s' % spikemonitor.t[:])

# Plots time x voltage #

fig = plt.figure(figsize=(20, 10), dpi=100)

plot(spikemonitor.t/ms, spikemonitor.i, '.k')

xlabel('Time (ms)')
ylabel('Simulated Neuron (N)')

plt.savefig(path+"500_stochasticneurons_resetest.png")
