# This work is licensed under a MIT License. The copyright notice must be included in all copies or portions of the Software or data.
## Citation
```
@incollection{Alshehri2021227,
title = {Next Generation Pure Component Property Estimation Methods: With and Without Machine Learning},
editor = {M.  Turkay and R. Gani},
author = {Abdulelah S. Alshehri, Anjan K. Tula, Lei Zhang, Rafiqul Gani, Fengqi You},
Publisher= {Elsevier},
booktitle= {31 European Symposium on Computer Aided Process Engineering},
volume = {50},
pages = {227-233},
doi = {http://dx.doi.org/10.1016/B978-0-323-88506-5.50037-1},
abstract = {Physicochemical property estimation methods serve as the basis for the design of molecules that enhance the functionality and efficiency of products and processes. The need to provide reliable pure component properties through quantum chemistry computations and/or experimental measurements is a major bottleneck to the goal of faster and cheaper to market the desired products. Hence, the development of approximate but accurate models is vital to progress in the field of Computer-Aided Molecular Design (CAMD), among others. With group contribution (GC) as a dominant molecular representation, semi-empirical methods have been the most popular class in generating approximate property models for CAMD owing to their low computational cost and direct incorporation into optimization models. Recent advances in machine learning have stimulated widespread interest and progress towards closing the gap between semi-empirical and quantum chemistry methods. Herein, we use machine learning and data analysis methods to address the shortcomings of the current GC-based models by synthesizing the next-generation models and tools for the fast and accurate estimation of 20 physicochemical properties central to CAMD.},
year = {2021}
}
```
# Pure-Component-Property-Estimation
This repo contains models and results for Next Generation Pure Component Property Estimation Methods: With and Without Machine Learning [Link](), AIChE Journal

The figure shows the overall performance of all models with the fraction of the dataset predicted under different error threshold rates (1%, 5%, 10%) as a measure of the performance.

<p align="center">
<img src="https://github.com/PEESEgroup/Pure-Component-Property-Estimation/blob/main/MAT1.jpg" width="900" >
</p>


## Overview
* `1 Dataset/` contains data and ML-results
* `2 Full Excel Sheet/` contains full results of GC-Simple and GC-ML models and full dataset
* `3 Paramters and GC models` contains models for GC-ML and parameters of the GC-Simple models
* `4 Tools Illustration` contains an illustration on how to use the GC-ML models
* `5 Correlations` contains the models and the results of the correlations
## Properties
* Octanol-Water Partition Coefficient (LogP)
* Toxicity (Oral Rat) (LD50) [mol/kg]
* Aqueous Solubility (LogWs) [mol/L]
* Auto Ignition Temperature (AiT) [K]
* Normal Melting Point (Tm) [K]
* Normal Boiling Point (Tb) [K]
* Acentric factor (ω)
* Acid Dissociation Constant (pKa)
* Hildebrandt Solubility Parameter at 298 K (HSolP) [MPa1/2]
* Standard Enthalpy Of Formation (Hf) [kJ/mol]
* Liquid Molar Volume at 298K (Lmv) [cc/mol]
* Hansen solubility parameter - Dispersion δD [MPa1/2]
* Hansen solubility parameter – H2 δH [MPa1/2]
* Hansen solubility parameter – Polar  δP [MPa1/2]
* Critical Temperature (Tc) [K]
* Critical Pressure (Pc) [bar]
* Critical Volume (Vc) [cc/mol]
* Standard Gibbs Energy Of Formation (Gf) [kJ/mol]
* Normal Enthalpy Of Fusion (Hfus) [kJ/mol]
* Fathead Minnow 96-H LC50 (LC50(FM)) [mol/L]
* Photochemical Oxidation Potential (PCO)
* Bioconcentration Factor (BCF)
* Flash Point (Fp) [K]
* Enthalpy Of Vaporization At 298K (Hv) [kJ/mol]
* Permissible Exposure Limit (OSHA-TWA) [mol/m3]

## IPYNB Requirements
* Python >= 3.0
* Numpy
* Pickle 

