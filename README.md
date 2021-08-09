<img src="https://drive.google.com/uc?export=view&id=1QspeLL4wVjzzIGHuyYVMfy2-77yHECNT" width = "350" height="150">

# Nuclear-Magnetic-Resonance-Analysis

This analysis aims to model and demonstrate the properties of Nuclear Magnetic Resonance (NMR). The first question is to analyse numerically the dependence of the magnetic field produced by a magnetic dipole of a proton as a function of distance and angle to the dipole orientation. By considering the points lying in the dipole plane only, constant magnetic field lines and radial dependence on vector components can be plotted. Question two solves the simultaneous first-order differential equations, which describe the magnetisation of a system known as the Bloch equations for carbon-13 nuclei. By considering a large static magnetic field aligned along the z-axis and an alternating field in the x-axis, the magnetisation in the rotating frame can be calculated.

## Prerequisites

Python modules utilised in this analysis:

- numpy
- os
- matplotlib
- unittest

To install any missing modules excecute

```bash
python3 -m pip install missing-moduule-name
```

or

```bash
pip3 install missing-module-name
```

## Download

To download this analysis just clone this repository and then move to that directory to excecute.

```bash
git clone https://github.com/JamArm99/Nuclear-Magnetic-Resonance-Analysis.git
cd Nuclear-Magnetic-Resonance-Analysis
```

## Excecute

### NMR.py

This script conducts the primary analysis. By utilising the functions defined in **_func_NMR.py_**, both questions are calculated. Question one is achieved by using NumPy's linspace function to produced either radial or angular data between defined points. Question two centres around the **_Mag_** function that features a while loop to iterate the time parameter in the differential equations.

```bash
python3 NMR.py
```

### test_NMR.py

This script is designed to run tests on the functions defined in **_func_NMR.py_**. Using unittest, these functions can be tested to ensure the desired result when called upon in the main script.

```bash
python3 -m unittest test_NMR.py
```

or

```bash
python3 test_NMR.py
```

## Outputs

Two folders are either created or overwritten when the primary analysis is executed. Question one plots are saved in the **_images_NMR_Q1_** directory, whilst question two plots are saved in the **_images_NMR_Q2_**.
