from ProteinAnalysisTrajectory import *

from construct_plots import *
from statistical_analysis import *
from constants import *
from data_analysis import *

color_compare_aa_cg_ff = colors_Dark2

amber = ProteinAnalysisTrajectory('/compare_aa_cg_ff/amber.gro', '/compare_aa_cg_ff/amber.xtc', color=next(color_compare_aa_cg_ff), label='AMBER99SB-ILDN')
charmm = ProteinAnalysisTrajectory('/compare_aa_cg_ff/charmm.gro', '/compare_aa_cg_ff/charmm.xtc', color=next(color_compare_aa_cg_ff), label='CHARMM27')
opls = ProteinAnalysisTrajectory('/compare_aa_cg_ff/opls.gro', '/compare_aa_cg_ff/opls.xtc', color=next(color_compare_aa_cg_ff), label='OPLS-AA')
martini = ProteinAnalysisTrajectory('/compare_aa_cg_ff/martini.gro', '/compare_aa_cg_ff/martini.xtc', color=next(color_compare_aa_cg_ff), label='MARTINI 3')

proteins = [amber, charmm, opls, martini]

t_amber, rgyr_amber = amber.r_gyr2()
t_charmm, rgyr_charmm = charmm.r_gyr2()
t_opls, rgyr_opls = opls.r_gyr2()
t_martini, rgyr_martini = martini.r_gyr2()

info_of_time_series(rgyr_charmm, title='CHARMM')
info_of_time_series(rgyr_opls, title='OPLS')
info_of_time_series(rgyr_amber, title='AMBER')

t_test(rgyr_martini, rgyr_amber, 'MARTINI vs AMBER')
t_test(rgyr_martini, rgyr_charmm, 'MARTINI vs CHARMM')
t_test(rgyr_martini, rgyr_opls, 'MARTINI vs OPLS')

pearson_correlation_coefficient(rgyr_martini, rgyr_amber, 'MARTINI vs AMBER')
pearson_correlation_coefficient(rgyr_martini, rgyr_charmm, 'MARTINI vs CHARMM')
pearson_correlation_coefficient(rgyr_martini, rgyr_opls, 'MARTINI vs OPLS')



rgyr_plot(proteins, loc_legend='center left')

