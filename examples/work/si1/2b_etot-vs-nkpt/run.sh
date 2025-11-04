#!/usr/bin/env bash
conda activate cf.abinit
INP=etot-vs-nkpt.abi
abinit $INP 1> ${INP/.abi}.log 2> ${INP/.abi}.err
grep etotal ${INP/.abi}.abo
conda deactivate
