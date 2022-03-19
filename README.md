# Pure-Component-Property-Estimation
## Notice: This work is licensed under a MIT License. The copyright notice must be included in all copies or portions of the Software or data.
## Citation
```
@article{https://doi.org/10.1002/aic.17469,
author = {Alshehri, Abdulelah S. and Tula, Anjan K. and You, Fengqi and Gani, Rafiqul},
title = {Next generation pure component property estimation models: With and without machine learning techniques},
journal = {AIChE Journal},
volume = {n/a},
number = {n/a},
pages = {e17469},
keywords = {data analysis, group-contribution, machine learning, pure component property prediction},
doi = {https://doi.org/10.1002/aic.17469},
url = {https://aiche.onlinelibrary.wiley.com/doi/abs/10.1002/aic.17469},
eprint = {https://aiche.onlinelibrary.wiley.com/doi/pdf/10.1002/aic.17469},
abstract = {Abstract Physiochemical properties of pure components serve as the basis for the design and simulation of chemical products and processes. Models based on the molecular structural information of chemicals for the following 25 pure component properties are presented in this work: (critical-) temperature, pressure, volume, acentric factor; (normal-) boiling point, melting point, auto-ignition temperature; flash point; (standard-) enthalpy of formation, Gibbs energy of formation, enthalpy of fusion, enthalpy of vaporization, liquid molar volume; (environmental-) (lethal dose-) LC50 and LD50, photo-chemical oxidation potential, bioconcentration factor, permissible exposure limit; (physicochemical-) acid dissociation constant, water-solubility, octanol–water partition coefficient, Hildebrandt solubility parameter, Hansen solubility parameters. Utilizing functional groups for molecular representation, two parallel property estimation models where the group contributions for each property are regressed through traditional regression techniques and machine learning techniques are presented. Both techniques use an a priori data analysis before regression of model parameters. A dataset with more than 24,000 chemicals for the 25 pure component properties has been utilized for the development of the two sets of property models. The efficacy of the developed models and their use are highlighted together with a discussion on the overall performance, application range, and predictive capabilities with implications to product and/or process engineering problem solutions.}
}

```
# About
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

