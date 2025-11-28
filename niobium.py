import marimo

__generated_with = "0.17.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import abipy.data as abidata
    from abipy.abilab import abiopen

    plt.style.use("default")
    return abiopen, mo, np, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # $E_{cut}$ Convergence
    """)
    return


@app.cell(hide_code=True)
def _(np):
    # ==========================================
    # 1. DATA SETUP
    # ==========================================
    ecut = np.array(range(28, 55, 2))
    etot = np.array(
        [
            -6.2277586160e01,
            -6.2281510125e01,
            -6.2283579949e01,
            -6.2284640583e01,
            -6.2285115894e01,
            -6.2285310194e01,
            -6.2285376420e01,
            -6.2285393073e01,
            -6.2285395596e01,
            -6.2285396364e01,
            -6.2285399052e01,
            -6.2285402845e01,
            -6.2285407042e01,
            -6.2285409984e01,
        ]
    )

    tolerance = 1.0e-5
    return ecut, etot, tolerance


@app.cell(hide_code=True)
def _(ecut, etot, mo, np, plt, tolerance):
    # ==========================================
    # 2. CALCULATIONS
    # ==========================================
    # Calculate differences: |E(n) - E(n-1)|
    diffs = np.abs(np.diff(etot))
    # Corresponding ecut values for the differences (the upper value of the step)
    ecut_steps = ecut[1:]

    # Find first point where difference < tolerance
    passed_indices = np.where(diffs < tolerance)[0]
    if len(passed_indices) > 0:
        converged_ecut = ecut_steps[passed_indices[0]]
    else:
        converged_ecut = ecut_steps[-1]

    # ==========================================
    # 3. PLOTTING
    # ==========================================
    # Create a figure with 2 subplots, sharing the x-axis
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 10), sharex=True)

    # --- Subplot 1: Total Energy ---
    ax1.plot(ecut, etot, "o-", color="tab:blue", label="Total Energy")
    ax1.axvline(
        x=converged_ecut,
        color="red",
        linestyle="--",
        label=f"Converged ({converged_ecut} Ha)",
    )
    ax1.set_ylabel("Total Energy ($E_{tot}$) [Ha]")
    ax1.set_title("Nb Convergence: Total Energy & Successive Differences")
    ax1.grid(True, linestyle=":", alpha=0.6)
    ax1.legend()

    # --- Subplot 2: Successive Differences (Log Scale) ---
    ax2.semilogy(
        ecut_steps,
        diffs,
        "o-",
        color="tab:blue",
        label="Successive Energy Difference",
    )
    ax2.axhline(
        y=tolerance,
        color="red",
        linestyle="--",
        label=f"Tolerance ($10^{{-5}}$ Ha)",
    )
    ax2.axvline(x=converged_ecut, color="red", linestyle="--")  # Consistency line
    ax2.set_xlabel("Cutoff Energy ($E_{cut}$) [Ha]")
    ax2.set_ylabel("$\Delta E$ [Ha]")
    ax2.grid(True, which="both", ls=":", alpha=0.6)
    ax2.legend()

    plt.tight_layout()

    plt.savefig("images/convergence_plot.png", dpi=300, bbox_inches="tight")

    mo.center(plt.gca())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # $t_{smear}$ and $ngkpt$ Convergence
    """)
    return


@app.cell(hide_code=True)
def _(pd):
    ngkpt_tsmear = pd.DataFrame(
        data={
            "tsmear": [
                0.001,
                0.002,
                0.003,
                0.004,
                0.005,
                0.006,
                0.007,
                0.008,
                0.009,
            ],
            "8x8x8": [
                -6.2284869142e01,
                -6.2284871193e01,
                -6.2284876848e01,
                -6.2284889393e01,
                -6.2284893498e01,
                -6.2284880454e01,
                -6.2284858683e01,
                -6.2284839641e01,
                -6.2284829472e01,
            ],
            "10x10x10": [
                -6.2285539305e01,
                -6.2285546612e01,
                -6.2285548290e01,
                -6.2285541520e01,
                -6.2285535620e01,
                -6.2285533906e01,
                -6.2285535933e01,
                -6.2285540830e01,
                -6.2285548253e01,
            ],
            "12x12x12": [
                -6.2285558268e01,
                -6.2285638521e01,
                -6.2285728238e01,
                -6.2285780109e01,
                -6.2285756055e01,
                -6.2285659014e01,
                -6.2285514651e01,
                -6.2285343820e01,
                -6.2285155925e01,
            ],
            "14x14x14": [
                -6.2286107148e01,
                -6.2286117506e01,
                -6.2286131617e01,
                -6.2286139930e01,
                -6.2286133895e01,
                -6.2286112872e01,
                -6.2286082697e01,
                -6.2286049123e01,
                -6.2286015724e01,
            ],
            "16x16x16": [
                -6.2285898400e01,
                -6.2285898168e01,
                -6.2285897083e01,
                -6.2285895584e01,
                -6.2285890862e01,
                -6.2285882753e01,
                -6.2285873620e01,
                -6.2285865220e01,
                -6.2285858133e01,
            ],
        }
    )

    ngkpt_tsmear
    return (ngkpt_tsmear,)


@app.cell(hide_code=True)
def _(mo, ngkpt_tsmear, plt):
    cols = ["8x8x8", "10x10x10", "12x12x12", "14x14x14", "16x16x16"]
    global_min = ngkpt_tsmear[cols].min().min()

    plt.figure(figsize=(10, 6))
    for col in cols:
        plt.plot(
            ngkpt_tsmear["tsmear"],
            ngkpt_tsmear[col],
            marker="o",
            linewidth=2,
            label=col,
        )

    plt.title("Nb Convergence: Smearing vs k-points")
    plt.xlabel("Smearing Temperature ($t_{smear}$) [Ha]")
    plt.ylabel("$E_{tot} [Ha]$")
    plt.grid(True, linestyle="--", alpha=0.6)

    plt.legend()

    plt.savefig("images/tsmear-ngkpt.png", dpi=300, bbox_inches="tight")

    mo.center(plt.gca())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Electronic Density of States
    """)
    return


@app.cell(hide_code=True)
def _(abiopen, mo, np, plt):
    with abiopen("edos/outdata/nb_dos_DS2_GSR.nc") as gs_wfk:
        gs_ebands = gs_wfk.ebands

    edos = gs_ebands.get_edos(method="gaussian", step=0.01, width=0.1)
    edos_fig = edos.plot_dos_idos(
        title="DOS and Integrated DOS", xlims=(-6, 10), show=False
    )

    ax_idos, ax_dos = edos_fig.get_axes()[:2]
    ax_dos.set_ylim(0, 3)
    ax_idos.set_ylim(7, 22)


    energy, idos = ax_idos.lines[0].get_data()
    _, dos = ax_dos.lines[0].get_data()
    fermi_energy_idx = np.where(energy == min(energy, key=abs))[0][0]
    print("IDOS at Fermy Energy: ", idos[fermi_energy_idx])
    print("DOS at Fermy Energy: ", dos[fermi_energy_idx])


    plt.savefig("images/edos.png", dpi=300, bbox_inches="tight")
    mo.center(plt.gca())
    return energy, idos


@app.cell(hide_code=True)
def _(energy, idos):
    # define your energy range
    e_min = -6  # Lower bound in eV
    e_max = 0  # Upper bound in eV

    # create a boolean mask for indices where energy is within [e_min, e_max]
    mask = (energy >= e_min) & (energy <= e_max)

    # apply the mask to slice the arrays
    energy_subset = energy[mask]
    idos_subset = idos[mask]

    print(f"--- Data in range [{e_min}, {e_max}] eV ---")
    print(f"Start IDOS ({energy_subset[0]:.2f} eV): {idos_subset[0]:.4f}")
    print(f"End IDOS   ({energy_subset[-1]:.2f} eV): {idos_subset[-1]:.4f}")

    states_in_window = idos_subset[-1] - idos_subset[0]
    print(f"Total states integrated within window: {states_in_window:.4f}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Phonons
    """)
    return


@app.cell(hide_code=True)
def _(abiopen, mo, plt):
    with abiopen("phonons/outdata/3_anaddb/anaddb_PHBST.nc") as nc_bands:
        ph_bands = nc_bands.phbands

    with abiopen("phonons/outdata/3_anaddb/anaddb_PHDOS.nc") as nc_dos:
        ph_dos = nc_dos.phdos

    ph_fig = ph_bands.plot_with_phdos(
        ph_dos, units="cm-1", title="Phonon Bands + DOS", show=False
    )

    plt.savefig("images/ph_bands_dos.png", dpi=300, bbox_inches="tight")

    mo.center(ph_fig)
    return


if __name__ == "__main__":
    app.run()
