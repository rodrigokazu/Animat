from brian2 import *

set_device('cpp_standalone')


@implementation('cpp','''
// Note that functions always need a return value at the moment
double store_spike(int i, double t) {
    static std::ofstream spike_file("C:/Users/pc1rss/Dropbox/NeuralCGI/Brian2/My scripts/Results and plots/spikes.txt");
    spike_file << i << " " << t << std::endl;
    return 0.;  // unused
}
''')


@check_units(i=1, t=second, result=1)
def store_spike(i, t):

    raise NotImplementedError('Use standalone mode')


G = NeuronGroup(10, 'rates : Hz (constant)', threshold='rand()<rates*dt', reset='dummy_var = store_spike(i, t)')
G.rates = '50*Hz + i*50*Hz'
run(100*ms)
