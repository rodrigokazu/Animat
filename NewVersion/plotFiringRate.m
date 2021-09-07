%% University of Reading
%  School of System Engineering
%  Brain Embodiment Laboratory
%  Johnathan Mayke Melo Neto
%  March/2015
%  Script that receives a mat-file and plot the firing rate due to the Left
%  and Right channels

% Initial configuration
clear all;
close all;
clc;

a = load('C:\Users\joseli\Documents\Visual Studio 2008\Projects\alpha\Debug\firing_rates.txt');

leftFiringRate = a(:,1);
rightFiringRate = a(:,2);
stimuliLeft = a(:,3);
stimuliRight = a(:,4);
    
subplot(4,1,1);
plot(leftFiringRate,'-b');
title('Firing Rate - Left Channel');
ylabel('Firing Rate');
   
subplot(4,1,2);
plot(rightFiringRate,'-r');
title('Firing Rate - Right Channel');
ylabel('Firing Rate');

subplot(4,1,3);
plot(stimuliLeft,'-g');
title('Obstacle Detection - Left Sensor');

subplot(4,1,4);
plot(stimuliRight,'-k');
title('Obstacle Detection - Right Sensor');
xlabel('Seconds');
 




