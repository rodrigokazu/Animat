clear all
close all

%-----------------------------------------------------------------------%
% Written by Dr Rodrigo Siqueira @ AMRC, University of Sheffield %
%-----------------------------------------------------------------------%
% Creating an input spike train that connects to a neuron via a synapse %
%-----------------------------------------------------------------------%

i = csim('create', 'SpikingInputNeuron');
s = csim('create', 'DynamicSpikingSynapse');
n = csim('create', 'LifNeuron');

%-----------------------------------------------------------------------%
% Setting specific parameters %
%-----------------------------------------------------------------------%

csim('set','randSeed',123456);

%Change the absolute refractory period of the LIF neuron n to be of length
%2 ms and add a noisy current of 50 nA. 

csim('set',n,'Trefract',0.002,'Inoise',50e-9,'Vthresh', -0.055);

% For the dynamic synapse, parameters for depressing behaviour:

csim('set',s,'W',10,'U',0.1,'D',1,'F',0.05, 'u0',0.1,'r0',1);

%csim('set',s,'W',2000e-9); % Synaptic weight from the CSIM tutorial

%-----------------------------------------------------------------------%
% Connecting the elements %
%-----------------------------------------------------------------------%

csim('connect', n, s); 
csim('connect', s, i); 

%-----------------------------------------------------------------------%
% Recording specific data %
%-----------------------------------------------------------------------%

r = csim('create', 'Recorder');

% The timestep at which an recording should be done is the dt

csim('set',r,'dt',0.5e-3); % Setting recorder parameters


csim('connect', r, s, 'psr'); % Recording the post-synaptic response 
csim('connect', r, n, 'Vm'); % Recording the membrane potential
csim('connect', r, n, 'spikes'); % Recording the Spikes 

%-----------------------------------------------------------------------%
% Defining the input %
%-----------------------------------------------------------------------%

S.spiking = 1; % 1 for spike times, 0 for analog
S.dt = -1; % Resolution for analog data (-1 as per the example)
S.idx = i; % Index of the receiving object

S.data = [0.0046    0.0844    0.1067    0.2599    0.3998    0.7749  ... 
    0.8001    0.8173 0.8687    0.9619]; % 10 random spikes 

%-----------------------------------------------------------------------%
% Running the simulation %
%-----------------------------------------------------------------------%

Tsim = 1; % 1 second

csim('simulate', Tsim, S);

%-----------------------------------------------------------------------%
% Visualising the output of the simulation %
%-----------------------------------------------------------------------%

t = csim('get', r, 'traces');

figure(1); clf reset;
subplot(3,1,1);

st=S.data;
line([st; st],[-0.045; -0.015]*ones(size(st)),'Color','k');
set(gca,'Xlim',[0 Tsim]);
title('Input spike train');
axis off % Just to make it look like a raster

subplot(3,1,2);
plot(t.channel(1).dt:t.channel(1).dt:Tsim,t.channel(1).data);
ylabel([t.channel(1).fieldName ' [A]']);
title('Postsynaptic Response');

subplot(3,1,3);

st=t.channel(3).data;
line([st; st],[-0.045; -0.015]*ones(size(st)),'Color','k'); %Spikes

mV = t.channel(2).data*1000 %Converting to mV
plot(t.channel(2).dt:t.channel(2).dt:Tsim,mV)


ylabel([t.channel(2).fieldName ' [mV]']);
xlabel('Time [s]');
title('Membrane Potential and Spikes');

drawnow;