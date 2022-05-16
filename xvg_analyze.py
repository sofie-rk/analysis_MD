import matplotlib.pyplot as plt

def read_file(filename):

    file = open(filename, 'r')

    x = []
    y = []

    for line in file:
        a = line.split()
        x.append(float(a[0]))
        y.append(float(a[1]))
        #print(line.rstrip(' '))

    file.close()

    plt.plot(x[1000:],y[1000:])
    plt.show()


read_file('./raw_files/vacuum_surf_prot/potential3.txt')