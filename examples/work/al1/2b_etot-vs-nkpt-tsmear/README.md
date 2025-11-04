Groud state energy of crystalline aluminum vs size of the BZ grid and Marzari
smearing temperature.
N.B. Energy values are in Ha.
I assume that convergence is achieved with respect to the energy cut-off when
the total energy change obtainted by increasing the cut-off energy is below
0.001 Ha.

Experience teaches us that convergence w.r.t. cut-off energy and size of the BZ
grid can be trated separately.
The same is not true for the Marzari smearing temperature, which has a strong
cross-convergence effect with the number of k points.
Therefore, one has to consider different sizes of the BZ grid and different
smearing temperatures, and study convergece w.r.t. to their combinations
(basically Cartesian product).

N.B. Variational theorem applies to 'ecut' (basis set size), but there is no
variational theorem for k point grid and smearing temperature! Increasing these
might also slightly increase 'etotal'. What matters in this case is the size
of the change of 'etotal'.

Based on:
- https://docs.abinit.org/tutorial/base4/

