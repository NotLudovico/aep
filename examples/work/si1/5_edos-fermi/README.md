Electronic density-of-states. Fermi surface makes sense only if you DOPE the
material, which is considered here for large doping values, to make the impact
on the Fermi surface very visible.

Based on:
- https://docs.abinit.org/tutorial/base3/
- https://docs.abinit.org/topics/ElecDOS/
- https://docs.abinit.org/tutorial/spin/
- https://abinit.github.io/abipy/gallery/plot_ebands_edos.html

The DOS is saved in the file 'outdata/edos_DS2_DOS'. You can take these values and
use Excel or MATLAB/Python to plot the band structure. You can make your life a bit easier with AbiPy
(https://abinit.github.io/abipy/gallery/plot_edos.html). From the Jupyter
notebook, you can control the Gaussian "smearing", which is quite large in the
plots generated from the terminal. The electronic states are stored in a BXSF
file readable by XCrysDen to plot the Fermi surface.
