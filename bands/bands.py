from abipy.abilab import abiopen
import abipy.data as abidata
from abipy.electrons.effmass_analyzer import EffMassAnalyzer

with abiopen("outdata/ebnd_DS2_GSR.nc") as ncfile:
    ebands = ncfile.ebands

print(ebands.fermie)
ebands.plot(with_gaps=True, title="Nb band structure")


# emana = EffMassAnalyzer.from_file("outdata/ebnd_DS2_GSR.nc")
# emana.select_vbm()
# # emana.summarize()
# emana.plot_emass()
