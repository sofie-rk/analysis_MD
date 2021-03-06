import matplotlib.pyplot as plt
from constants import *
from labels import *

import matplotlib as mpl

params = {'legend.fontsize': 'medium',
            'figure.figsize': (12,6),
            'axes.labelsize': 'large',
            'axes.titlesize': 'x-large',

}
mpl.rcParams.update(params)

def plot_rmsd(proteins, title='', xlim=None, ylim=None, loc_legend='lower right', line_type='-'):

    labels = [p.label for p in proteins]
    colors = [p.color for p in proteins]
    rmsd = [p.rmsd() for p in proteins]

    fig = plt.figure()

    for i in range(len(proteins)):

        plt.plot(rmsd[i].index/1000, rmsd[i][columns_rmsd], line_type, color=colors[i], label=labels[i])

    plt.ylabel("RMSD [Å]")
    plt.xlabel(xlabel_time)
    plt.title(title)
    plt.legend(loc=loc_legend)
    plt.grid(True)
    if (xlim != None):
        plt.xlim(xlim)
    if (ylim != None):
        plt.ylim(ylim)
    plt.show()


def plot_rgyr(proteins, title='', xlim=None, ylim=None, loc_legend='lower right', line_type='-'):

    labels = [p.label for p in proteins]
    colors = [p.color for p in proteins]
    r_gyrs = [p.r_gyr() for p in proteins]

    fig = plt.figure()

    for i in range(len(proteins)):

        plt.plot(r_gyrs[i].index/1000, r_gyrs[i][column_rgyr], line_type, color=colors[i], label=labels[i])

    plt.ylabel("Radius of gyration [Å]")
    plt.xlabel("Time [ns]")
    plt.title(title)
    plt.legend(loc=loc_legend)
    plt.grid(True)
    if (xlim != None):
        plt.xlim(xlim)
    if (ylim != None):
        plt.ylim(ylim)
    plt.show()


def plot_zcoord_center_of_geometry(proteins, title='', loc_legend='lower right', line_type='-', xlim=None, ylim=None, surface_z=3.2):
    labels = [p.label for p in proteins]
    colors = [p.color for p in proteins]
    z_coord = [p.zcoord_center_of_geometry() for p in proteins]
    surf_val = [p.surface_values() for p in proteins]

    fig = plt.figure()

    for i in range(len(proteins)):

        plt.plot(z_coord[i].index/1000, (z_coord[i][column_center_of_geometry])-surf_val[i], line_type, color=colors[i], label=labels[i])

    plt.ylabel(ylabel_cog)
    plt.xlabel(xlabel_time)
    plt.title(title)
    plt.legend(loc=loc_legend)
    plt.grid(True)
    if (xlim != None):
        plt.xlim(xlim)
    if (ylim != None):
        plt.ylim(ylim)
    plt.show()

def plot_z_min_distance(proteins, title='', loc_legend='lower right', xlim=None, ylim=None):

    labels = [p.label for p in proteins]
    colors = [p.color for p in proteins]
    min_z = [p.z_min_distance() for p in proteins]
    surf_val = [p.surface_values() for p in proteins]

    for i in range(len(proteins)):
        plt.plot(min_z[i].index/1000, min_z[i][column_min_distance]-surf_val[i] , color=colors[i], label=labels[i])

    plt.ylabel(ylabel_mindist)
    plt.xlabel(xlabel_time)
    plt.title(title)
    plt.legend(loc=loc_legend)
    plt.grid(True)
    if (xlim != None):
        plt.xlim(xlim)
    if (ylim != None):
        plt.ylim(ylim)
    plt.show()

    return 0

def plot_residues_within_limit(proteins, adsorption_limit, title='', loc_legend='lower right', xlim=None, ylim=None):

    labels = [p.label for p in proteins]
    colors = [p.color for p in proteins]
    number_of_residues = [p.residues_within_limit(adsorption_limit) for p in proteins]

    for i in range(len(proteins)):
        plt.plot(number_of_residues[i].index/1000, (number_of_residues[i][column_number_of_residues]) , color=colors[i], label=labels[i])

    plt.ylabel('Number of resiudes within adsorption limit')
    plt.xlabel(xlabel_time)
    plt.title(title+' - with adsorption limit: '+ str(adsorption_limit))
    plt.legend(loc=loc_legend)
    plt.grid(True)
    if (xlim != None):
        plt.xlim(xlim)
    if (ylim != None):
        plt.ylim(ylim)
    plt.show()

    return 0


def plot_hphil_hphob_resiudes_within_limit(protein, title, limit=0.5):

    color = protein.color
    label = protein.color

    df_hphil_res = protein.residues_within_limit(limit)

    df_hphil_res.plot.area()
    plt.legend(['Hydrophobic residues', 'Hydrophilic resiudes'])
    plt.ylim(0,1.1)
    plt.grid(True)
    plt.xlabel(xlabel_time)
    plt.title(title)
    plt.show()
    # plt.plot(df_hphil_res)
    # plt.plot(df_hphob_res)
    # plt.show()