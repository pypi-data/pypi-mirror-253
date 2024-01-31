
Welcome to QEapp XPS plugin!
===========================================

A plugin for calculating X-ray Photoelectron Spectroscopy (XPS) spectra using the [`XpsWorkChain`](https://github.com/aiidateam/aiida-quantumespresso/blob/main/src/aiida_quantumespresso/workflows/xps.py) of aiida-quantumespresso package.

## Setting Panel
The Setting panel allows users to
- select the peak (element and orbital) to be calculated. The availability of peak in the panel depends on the corresponding pseudopotentials.
- adjust the parameters based on the input structure.

![Screenshot from 2024-01-29 17-10-09](https://github.com/aiidalab/aiidalab-qe/assets/11457659/d92574a1-6213-4aea-b949-a06bb45a7e3e)


## Results Panel
The Result panel displays the final XPS spectrum.
- broadened spectrum using a Voight profile (combined Lorenzian and Gaussian)
- the chemical shift values (differences in total energy relative to the lowest value)
- absolute binding energy

![Screenshot from 2024-01-29 18-02-42](https://github.com/aiidalab/aiidalab-qe/assets/11457659/a8ab265d-08a3-411e-a22c-83ed0840752f)


Pseudopotentials
XPS calculations in QE require core-hole pseudopotentials. We supply a set of pseudopotentials specific to XPS calculations in the [XPS Pseudopotential Repository](https://github.com/superstar54/xps-data). This repository provides the core-hole pseudopotentials as an AiiDA archive file. There are two kind of pseudopotentials available:
- pbe
- pbesol

## WorkChain
To make the setting as simple as possible for user. The following default setting are used.
- `core_hole_treatment`. 
  - `full` for molecule
  - `xch_smear` for metal
  - `xch_fixed` for insulator
- `supercell_min_parameter` updated based on `protocol`.