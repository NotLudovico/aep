Unit cell optimization. In this case, the unit cell optimization is combined
with convergence study of BZ grid size and smearing temperature, for the sake
of rigor. However, the convergence conclusions are the same as the ones at
fixed unit cell, since the initial guess was anyway reasonable.

Based on:
- https://docs.abinit.org/tutorial/base4/
N.B. Numerical results slightly different, because LDA XC functionals used in
webpage tutorial, GGA PBE XC functional used here (more accurate).

In general, one should check that the Cartesian forces tend to 0 (are below a
certain threshold) in the optimized structure, although in this tutorial we use
only the total energy as optimization metric. This can be checked in the output
file, or a tolerance can be set in the input with the variable 'tolmxf' (see
https://docs.abinit.org/variables/rlx/#tolmxf), whose default value is
5 x 10^(-5) Ha/Bohr. In this example, a value equal to zero is reached, so we
are well below the default tolerance.
