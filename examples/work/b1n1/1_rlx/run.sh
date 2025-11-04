#!/usr/bin/env bash
conda activate cf.abinit                                                        # only if using Conda environement
INP=rlx.abi
abinit $INP 1> ${INP/.abi}.log 2> ${INP/.abi}.err
grep etotal ${INP/.abi}.abo                                                     # get etotal during relaxation
grep "Scale of Primitive Cell (acell)" ${INP/.abi}.abo -A 1                     # get lattice vector scaling [Bohr] during relaxation
grep "acell" ${INP/.abi}.abo                                                    # get equilibrium lattice scaling vector [Bohr]
conda deactivate                                                                # only if using Conda environement
