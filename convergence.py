import matplotlib.pyplot as plt

energy_values = [
    -6.2225511036e01,
    -6.2258180354e01,
    -6.2274086001e01,
    -6.2280977299e01,
    -6.2283654790e01,
    -6.2284567872e01,
    -6.2284805280e01,
    -6.2284845217e01,
    -6.2284847699e01,
]

# At ngkpt 8 8 8
ecut_values = [21, 24, 27, 30, 33, 36, 39, 42, 45]

plt.scatter(ecut_values, energy_values)
plt.title("Ecut Convergence at ngkpt 8 8 8")
plt.xlabel("Ecut (Ha)")
plt.ylabel("$E_{total}$")
plt.grid()
plt.show()


## ngkpt Convergence at Ecut = 33
energy_values = [
    -6.2200732126e01,
    -6.2288980977e01,
    -6.2285847286e01,
    -6.2283654790e01,
    -6.2285283821e01,
]

ngkpt_values = [2, 4, 6, 8, 10]
plt.scatter(ngkpt_values, energy_values)
plt.title("ngkpt Convergence at ecut = 33")
plt.xlabel("ngkpt (Ha)")
plt.ylabel("$E_{total}$")
plt.grid()
plt.show()
