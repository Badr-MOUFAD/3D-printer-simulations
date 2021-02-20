# Overview:


As part of an academic mechatronics project, I worked with my team on the realization of a 3D printer.


The 3D printer comes in the form of a **parallel linear delta robot** that has 6 axes:
3 axes for moving a nacelle and 3 axes for moving and tilting the bed.


Our work focused mainly on:
- The conceptual design and 3D modeling of the robot namely the titling bed,
- Simulation of movement, efforts, workspace, and precision
- Control of the robot via Arduino
- The conception of a user interface that eases the control of the robot
- Marketing of the project



# About this repository:


This repository contains all the programs that were developed during the project.
I can classify these programs as follow:

1. Nacelle:
    - Simulation of the workspace (here mechanic constraints were taken into account such as axis length)
    - Simulation of static error
    - Simulation of the impact of design imperfection on the command

2. Tiling bed
    - Simulation of the workspace (here also, the mechanic constraints were considered)
    - Dimensioning of the mechanical joints

3. Algorithm
    - Finding radius of workspace. The algorithm is inspired by binary search.
    - Finding the parameters of a robot given a workspace radius



# Further links:


For further details of the project, [check our website](https://delta-le-grand-website.vercel.app/).
The website was developed as part of the marketing of the project. You have also access to the code via
[this link](https://github.com/Badr-MOUFAD/Delta-LeGrand-website).


If you want to learn about how we managed to make the command of the robot possible even for a usual user,
you can check the code of the UI that was developed for this purpose at [this link](https://github.com/Badr-MOUFAD/Delta-LeGrand-Interface).



> Mecatro 2020: Team Delta Le Grand