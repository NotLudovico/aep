#!/usr/bin/env bash
conda activate cf.abinit                                                        # only if using Conda environement
INP=ebnd.abi
abinit $INP 1> ${INP/.abi}.log 2> ${INP/.abi}.err
conda activate cf.abipy                                                         # only if using AbiPy in Conda environment
abiopen.py ./outdata/ebnd_DS2_GSR.nc --expose -sns=talk
conda deactivate
conda deactivate                                                                # only if using Conda environement

# ABOUT ABIPY
# See https://docs.abinit.org/tutorial/base3/ and https://abinit.github.io/abipy/gallery/plot_ebands.html
# If you use 'abiopen.py' from terminal, AbiPy will generate a set of standard plots for the kind of data contained in the target file.
# Alternatively, you can work form within a Jupyter Notebook (see link above).
# Run `abiopen.py --help` for info on how to use the terminal command, or read the documentation online for the Jupyter Notebook approach
