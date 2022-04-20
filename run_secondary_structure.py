from ProteinAnalysisTrajectory import *

from construct_plots import *
from statistical_analysis import *
from constants import *
from data_analysis import *

color_secondary_structure = colors_Dark2

ss_lysozyme_in_water = ProteinAnalysisTrajectory('/secondary_structure/ss_lysozyme_in_water.gro', '/secondary_structure/ss_lysozyme_in_water.xtc', color=next(color_secondary_structure), label="Specified secindary structure")
no_ss_lysozyme_in_water = ProteinAnalysisTrajectory('/secondary_structure/no-ss_lysozyme_in_water.gro', '/secondary_structure/no-ss_lysozyme_in_water.xtc', color=next(color_secondary_structure), label="No specified secindary structure")

proteins = [ss_lysozyme_in_water, no_ss_lysozyme_in_water]

rgyr_plot(proteins, xlim=(0, 100))
