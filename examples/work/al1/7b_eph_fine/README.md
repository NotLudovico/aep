Electron-phonon coupling.

Based on:
- https://docs.abinit.org/tutorial/eph_legacy/
and not:
- https://docs.abinit.org/tutorial/eph_intro/
since the second one is very new and does not supporto things such as SOC.

Meaning of ANADDB VARIABLES
https://docs.abinit.org/variables/anaddb/

The procedure is similar to phonon properties:
1) Calculative response functions, i.e. derivates (first or second, depending on
   the perturbation) of the total energy w.r.t. to the following perturbations:
   - phonons
   - electric field - importantant only for polar materials; response to d/dk
     perturbation must be calculated before since it is an auxiliary variable;
     not done here since dealing with monoatomic materials.
   and calculate the gkk matrix elements.
   A Derivative DataBase (DDB) will be generated for each q-vector and a GKK
   database will be generated for each (q-vector, perturbation) pair.
2) Merge the DDBs into a single one with MRGDDB.
3) Merge GKK into a single file with MRGGKK.
4) Analyze merged data with ANADDB to study electron-phonon properties.

You can find superconductivity parameters at the end of the ANADDB output file,
("4-anaddb.abo" inside this folder) under the section "Superconductivity :
isotropic evaluation of parameters from electron-phonon coupling.", which
contains:
- lambda
- omegalog
- the mustar valuer provided by the user in the input file
- the MacMillan crytical temperature

The Eliashberg function is contained in the ANADDB output data file eneding with
"_A2F", which is "4-anaddb/anaddb_ep_A2F" in this folder.
