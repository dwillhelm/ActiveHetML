# ActiveHetML
Active Learning for van der Waals Heterostructures  
D.Willhelm (2022)

For a demonstration, please refer to the [example notebooks](https://github.com/dwillhelm/ActiveHetML/tree/main/notebooks). 


https://user-images.githubusercontent.com/45088478/173843665-8f23053a-03fe-4851-9745-27250e17d79b.mp4



## Problem Statement  

These notebooks demonstrate a sequential learning (a.k.a active learning) process to a real-world material design problem. In the demonstration, I will use a custom material dataset of van der Waal heterostructure bilayers that I created during my [Ph.D. work](https://github.com/dwillhelm/HetML). The dataset was used to train a data-driven surrogate model for DFT and is capable of accurately predicting several important properties of vdW heterostructures - such as the band gap energy (Eg), ionization energy (IE), electron affinity (EA), interlayer binding energy (Eb) and interlayer distance (d0). The model made predictions on nearly 3,000 unique bilayers. For the purpose of this demo, I will use the features and predicted properties as a toy dataset (the original dataset contains ~800 DFT labeled materials). 

2D vdW heterostructures are an emerging family of materials made by vertically stacking different 2D monolayers. When stacked, these materials display emergent properties unique to that of the component monolayers. This means that the properties of the bilayer can be tuned by careful selection of the constituent monolayers (i.e. stacking order) as well as other factors such as interlayer distance or interlayer twist-angle. These materials have a wide range of potential applications in next-generation electronic and optoelectronics. For many applications, the position of the electronic band edges is important. For example, one may wish to align the band edges with another material to tune the properties via doping or wish to find materials with suitable band edges for photocatalytic water splitting reactions. 

However, as we continue to discover new 2D monolayers, the heterostructure material space will grow combinatorically. For example, with only 50 starting monolayers, a total of 1,225 unique bilayers are possible. The large material design space for vdW heterostructures is too large for conventional experimental approaches. For this reason, a data-driven approach is crucial to efficiently explore this materials space. 

Here, I will demonstrate how active learning can be used to design a vdW bilayer with an optimal band edge of your choosing. First I will perform an initial analysis of the dataset and test some machine learning models to predict the IE ([Notebook 1](https://github.com/dwillhelm/ActiveHetML/blob/main/notebooks/01-data_exploration.ipynb)). Afterward, I will use active learning to build new machine learning models starting with only 10 initial samples ([Notebook 2](https://github.com/dwillhelm/ActiveHetML/blob/main/notebooks/02-active_learning_for_DFT_surrogate.ipynb)). Then, I will demonstrate how to use active learning to optimize the IE for a given target value ([Notebook 3](https://github.com/dwillhelm/ActiveHetML/blob/main/notebooks/03-active_learning_property_optimization.ipynb)). 


## A Brief Material Background

Here I will focus on one property - the ionization energy (IE). The IE is defined by the energy of the valence band maxima with respect to the vacuum level energy. Here, the IE is used with units in electron volts (eV). 

$IE = E_{vac} - E_{VBM}$

Hwere $E_{vac}$ is the vacuum energy and $E_{VBM}$ is the valence band edge energy The diagram below shows how the IE is defined graphically.

![alt text](https://github.com/dwillhelm/ActiveHetML/blob/main/docs/figs/band_alignment_diagram.svg?raw=true)


## Repo Setup  



