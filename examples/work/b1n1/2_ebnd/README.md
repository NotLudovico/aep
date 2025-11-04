Electronic structure.

Based on:
- https://docs.abinit.org/tutorial/base3/

The KS eigenvalues can be found in the 'ebnd.abo' file, in the section about
the second dataset, under "Eigenvalues (   eV  ) for nkpt=  39  k points:".
Here, the data is presented as pairs of lines, with the first line reporting
the k-point in normalized units, and the second line the eigenvalues in eV
(N.B. Since we chose 'nband 8', there are 8 eigenvalues for each k point).

In principle, you can just take this values and use Excel or MATLAB/Python to
plot the band structure. You can make your life a bit easier with AbiPy
(https://abinit.github.io/abipy/gallery/plot_ebands.html).
