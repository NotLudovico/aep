#!/usr/bin/env bash
conda activate cf.abinit
INP=0_qptgen.abi # read number of k-points in output abo.
OUT=${INP/.abi}
mpirun -n 8 abinit $INP 1> $OUT.log 2> $OUT.err
INP=1_response.abi # ndtset = number of k-points above (number of q-points here) + 1 (GS calculation)
OUT=${INP/.abi}
mpirun -n 8 abinit $INP 1> $OUT.log 2> $OUT.err
INP=2_mrgddb.abi
OUT=${INP/.abi}
mrgddb < $INP
INP=3_mrggkk.abi
OUT=${INP/.abi}
mrggkk < $INP
INP=4_anaddb.abi
OUT=${INP/.abi}
anaddb $INP 1> $OUT.log 2> $OUT.err
conda deactivate
