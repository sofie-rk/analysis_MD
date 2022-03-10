import matplotlib.pyplot as plt

def construct_plot(dfs, colors, labels):

    fig = plt.figure()

    for i in range(len(colors)):

        plt.plot(dfs[i].index, dfs[i]['Radius of gyration [Å]'], color=colors[i], label=labels[i])

    plt.ylabel("Radius of gyration [Å]")
    plt.xlabel("Time [ps]")
    plt.title("Radius of gyration - comparing force fields")
    plt.legend()
    plt.grid(True)
    plt.show()