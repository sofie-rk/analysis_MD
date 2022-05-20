from ProteinAnalysis import ProteinAnalysis
from ProteinSurfaceAnalysisTrajectory import *

from construct_plots import *
from statistical_analysis import *
from constants import *
from data_analysis import *

color_secondary_structure = colors_Dark2

LIW_ss = ProteinSurfaceAnalysisTrajectory('/lysozyme_in_water/LIW-ss/md_LIW-ss.tpr', '/lysozyme_in_water/LIW-ss/md_LIW-ss_noPBC.xtc', color=next(color_LIW_ss_proteins), label="Specified secondary structure")
LIW_noss = ProteinSurfaceAnalysisTrajectory('/lysozyme_in_water/LIW-noss/md_LIW-noss.tpr', '/lysozyme_in_water/LIW-noss/md_LIW-noss_noPBC.xtc', color=next(color_LIW_ss_proteins), label="No specified secondary structure")

C1surf_ss   = ProteinSurfaceAnalysisTrajectory('surf_prot_water/C1-water-0p5nm/md_C1-water-0p5nm.tpr', 'surf_prot_water/C1-water-0p5nm/md_C1-water-0p5nm_noPBC.xtc', color='red', label='Specified secondary structure')
C1surf_noss = ProteinSurfaceAnalysisTrajectory('surf_prot_water/C1-water-noss/md_C1-water-noss.tpr', 'surf_prot_water/C1-water-noss/md_C1-water-noss_noPBC.xtc', color='blue', label='No specified secondary structure')



#LIW_ss_test = ProteinSurfaceAnalysisTrajectory('/lysozyme_in_water/LIW-ss/md_LIW-ss.tpr', '/lysozyme_in_water/LIW-ss/md_LIW-ss-noPBC-test.xtc', color='red', label="Specified secondary structure TEST")


#surface_ss = ProteinSurfaceAnalysisTrajectory('surf_prot_water/C1-water-0p5nm/md_C1-water-0p5nm.gro', 'surf_prot_water/C1-water-0p5nm/md_C1-water-0p5nm.xtc', color=next(color_secondary_structure), label="No specified secondary structure")
#surface_noss = ProteinSurfaceAnalysisTrajectory('surf_prot_water/C1-water-noss/md_C1-water-noss.gro', 'surf_prot_water/C1-water-noss/md_C1-water-noss.xtc', color=next(color_secondary_structure), label="No specified secondary structure")

# ss_em = ProteinAnalysis('/secondary_structure/ss-em.gro', label='ss em.gro', color='black', id=0)
# ss_eq = ProteinAnalysis('/secondary_structure/ss-eq.gro', label='ss eq.gro', color='blue', id=1)

# noss_init = ProteinAnalysis('/secondary_structure/noss-lysozyme_centered.gro', label='noss lysozyme_centered.gro', color='red', id=2)
# noss_em = ProteinAnalysis('/secondary_structure/noss-em.gro', label='noss em.gro', color='black', id=0)
# noss_eq = ProteinAnalysis('/secondary_structure/noss-eq.gro', label='noss eq.gro', color='blue', id=1)


# print("\nNO SECONDARY STRUCTURE SPECIFIED")
# print(noss_init.label +'\t', noss_init.r_gyr())
# print(noss_em.label +'\t', noss_em.r_gyr())
# print(noss_eq.label +'\t', noss_eq.r_gyr())

LIW_proteins = [LIW_ss, LIW_noss]

C1_surf = [C1surf_ss, C1surf_noss]

plot_rmsd(LIW_proteins)

#plot_rgyr(C1_surf, title='With hydrophobic surface')
#plot_zcoord_center_of_geometry(C1_surf, ylim=(0,4), title='With hydrophobic (C1) surface')
#plot_z_min_distance(C1_surf, title='With hydrophobic (C1) surface', ylim=(0,1.5), loc_legend='upper right')


#plot_rgyr(LIW_proteins, title='Lysozyme-in-water')

#plot_rgyr(surface_proteins, title='Secondary structure - with surface')
# plot_z_min_distance(surface_proteins, title='Secondary structure - with surface')
# plot_zcoord_center_of_geometry(surface_proteins, title='Secondary structure - with surface')

#rgyr_plot(proteins)

