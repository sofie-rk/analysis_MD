import MDAnalysis as mda
from ProteinAnalysisTrajectory import *
import matplotlib.pyplot as plt

from construct_plots import rgyr_plot, rgyr_error

ss_lysozyme = ProteinAnalysisTrajectory('md_run.gro', 'md_run.xtc', color='blue', label='Specified secondary structure')

one = ProteinAnalysisTrajectory('1.gro', '1.xtc', label='1', color='green')
two = ProteinAnalysisTrajectory('2.gro', '2.xtc', label='2', color='red')
three = ProteinAnalysisTrajectory('3.gro', '3.xtc', label='3', color='black')
four = ProteinAnalysisTrajectory('4.gro', '4.xtc', label='4', color='orange')
five = ProteinAnalysisTrajectory('5.gro', '5.xtc', label='5', color='purple')

three_nopbc = ProteinAnalysisTrajectory('3.gro', '3_noPBC.xtc', label='secondary structure specified', color='red')
four_nopbc = ProteinAnalysisTrajectory('4.gro', '4_noPBC.xtc', label='4 - no PBC', color='orange')
five_nopbc = ProteinAnalysisTrajectory('5.gro', '5_noPBC.xtc', label='no secondary structure specified', color='purple')

three_ss = ProteinAnalysisTrajectory('3.gro', '3_noPBC.xtc', label='secondary structure specified', color='red')
five_ss = ProteinAnalysisTrajectory('5.gro', '5_noPBC.xtc', label='no secondary structure specified', color='purple')

three_101010 = ProteinAnalysisTrajectory('3.gro', '3_noPBC.xtc', label='10nm x 10nm x10 nm', color='red')
four_121212 = ProteinAnalysisTrajectory('5.gro', '5_noPBC.xtc', label='12nm x 12nm x 12nm', color='blue')

two_compare = ProteinAnalysisTrajectory('2.gro', '2_noPBC.xtc', label='10nm x 10nm x 10nm', color='black')
three_compare = ProteinAnalysisTrajectory('3.gro', '3_noPBC.xtc', label='10nm x 10nm x 10nm', color='red')

shorter_eq = ProteinAnalysisTrajectory('3.gro', '3_noPBC.xtc', label='shorter eq', color='green')
longer_eq = ProteinAnalysisTrajectory('longer_eq.gro', 'longer_eq.xtc', label='Longer eq', color='purple')

mdp_files = ProteinAnalysisTrajectory('mdp-file-test.gro', 'mdp-file-test.xtc', label='new mdp-file', color='orange')

compare_1_2_3 = [one, two, three_nopbc]
compare_ss = [three_ss, five_ss]
compare_box_size = [three_101010, four_121212]
compare_pbc = [three, three_nopbc]
compare = [two_compare, three_compare]

compare_eq_time = [longer_eq, shorter_eq]

compare_mdp_files = [mdp_files, three_101010]

#rgyr_plot(compare_1_2_3)
# rgyr_plot(compare_ss, title="MARTINI lysozyme - secondary structure analysis")
# rgyr_plot(compare_box_size, title="Box size")
# rgyr_plot(compare, title='Same conditions')
#rgyr_plot(compare_pbc)
rgyr_plot(compare_eq_time)

#rgyr_plot(compare_mdp_files)

#proteins = [ss_lysozyme, one, two]

#rgyr_plot(proteins)

# noss_lysozyme = ProteinAnalysisTrajectory('noss_md_0_1.gro', 'noss_md_0_1.xtc', color='blue', label='MARTINI - no secondary structure')
# ss_lysozyme = ProteinAnalysisTrajectory('md_0_1.gro', 'md_0_1.xtc', color='black', label='MARTINI - specifying secondary structure')
# charmm_lysozyme = ProteinAnalysisTrajectory('charmm_md_0_1.gro', 'charmm_md_0_1.xtc', color='red', label='CHARMM')
# opls_lysozyme = ProteinAnalysisTrajectory('OPLS_md_0_1.gro', 'OPLS_md_0_1.xtc', color='green', label='OPLS')

# proteins = [noss_lysozyme, ss_lysozyme, charmm_lysozyme, opls_lysozyme]
# rgyr_plot(proteins)
# rgyr_error(noss_lysozyme, [ss_lysozyme, charmm_lysozyme, opls_lysozyme])
# rgyr_error(ss_lysozyme, [noss_lysozyme, charmm_lysozyme, opls_lysozyme])


# OPLS1 = ProteinAnalysisTrajectory('OPLS_sc1.gro', 'OPLS_sc1.xtc', "OPLS neutral", "#000033")
# OPLS2 = ProteinAnalysisTrajectory('OPLS_sc2.gro', 'OPLS_sc2.xtc', "OPLS 0.3 mol/L", "#0000CC")
# OPLS3 = ProteinAnalysisTrajectory('OPLS_sc3.gro', 'OPLS_sc3.xtc', "OPLS 0.6 mol/L", "#3333FF")
# OPLS4 = ProteinAnalysisTrajectory('OPLS_sc4.gro', 'OPLS_sc4.xtc', "OPLS 0.9 mol/L", "#9999FF")

# MARTINI1 = ProteinAnalysisTrajectory('MARTINI_sc1.gro', 'MARTINI_sc1.xtc', 'MARTINI neutral', '#660033')
# MARTINI2 = ProteinAnalysisTrajectory('MARTINI_sc2.gro', 'MARTINI_sc2.xtc', 'MARTINI 0.3 mol/L', '#CC0066')
# MARTINI3 = ProteinAnalysisTrajectory('MARTINI_sc3.gro', 'MARTINI_sc3.xtc', 'MARTINI 0.6 mol/L', '#FF662B')
# MARTINI4 = ProteinAnalysisTrajectory('MARTINI_sc4.gro', 'MARTINI_sc4.xtc', 'MARTINI 0.9 mol/L', '#FFCCE5')

# proteins = [OPLS1, OPLS2, OPLS3, OPLS4, MARTINI1, MARTINI2, MARTINI3, MARTINI4]


# rgyr_plot(proteins)

# OPLS_protein = ProteinAnalysisTrajectory("OPLS_gro.gro", "OPLS_xtc.xtc", "OPLS", "blue")
# MARTINI_protein = ProteinAnalysisTrajectory("MARTINI_gro.gro", "MARTINI_xtc.xtc", "MARTINI", "orange")
# CHARMM_protein = ProteinAnalysisTrajectory("CHARMM_gro.gro", "CHARMM_xtc.xtc", label="CHARMM27", color="red")
# AMBER_protein = ProteinAnalysisTrajectory("AMBER_gro.gro", "AMBER_xtc.xtc", label="AMBER", color="green")

# OPLS_rgyr = OPLS_protein.r_gyr()
# MARTINI_rgyr = MARTINI_protein.r_gyr()
# CHARMM_rgyr = CHARMM_protein.r_gyr()
# AMBER_rgyr = AMBER_protein.r_gyr()

# construct_plot([OPLS_rgyr, MARTINI_rgyr, CHARMM_rgyr, AMBER_rgyr], [OPLS_protein.color, MARTINI_protein.color, CHARMM_protein.color, AMBER_protein.color], [OPLS_protein.label, MARTINI_protein.label, CHARMM_protein.label, AMBER_protein.label])



# rmsd_OPLS = OPLS_protein.rmsd()

# print(rmsd_OPLS)

# rmsd_OPLS.plot(title='RMSD')
# plt.show()
