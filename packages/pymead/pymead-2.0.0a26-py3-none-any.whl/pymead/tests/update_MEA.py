import os

import numpy as np
import matplotlib.pyplot as plt

from pymead.core.mea import MEA
from pymead.utils.read_write_files import load_data


def main():
    base_opt_dir = os.path.join("pai", "root_underwing_opt", "opt_runs", "2023_05_03_A")

    # Load MEA from file
    jmea_file = os.path.join(base_opt_dir, "pai_underwing_04_18_start.jmea")
    jmea = load_data(jmea_file)
    mea = MEA.generate_from_param_dict(jmea)

    # Load parameter list from file
    param_file = os.path.join(base_opt_dir, "ga_opt_7", "opt_X_2.dat")
    parameters = np.loadtxt(param_file)

    # Update parameters
    mea.update_parameters(parameters)

    # Plot airfoils
    fig, ax = plt.subplots()
    for a_name, a in mea.airfoils.items():
        a.plot_airfoil(ax, color="cornflowerblue")
        print(f"Airfoil {a_name}: self-intersecting? {a.check_self_intersection()}")
    ax.set_aspect("equal")

    # Show plot
    plt.show()


if __name__ == "__main__":
    main()
