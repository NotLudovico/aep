#!/usr/bin/env bash
conda activate cf.abinit                                                        # only if using Conda environement
INP=scf.abi
mpirun -n 8 abinit $INP 1> ${INP/.abi}.log 2> ${INP/.abi}.err
grep etotal ${INP/.abi}.abo
conda deactivate                                                                # only if using Conda environement
