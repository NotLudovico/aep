Phonon properties.

Adapted to silicon and aluminum from:
- https://docs.abinit.org/tutorial/rf1/
- https://docs.abinit.org/tutorial/rf2/
- https://docs.abinit.org/guide/mrgddb/
- https://docs.abinit.org/variables/anaddb/
- https://docs.abinit.org/tests/v7/Input/t94.abi
- https://docs.abinit.org/guide/respfn/#0-introducing-the-computation-of-responses

IMPORTANT!
Check that the Cartesian forces on atoms vanish, so that you are at equilibrium
position! You will get complex phonon frequencies otherwise!

Basically divided in the following steps:
1) Calculative response functions, i.e. derivates (first or second, depending on
   the perturbation) of the total energy w.r.t. to the following perturbations:
   - phonons
   - electric field - importantant only for polar materials; response to d/dk
     perturbation must be calculated before since it is an auxiliary variable.
     Not done here since dealing with monoatomic materials.
   A Derivative DataBase (DDB) will be generated for each q-vector.
2) Merge the DDBs into a single one with MRGDDB.
3) Analyze merged DDB with ANADDB to study IFCs and phonon band structure.
   Important! It is a good idea to do calculation on a coarse grid, then
   do Fourier interpolation to a finer grid.

MRGDDB is an interactive terminal commands, but you can still use an
"input" file by knowing the order of the prompts and using a "<" between
command and "input" file. Basically, each line of this "input" file is EXACTLY
what you would type in the prompt (no comments allowed, see commented files
in "Commented" directory) in the SAME order. Also the comments for 'band2eps'
(plotting phonons) must be checked in the Commented directory.

The file PHBST_partial_DOS contains the phonon density of states.

Some theory can be found at:
https://www.vasp.at/wiki/index.php/Phonons:_Theory

Compare band structure with:
https://www.researchgate.net/publication/252286619_Phonon_spectrum_and_specific_heat_of_silicon_nanowires
