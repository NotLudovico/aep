#!/usr/bin/env bash
conda activate cf.abinit
INP=electrons.abi
mpirun -n 8 abinit $INP 1> ${INP/.abi}.log 2> ${INP/.abi}.err
conda deactivate
xcrysden --bxsf outdata/electrons_DS3_BXSF
