import abipy.data as abidata
from abipy.abilab import abiopen

# Open the wavefunction file computed with a homogeneous sampling of the BZ
# and extract the band structure on the k-mesh.
with abiopen("./outdata/edos-fermi_DS2_GSR.nc") as gs_wfk:
    gs_ebands = gs_wfk.ebands

edos = gs_ebands.get_edos(method="gaussian", step=0.01, width=0.1)
edos.plot_dos_idos(title="DOS and Integrated DOS")
