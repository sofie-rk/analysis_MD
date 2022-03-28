import matplotlib.pyplot as plt

def rgyr_plot(proteins):

    labels = [p.label for p in proteins]
    colors = [p.color for p in proteins]
    r_gyrs = [p.r_gyr() for p in proteins]

    fig = plt.figure()

    for i in range(len(proteins)):

        plt.plot(r_gyrs[i].index, r_gyrs[i]['Radius of gyration [Å]'], color=colors[i], label=labels[i])

    plt.ylabel("Radius of gyration [Å]")
    plt.xlabel("Time [ps]")
    plt.title("Radius of gyration - comparing force fields")
    plt.legend()
    plt.grid(True)
    plt.xlim(0,200)
    plt.show()