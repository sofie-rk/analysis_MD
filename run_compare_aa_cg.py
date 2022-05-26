
from ProteinSurfaceAnalysisTrajectory import ProteinSurfaceAnalysisTrajectory

from construct_plots import *
from statistical_analysis import *
from constants import *
from data_analysis import *
from colors import *
from labels import *


LIW_OPLS = ProteinSurfaceAnalysisTrajectory('lysozyme_in_water/compare_aa_cg/md_LIW-OPLS.tpr', 'lysozyme_in_water/compare_aa_cg/md_LIW-OPLS_noPBC.xtc', color=color_OPLS, label=label_OPLS)
LIW_AMBER = ProteinSurfaceAnalysisTrajectory('lysozyme_in_water/compare_aa_cg/md_LIW-AMBER.tpr', 'lysozyme_in_water/compare_aa_cg/md_LIW-AMBER_noPBC.xtc', color=color_AMBER, label=label_AMBER)
LIW_CHARMM = ProteinSurfaceAnalysisTrajectory('lysozyme_in_water/compare_aa_cg/md_LIW-CHARMM.tpr', 'lysozyme_in_water/compare_aa_cg/md_LIW-CHARMM_noPBC.xtc', color=color_CHARMM, label=label_CHARMM)
LIW_MARTINI = ProteinSurfaceAnalysisTrajectory('lysozyme_in_water/compare_aa_cg/md_LIW-MARTINI.tpr', 'lysozyme_in_water/compare_aa_cg/md_LIW-MARTINI_noPBC.xtc', color=color_MARTINI, label=label_MARTINI)

proteins = [LIW_OPLS, LIW_AMBER, LIW_CHARMM, LIW_MARTINI]

plot_rgyr(proteins, ylim=(13.6,14.75))

#plot_rmsd(proteins)