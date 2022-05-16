
from ProteinAnalysisTrajectory import *
from ProteinSurfaceAnalysisTrajectory import ProteinSurfaceAnalysisTrajectory


from construct_plots import *
from statistical_analysis import *
from constants import *
from data_analysis import *

color_surf_prot_water = colors_Dark2


test = C1_water_0p5nm    = ProteinSurfaceAnalysisTrajectory('surf_prot_water/C1-water-0p5nm/md_C1-water-0p5nm.gro', '/surf_prot_water/C1-water-0p5nm/md_C1-water-0p5nm.xtc', color=next(color_surf_prot_water), label='C1 water - 0.5 nm')

test.surface_positions()