from brian2 import *

start_scope()  # Brian objects created before the function is called aren't included in the next run

eqs = '''
dv/dt = (I-v)/tau : 1
I : 1
tau : second
'''

G = NeuronGroup(3, eqs, threshold='v>1', reset='v = 0', method='exact')

G.I = [2, 0, 0]
G.tau = [10, 100, 100]*ms


S = Synapses(G, G, 'w : 1', on_pre='v_post += w')
S.connect(i=0, j=[1, 2])
S.w = 'j*0.5'  # Weight
S.delay = 'j*2*ms'  # Delay
N = 4000
t = -50*mV
reset = -60*mV


M = SpikeMonitor(G)
trace = StateMonitor(G, 'v', record=0)

ion()

run(1*second)



subplot(211)

rasterline, = plot([], [], '.')  # plot points, hence the '.' axis([0, 1, 0, N])

subplot(212)

traceline, = plot([], [])  # plot lines, hence no '.' axis([0, 1, -0.06, -0.05])


#@network_operation(clock=Clock(dt=10*ms))
def draw_gfx():  # This returns two lists i, t of the neuron indices and spike times for # all the recorded spikes

    rasterline.set_xdata(M.t/ms)
    rasterline.set_ydata(M.i)

    traceline.set_xdata(trace.t)
    #traceline.set_ydata(trace[0])  # and finally tell pylab to redraw it
    draw()

draw_gfx()
