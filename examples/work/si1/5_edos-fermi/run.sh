#!/usr/bin/env bash
conda activate cf.abinit                                                        # only if using Conda environement
INP=edos-fermi.abi
abinit $INP 1> ${INP/.abi}.log 2> ${INP/.abi}.err
conda activate cf.abipy                                                         # only if using AbiPy in Conda environment
abiopen.py ./outdata/edos-fermi_DS2_GSR.nc --expose -sns=talk
conda deactivate                                                                # only if using Conda environement
xcrysden --bxsf ./outdata/edos-fermi_DS2_BXSF                                   # open Fermi surface file in format readable by XCrysDen
conda deactivate
