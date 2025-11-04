#!/usr/bin/env bash
conda activate cf.abinit
INP=0_qptgen.abi
OUT=${INP/.abi}
mpirun -n 8 abinit $INP 1> $OUT.log 2> $OUT.err
INP=1_response.abi
OUT=${INP/.abi}
mpirun -n 12 abinit $INP 1> $OUT.log 2> $OUT.err
INP=2_mrgddb.abi
OUT=${INP/.abi}
mrgddb < $INP
INP=3_anaddb.abi
OUT=${INP/.abi}
anaddb $INP 1> $OUT.log
conda deactivate
