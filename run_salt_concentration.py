from ProteinAnalysisTrajectory import *

from construct_plots import *
from statistical_analysis import *
from constants import *

color_salt_conc = colors_seq_blue
color_salt_conc2 = colors_seq_pink

martini_neutral = ProteinAnalysisTrajectory('/salt_concentration/MARTINI_sc1.gro', '/salt_concentration/MARTINI_sc1.xtc', color=next(color_salt_conc), label='MARTINI neutral')
martini_0point3 = ProteinAnalysisTrajectory('/salt_concentration/MARTINI_sc2.gro', '/salt_concentration/MARTINI_sc2.xtc', color=next(color_salt_conc), label='MARTINI 0.3 mol/L')
martini_0point6 = ProteinAnalysisTrajectory('/salt_concentration/MARTINI_sc3.gro', '/salt_concentration/MARTINI_sc3.xtc', color=next(color_salt_conc), label='MARTINI 0.6 mol/L')
martini_0point9 = ProteinAnalysisTrajectory('/salt_concentration/MARTINI_sc4.gro', '/salt_concentration/MARTINI_sc4.xtc', color=next(color_salt_conc), label='MARTINI 0.9 mol/L')

opls_neutral = ProteinAnalysisTrajectory('/salt_concentration/OPLS_sc1.gro', '/salt_concentration/OPLS_sc1.xtc', color=next(color_salt_conc2), label='OPLS neutral')
opls_0point3 = ProteinAnalysisTrajectory('/salt_concentration/OPLS_sc2.gro', '/salt_concentration/OPLS_sc2.xtc', color=next(color_salt_conc2), label='OPLS 0.3 mol/L')
opls_0point6 = ProteinAnalysisTrajectory('/salt_concentration/OPLS_sc3.gro', '/salt_concentration/OPLS_sc3.xtc', color=next(color_salt_conc2), label='OPLS 0.6 mol/L')
opls_0point9 = ProteinAnalysisTrajectory('/salt_concentration/OPLS_sc4.gro', '/salt_concentration/OPLS_sc4.xtc', color=next(color_salt_conc2), label='OPLS 0.9 mol/L')

martini_0point6_v2 = ProteinAnalysisTrajectory('/salt_concentration/MARTINI_sc3_v2.gro', '/salt_concentration/MARTINI_sc3_v2.xtc', color='black', label='MARTINI 0.6 mol/L v2')

proteins_martini = [martini_neutral, martini_0point3, martini_0point6_v2, martini_0point9]
proteins_opls = [opls_neutral, opls_0point3, opls_0point6, opls_0point9]

proteins_compare_0point6 = [martini_0point6, martini_0point6_v2]

rgyr_plot(proteins_compare_0point6, xlim=(0,0.2), line_type='.')
rgyr_plot(proteins_martini, xlim=(0,0.2))
rgyr_plot(proteins_opls, xlim=(0,0.2))
