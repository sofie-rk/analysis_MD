import matplotlib.pyplot as plt
from sqlalchemy import column
from constants import *

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

    fig = plt.figure()

    for i in range(len(proteins)):

        plt.plot(z_coord[i].index/1000, (z_coord[i][column_center_of_geometry])-surface_z, line_type, color=colors[i], label=labels[i])

    plt.ylabel("Distance from the surface [nm] (center of geometry)")
    plt.xlabel(xlabel_time)
    plt.title(title)
    plt.legend(loc=loc_legend)
    plt.grid(True)
    if (xlim != None):
        plt.xlim(xlim)
    if (ylim != None):
        plt.ylim(ylim)
    plt.show()

def plot_z_min_distance(proteins, z_surface=3.2, title='', loc_legend='lower right', xlim=None, ylim=None):

    labels = [p.label for p in proteins]
    colors = [p.color for p in proteins]
    min_z = [p.z_min_distance() for p in proteins]

    for i in range(len(proteins)):
        plt.plot(min_z[i].index/1000, min_z[i][column_min_distance]-z_surface , color=colors[i], label=labels[i])

    plt.ylabel('Minimum distance between protein molecule and surface [nm]')
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