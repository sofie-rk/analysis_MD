
from ProteinSurfaceAnalysisTrajectory import ProteinSurfaceAnalysisTrajectory

from construct_plots import *
from statistical_analysis import *
from constants import *
from data_analysis import *


LIW_OPLS = ProteinSurfaceAnalysisTrajectory('lysozyme_in_water/compare_aa_cg/md_LIW-OPLS.tpr', 'lysozyme_in_water/compare_aa_cg/md_LIW-OPLS_noPBC.xtc', color='red', label='OPLS-AA')
LIW_AMBER = ProteinSurfaceAnalysisTrajectory('lysozyme_in_water/compare_aa_cg/md_LIW-AMBER.tpr', 'lysozyme_in_water/compare_aa_cg/md_LIW-AMBER_noPBC.xtc', color='blue', label='AMBER')

proteins = [LIW_OPLS, LIW_AMBER]

plot_rgyr(proteins)