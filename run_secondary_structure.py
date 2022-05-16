from ProteinAnalysis import ProteinAnalysis
from ProteinSurfaceAnalysisTrajectory import *

from construct_plots import *
from statistical_analysis import *
from constants import *
from data_analysis import *

color_secondary_structure = colors_Dark2

LIW_ss = ProteinSurfaceAnalysisTrajectory('/lysozyme_in_water/LIW-ss/md_LIW-ss.gro', '/lysozyme_in_water/LIW-ss/md_LIW-ss_noPBC.xtc', color=next(color_secondary_structure), label="Specified secondary structure")
LIW_noss = ProteinSurfaceAnalysisTrajectory('/lysozyme_in_water/LIW-noss/md_LIW-noss.gro', '/lysozyme_in_water/LIW-noss/md_LIW-noss_noPBC.xtc', color=next(color_secondary_structure), label="No specified secondary structure")

# ss_test = ProteinSurfaceAnalysis('/lysozyme_in_water/LIW-ss/md_LIW-ss.gro', '/lysozyme_in_water/LIW-ss/md_LIW-ss.xtc', color=next(color_secondary_structure), label="TEST Specified secondary structure")
# no_sstest = ProteinSurfaceAnalysis('/lysozyme_in_water/LIW-noss/md_LIW-noss.gro', '/lysozyme_in_water/LIW-noss/md_LIW-noss.xtc', color=next(color_secondary_structure), label="TEST No specified secondary structure")
# ss_init = ProteinAnalysis('/secondary_structure/ss-lysozyme_centered.gro', label='ss lysozyme_centered.gro', color='red', id=2)
# ss_em = ProteinAnalysis('/secondary_structure/ss-em.gro', label='ss em.gro', color='black', id=0)
# ss_eq = ProteinAnalysis('/secondary_structure/ss-eq.gro', label='ss eq.gro', color='blue', id=1)

# noss_init = ProteinAnalysis('/secondary_structure/noss-lysozyme_centered.gro', label='noss lysozyme_centered.gro', color='red', id=2)
# noss_em = ProteinAnalysis('/secondary_structure/noss-em.gro', label='noss em.gro', color='black', id=0)
# noss_eq = ProteinAnalysis('/secondary_structure/noss-eq.gro', label='noss eq.gro', color='blue', id=1)


# print("\nNO SECONDARY STRUCTURE SPECIFIED")
# print(noss_init.label +'\t', noss_init.r_gyr())
# print(noss_em.label +'\t', noss_em.r_gyr())
# print(noss_eq.label +'\t', noss_eq.r_gyr())

proteins = [LIW_ss, LIW_noss]


# rgyr_plot(proteins)

