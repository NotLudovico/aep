from abipy.abilab import abiopen
import abipy.data as abidata

with abiopen("outdata/ebnd_DS2_GSR.nc") as ncfile:
    ebands = ncfile.ebands

ebands.plot(with_gaps=True, title="Nb band structure")
