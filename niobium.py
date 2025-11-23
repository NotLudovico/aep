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
            "tsmear": [0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05],
            "8x8x8": [
                -6.2284830096e01,
                -6.2284963624e01,
                -6.2285186934e01,
                -6.2285370002e01,
                -6.2285455302e01,
                -6.2285445372e01,
                -6.2285370038e01,
                -6.2285254528e01,
                -6.2285111286e01,
            ],
            "10x10x10": [
                -6.2286442971e01,
                -6.2286260635e01,
                -6.2286165833e01,
                -6.2286093679e01,
                -6.2285977804e01,
                -6.2285809116e01,
                -6.2285608912e01,
                -6.2285396520e01,
                -6.2285180839e01,
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
                -6.2285984637e01,
                -6.2285889675e01,
                -6.2285880363e01,
                -6.2285881235e01,
                -6.2285827066e01,
                -6.2285706424e01,
                -6.2285542831e01,
                -6.2285358278e01,
                -6.2285162884e01,
            ],
            "16x16x16": [
                -6.2285852410e01,
                -6.2285843679e01,
                -6.2285860351e01,
                -6.2285863096e01,
                -6.2285809393e01,
                -6.2285693931e01,
                -6.2285536360e01,
                -6.2285355757e01,
                -6.2285161598e01,
            ],
        }
    )

    ngkpt_tsmear
    return (ngkpt_tsmear,)


@app.cell(hide_code=True)
def _(mo, ngkpt_tsmear, plt):
    cols = ["8x8x8","10x10x10", "12x12x12", "14x14x14", "16x16x16"]
    global_min = ngkpt_tsmear[cols].min().min()

    plt.figure(figsize=(10, 6))
    for col in cols:
        plt.plot(
            ngkpt_tsmear["tsmear"],
            ngkpt_tsmear[col],
            marker="o",
            linewidth=2,
            label=col
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
        title="DOS and Integrated DOS", xlims=(-5, 10), show=False
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
    return


if __name__ == "__main__":
    app.run()
