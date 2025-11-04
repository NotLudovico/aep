Calculation of BCC Wolfram (W) electronic structure, density-of-states, and
Fermi surface, with spin-orbit coupling.

This tutorial is also useful to combine several calculations into a single input
file (see *.abi).

Based on:
- https://docs.abinit.org/tutorial/base3/
- https://docs.abinit.org/tutorial/base4/
- https://docs.abinit.org/topics/ElecDOS/
- https://docs.abinit.org/tutorial/spin/
- https://abinit.github.io/abipy/gallery/plot_ebands_edos.html
- http://www.xcrysden.org/doc/fermi.html

The KS eigenvalues can be found in the 'ebnd.abo' file, in the section about
the second dataset, under "Eigenvalues (   eV  ) for nkpt=  ${nkpt}  k points:".
Here, the data is presented as pairs of lines, with the first line reporting
the k-point in normalized units, and the second line the eigenvalues in eV
(N.B. The number of eigenvalues for each k-points corresponds to 'nband').

In principle, you can just take this values and use Excel or MATLAB/Python to
plot the band structure. You can make your life a bit easier with AbiPy
(https://abinit.github.io/abipy/gallery/plot_ebands.html).

From the Jupyter notebook, you can control the Gaussian "smearing", which is
quite large in the plots generated from the terminal. The electronic states are
stored in a BXSF file readable by XCrysDen to plot the Fermi surface.

Since the purpose is to simply show the effect of spin-orbit coupling on the
electronic structure of crystals containing heavy elements, in particular how
the input file should be modified to includ spin-orbit effects, no convergence
study, nor relaxation, is performed in this tutorial. Clearly, these aspects
should be considered in serious studies and in the students homework.

The crystal structure of Tungsten is BCC. The lattice constant has been taken
from:
https://materialsproject.org/materials/mp-91?chemsys=W

Ecut has been set to the value of 37 Ha recommended at
http://www.pseudo-dojo.org/.

The results can be compared with the electronic structure reported at
https://materialsproject.org/materials/mp-91?chemsys=W

The results on Fermi surface can be compared with
https://www.researchgate.net/publication/235925995_Electronic_Structure_and_Compton_Profiles_of_Tungsten
