import re
import matplotlib.pyplot as plt
import sys


def parse_abinit_eigs(path):
    """
    Parse ABINIT 'Eigenvalues (eV) for nkpt= ...' text into:
      kpts  -> list of (kx, ky, kz) in reduced coords
      bands -> list of lists; bands[i][ik] is energy (eV) of band i at k-point ik
    """
    kpts = []
    eigenvals_per_k = []

    with open(path, "r") as f:
        lines = iter(f.readlines())

    for line in lines:
        if line.lstrip().startswith("kpt#"):
            # extract nband and k-point coords from the header line
            m = re.search(
                r"nband=\s*(\d+).*?kpt=\s*([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)", line
            )
            if not m:
                continue
            nband = int(m.group(1))
            kpt = (float(m.group(2)), float(m.group(3)), float(m.group(4)))
            kpts.append(kpt)

            # collect as many following lines as needed to reach nband floats
            vals = []
            while len(vals) < nband:
                try:
                    nextline = next(lines)
                except StopIteration:
                    break
                # Split on any whitespace and extend with floats
                parts = nextline.split()
                # If we accidentally hit a new 'kpt#' header before finishing, bail out
                if parts and parts[0] == "kpt#":
                    # put the header back (not strictly necessary for well-formed files)
                    raise ValueError(
                        "Unexpected 'kpt#' before collecting all eigenvalues."
                    )
                vals.extend(float(x) for x in parts)

            eigenvals_per_k.append(vals[:nband])

    # transpose to get bands[i][ik]
    if not eigenvals_per_k:
        return [], []
    nband = min(len(row) for row in eigenvals_per_k)
    bands = [[row[i] for row in eigenvals_per_k] for i in range(nband)]
    return kpts, bands


if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else "eigs.txt"
    kpts, bands = parse_abinit_eigs(infile)

    print(f"Parsed {len(kpts)} k-points and {len(bands)} bands.")

    x = range(1, len(kpts) + 1)  # simple x-axis: k-point index
    for b in bands:
        plt.plot(x, b, linewidth=1)
    plt.xlabel("k-point index")
    plt.ylabel("Energy (eV)")
    # Fermi energy 14.594571219345292 should be 5.32 eV...
    plt.ylim(10, 18)
    plt.tight_layout()
    plt.show()
