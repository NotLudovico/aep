Self-consistent-field (SCF) calculation of the ground-state energy of
crystalline silicon at fixed plane-wave basis-set cut-off energy and size of the
BZ grid (Monkhorst-Pack grid).

N.B. Energy values are in Ha.

Based on:
- https://docs.abinit.org/tutorial/base3/
N.B. Numerical results slightly different, because LDA XC functionals used in
webpage tutorial, GGA PBE XC functional used here (more accurate).

Reasonable guess for cut-off value given at:
  http://www.pseudo-dojo.org/
if the pseudo-potentials therein are used.

'scf.abi' is the input file. To run the simulation, execute in a terminal:
> INP=scf.abi
> abinit $INP 1> ${INP/.abi}.log 2> ${INP/.abi}.err

'abinit' execute commands according to the instructions in 'scf.abi'.
The main output file will be 'scf.abo'.
'1> scf.log' tells the program to save log info in 'scf.log'.
'2> scf.err' tells the program to save eventual error info in 'scf.err'.

There will be several additional output files, containing the simulation
output data.

'run.sh' contains the sequence of commands used.

Notice that by running 'grep etotal scf.abi', one gets 'etotal' value.

