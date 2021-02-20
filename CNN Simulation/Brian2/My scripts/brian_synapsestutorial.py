from brian2 import *
import seaborn as sns


def visualise_connectivity(path, S):

    sns.set(context='notebook', style='whitegrid', font_scale=4)

    sns.set_context("talk", rc={"font.size": 30, "axes.titlesize": 30, "axes.labelsize": 35, "lines.linewidth": 2,
                                "xtick.labelsize": 25, "ytick.labelsize": 25, "lines.markersize": 15})

    Ns = len(S.source)
    Nt = len(S.target)

    fig = figure(figsize=(40, 16))

    subplot(121)

    plot(zeros(Ns), arange(Ns), 'ok', ms=10)
    plot(ones(Nt), arange(Nt), 'ok', ms=10, color='grey')

    for i, j in zip(S.i, S.j):

        plot([0, 1], [i, j], '-k')

    xticks([0, 1], ['Source', 'Target'])

    ylabel('Neuron index')
    xlim(-0.1, 1.1)
    ylim(-1, max(Ns, Nt))

    subplot(122)
    plot(S.i, S.j, 'ok')
    xlim(-1, Ns)
    ylim(-1, Nt)
    xlabel('Source neuron index')
    ylabel('Target neuron index')

    plt.savefig(path + "Graph.png")

    return fig


path = "C:\\Users\\pc1rss\\Dropbox\\NeuralCGI\\Brian2\\My scripts\\Results and plots\\"


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

M = StateMonitor(G, 'v', record=True)

run(100*ms)

plot(M.t/ms, M.v[0], label='Neuron 0')
plot(M.t/ms, M.v[1], label='Neuron 1')
plot(M.t/ms, M.v[2], label='Neuron 2')
xlabel('Time (ms)')
ylabel('v')
legend()

plt.savefig(path+"3_connected.png")


start_scope()

N = 100

G = NeuronGroup(N, 'v:1')  # Neurons

S = Synapses(G, G)  # Synapses

# Connectivity rule : connect all pairs of neurons i and j with probability 0.002 as long as the condition i!=j holds #

S.connect(condition='i!=j', p=0.002, skip_if_invalid=True) # skip_if_invalid to avoid errors at the boundaries

visualise_connectivity(path, S)
