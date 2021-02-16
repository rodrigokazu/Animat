# RATOCA platform developed at the Reading Uni by Dr Rodrigo Siqueira # 


The aim of the system is to provide a complete integration between a Multi Electrode Array (MEA) with neuronal cells and a mobile robot. The biological signals of the cells will be acquired by a software named MC_Rack, from the MultiChannel Systems. When MC_Rack detects specific signal patterns on the electrodes, it creates a .mcd file that contains, among other types of data, a digital bit associated with the channel (electrode) that reached a predefined voltage threshold. A MATLAB script was developed in order to read every .mcd file that is created, and evaluate, for each of them, which channel was triggered. When the script acquires this information, it creates a .txt file, that contains the digital bit, the channel ID, and the number of the .mcd file that was read.

After the generation of the *.txt files with the information of the channels, the Alpha software is the next step of the closed-loop pipeline. Alpha detects the .txt files, read their content and transmit the channel information to Beta via TCP/IP socket. Alpha always must be in the same computer that the MC_Rack is, since they communicate with each other via files. The TCP/IP socket communication between Alpha and Beta was chosen since it provides a reliable way to transmit and receive data wireless, with no loss in a reasonable time spam.

Beta receives the information from Alpha and, based on a given decoding algorithm, it computes the wheel speeds of the mobile robot. Beta was built to command a real mobile robot and a simulation robot as well. The simulation platform used is V-REP, which has the 3D model of the robot. Currently, only the simulated robot is used. The communication between the Beta and the real mobile robot will be implemented. It is important to mention that Beta should be in a computer near the real robot to avoid communication delays, since the communication between the laptop and the robot is often via Bluetooth.

When the robot reaches the vicinity of an obstacle, the distance sensors detect the obstacle and trigger an event in Beta. When Beta receives the information that an obstacle has been detected, it sends this message to Alpha via TCP/IP. Alpha, when receives this information, should stimulate the neuronal cells by using another software, MC_Stimulus, that is responsible for stimulate the MEA. The stimulation part in Alpha is will be implemented. The above description is the completed closed-loop of the system. Figure 1 illustrates this process.
