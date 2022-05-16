from ProteinAnalysisTrajectory import *
from ProteinSurfaceAnalysisTrajectory import ProteinSurfaceAnalysisTrajectory

from construct_plots import *
from statistical_analysis import *
from constants import *
from data_analysis import *

color_surf_prot_vacuum = colors_Dark2


C1_vacuum_1     = ProteinSurfaceAnalysisTrajectory('real_simulations_vacuum/md_C1-vacuum-1nm.gro', 'real_simulations_vacuum/md_C1-vacuum-1nm.xtc', color=next(color_surf_prot_vacuum), label='C1 - 1 nm')
C1_vacuum_1p5   = ProteinSurfaceAnalysisTrajectory('real_simulations_vacuum/md_C1-vacuum-1p5nm.gro', 'real_simulations_vacuum/md_C1-vacuum-1p5nm.xtc', color=next(color_surf_prot_vacuum), label='C1 - 1.5 nm')
C1_vacuum_2     = ProteinSurfaceAnalysisTrajectory('real_simulations_vacuum/md_C1-vacuum-2nm.gro', 'real_simulations_vacuum/md_C1-vacuum-2nm.xtc', color=next(color_surf_prot_vacuum), label='C1 - 2nm')

EC_vacuum_1     = ProteinSurfaceAnalysisTrajectory('real_simulations_vacuum/md_EC-vacuum-1nm.gro', 'real_simulations_vacuum/md_EC-vacuum-1nm.xtc', color=next(color_surf_prot_vacuum), label='EC - 1 nm ')
EC_vacuum_1p5   = ProteinSurfaceAnalysisTrajectory('real_simulations_vacuum/md_EC-vacuum-1p5nm.gro', 'real_simulations_vacuum/md_EC-vacuum-1p5nm.xtc', color=next(color_surf_prot_vacuum), label='EC - 1.5 nm ')

SP2_vacuum_1    = ProteinSurfaceAnalysisTrajectory('real_simulations_vacuum/md_SP2-vacuum-1nm.gro', 'real_simulations_vacuum/md_SP2-vacuum-1nm.xtc', color=next(color_surf_prot_vacuum), label='SP2 - 1 nm')
SP2_vacuum_1p5  = ProteinSurfaceAnalysisTrajectory('real_simulations_vacuum/md_SP2-vacuum-1p5nm.gro', 'real_simulations_vacuum/md_SP2-vacuum-1p5nm.xtc', color=next(color_surf_prot_vacuum), label='SP2 - 1.5 nm')
SP2_vacuum_2    = ProteinSurfaceAnalysisTrajectory('real_simulations_vacuum/md_SP2-vacuum-2nm.gro', 'real_simulations_vacuum/md_SP2-vacuum-2nm.xtc', color=next(color_surf_prot_vacuum), label='SP2 - 2 nm')

one_vacuum = [C1_vacuum_1, EC_vacuum_1, SP2_vacuum_1]
one_point_five_vacuum = [C1_vacuum_1p5, EC_vacuum_1p5, SP2_vacuum_1p5]

C1_models_vacuum = [C1_vacuum_1, C1_vacuum_1p5, C1_vacuum_2]
EC_models_vacuum = [EC_vacuum_1, EC_vacuum_1p5]
SP2_models_vacuum = [SP2_vacuum_1, SP2_vacuum_1p5, SP2_vacuum_2]

#rgyr_plot(C1_models_vacuum)
# z_coord_plot(C1_models_vacuum, loc_legend='upper right', surface_z=3.2)

# z_coord_plot(one_point_five_vacuum, surface_z=3.2, loc_legend='best')

#z_coord_plot(EC_models_vacuum)
# minimum_distance(C1_models_vacuum, title='Hydrophobic surface (-CH2-)')

# minimum_distance(EC_models_vacuum, title='PEG surface (-O-CH2-CH2-)')

# minimum_distance(SP2_models_vacuum, title='Very hydrophilic surface (-OH)')

# number_of_residues_within_limit_plot(C1_models_vacuum, adsorption_limit=adsorption_limit)