import matplotlib.pyplot as plt

def rgyr_plot(proteins, title='Radius of gyration'):

    labels = [p.label for p in proteins]
    colors = [p.color for p in proteins]
    r_gyrs = [p.r_gyr() for p in proteins]

    fig = plt.figure()

    for i in range(len(proteins)):

        plt.plot(r_gyrs[i].index/1000, r_gyrs[i]['Radius of gyration [Å]'], color=colors[i], label=labels[i])

    plt.ylabel("Radius of gyration [Å]")
    plt.xlabel("Time [ns]")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    #plt.xlim(0,200)
    plt.show()

def rgyr_error(protein, proteins):

    fig = plt.figure()

    time_st, r_gyr_st = protein.r_gyr2()

    colors = [p.color for p in proteins]

    compare_with = protein.label
 

    for i in range(len(proteins)):
        t, rgyr = proteins[i].r_gyr2()
        y_axis = [abs(rgyr[j]-r_gyr_st[j])/r_gyr_st[j] * 100 for j in range(len(rgyr))]

        
        plt.plot(t, y_axis, color=colors[i], label=proteins[i].label)

    plt.legend()
    plt.title(compare_with)
    plt.xlabel('Time [ps]')
    plt.ylabel('Relative error [%]')
    plt.grid(True)
    plt.show()

    ##print(r_gyr)
    # for i in range(len(proteins)):
    #     x_axis = r_gyrs[i].index

    #     y_axis = []
    #     df = r_gyrs[i]
    #     y_axis = df['Radius of gyration [Å]'] - 5
    #     #y_axis = r_gyrs[i]['Radius of gyration [Å]'] - r_gyr_st
    #     print(y_axis)
    #     plt.plot(x_axis, y_axis, color=colors[i])
    
    # plt.legend()
    # plt.grid()
    # plt.show()