from ProteinAnalysisTrajectory import *
from ProteinSurfaceAnalysisTrajectory import ProteinSurfaceAnalysisTrajectory

from construct_plots import *
from statistical_analysis import *
from constants import *
from data_analysis import *

color_surf_prot_vacuum = colors_Dark2
color_surf_prot_vacuum2 = colors_tab20b


C1_vacuum_1     = ProteinSurfaceAnalysisTrajectory('surf_prot_vacuum/C1-vacuum-1nm/md_C1-vacuum-1nm.tpr', 'surf_prot_vacuum/C1-vacuum-1nm/md_C1-vacuum-1nm_noPBC.xtc', color=next(color_surf_prot_vacuum), label='C1 vacuum - 10 Å')
C1_vacuum_1p5   = ProteinSurfaceAnalysisTrajectory('surf_prot_vacuum/C1-vacuum-1p5nm/md_C1-vacuum-1p5nm.tpr', 'surf_prot_vacuum/C1-vacuum-1p5nm/md_C1-vacuum-1p5nm_noPBC.xtc', color=next(color_surf_prot_vacuum), label='C1 vacuum - 15 Å')
C1_vacuum_2     = ProteinSurfaceAnalysisTrajectory('surf_prot_vacuum/C1-vacuum-2nm/md_C1-vacuum-2nm.tpr', 'surf_prot_vacuum/C1-vacuum-2nm/md_C1-vacuum-2nm_noPBC.xtc', color=next(color_surf_prot_vacuum), label='C1 vacuum - 20 Å')
C1_vacuum_short = ProteinSurfaceAnalysisTrajectory('surf_prot_vacuum/C1-vacuum-1nm-15ns/md_C1-vacuum-1nm-15ns.tpr', 'surf_prot_vacuum/C1-vacuum-1nm-15ns/md_C1-vacuum-1nm-15ns_noPBC.xtc', color=next(color_surf_prot_vacuum), label='C1')

EC_vacuum_1     = ProteinSurfaceAnalysisTrajectory('surf_prot_vacuum/EC-vacuum-1nm/md_EC-vacuum-1nm.tpr', 'surf_prot_vacuum/EC-vacuum-1nm/md_EC-vacuum-1nm_noPBC.xtc', color=next(color_surf_prot_vacuum), label='EC vacuum - 10 Å')
EC_vacuum_1p5   = ProteinSurfaceAnalysisTrajectory('surf_prot_vacuum/EC-vacuum-1p5nm/md_EC-vacuum-1p5nm.tpr', 'surf_prot_vacuum/EC-vacuum-1p5nm/md_EC-vacuum-1p5nm_noPBC.xtc', color=next(color_surf_prot_vacuum), label='EC vacuum - 15 Å')
EC_vacuum_2     = ProteinSurfaceAnalysisTrajectory('surf_prot_vacuum/EC-vacuum-2nm/md_EC-vacuum-2nm.tpr', 'surf_prot_vacuum/EC-vacuum-2nm/md_EC-vacuum-2nm_noPBC.xtc', color=next(color_surf_prot_vacuum), label='EC vacuum - 20 Å')
EC_vacuum_short = ProteinSurfaceAnalysisTrajectory('surf_prot_vacuum/EC-vacuum-1nm-15ns/md_EC-vacuum-1nm-15ns.tpr', 'surf_prot_vacuum/EC-vacuum-1nm-15ns/md_EC-vacuum-1nm-15ns_noPBC.xtc', color=next(color_surf_prot_vacuum), label='EC')

SP2_vacuum_1    = ProteinSurfaceAnalysisTrajectory('surf_prot_vacuum/SP2-vacuum-1nm/md_SP2-vacuum-1nm.tpr', 'surf_prot_vacuum/SP2-vacuum-1nm/md_SP2-vacuum-1nm_noPBC.xtc', color=next(color_surf_prot_vacuum2), label='SP2 vacuum - 10 Å')
SP2_vacuum_1p5  = ProteinSurfaceAnalysisTrajectory('surf_prot_vacuum/SP2-vacuum-1p5nm/md_SP2-vacuum-1p5nm.tpr', 'surf_prot_vacuum/SP2-vacuum-1p5nm/md_SP2-vacuum-1p5nm_noPBC.xtc', color=next(color_surf_prot_vacuum2), label='SP2 vacuum - 15 Å')
SP2_vacuum_2    = ProteinSurfaceAnalysisTrajectory('surf_prot_vacuum/SP2-vacuum-2nm/md_SP2-vacuum-2nm.tpr', 'surf_prot_vacuum/SP2-vacuum-2nm/md_SP2-vacuum-2nm_noPBC.xtc', color=next(color_surf_prot_vacuum2), label='SP2 vacuum - 20 Å')
SP2_vacuum_short= ProteinSurfaceAnalysisTrajectory('surf_prot_vacuum/SP2-vacuum-1nm-15ns/md_SP2-vacuum-1nm-15ns.tpr', 'surf_prot_vacuum/SP2-vacuum-1nm-15ns/md_SP2-vacuum-1nm-15ns_noPBC.xtc', color=next(color_surf_prot_vacuum2), label='SP2')

A1_vacuum_1     = ProteinSurfaceAnalysisTrajectory('surf_prot_vacuum/A1-vacuum-1nm/md_A1-vacuum-1nm.tpr', 'surf_prot_vacuum/A1-vacuum-1nm/md_A1-vacuum-1nm_noPBC.xtc', color=next(color_surf_prot_vacuum2), label='A1 vacuum - 10 Å')
A1_vacuum_1p5   = ProteinSurfaceAnalysisTrajectory('surf_prot_vacuum/A1-vacuum-1p5nm/md_A1-vacuum-1p5nm.tpr', 'surf_prot_vacuum/A1-vacuum-1p5nm/md_A1-vacuum-1p5nm_noPBC.xtc', color=next(color_surf_prot_vacuum2), label='A1 vacuum - 15 Å')
A1_vacuum_2     = ProteinSurfaceAnalysisTrajectory('surf_prot_vacuum/A1-vacuum-2nm/md_A1-vacuum-2nm.tpr', 'surf_prot_vacuum/A1-vacuum-2nm/md_A1-vacuum-2nm_noPBC.xtc', color=next(color_surf_prot_vacuum2), label='A1 vacuum - 20 Å')
A1_vacuum_short = ProteinSurfaceAnalysisTrajectory('surf_prot_vacuum/A1-vacuum-1nm-15ns/md_A1-vacuum-1nm-15ns.tpr', 'surf_prot_vacuum/A1-vacuum-1nm-15ns/md_A1-vacuum-1nm-15ns_noPBC.xtc', color='black', label='A1')

one_vacuum = [EC_vacuum_1, SP2_vacuum_1, A1_vacuum_1, C1_vacuum_1]
one_point_five_vacuum = [C1_vacuum_1p5, EC_vacuum_1p5, SP2_vacuum_1p5]

C1_models_vacuum = [C1_vacuum_1, C1_vacuum_1p5, C1_vacuum_2]
EC_models_vacuum = [EC_vacuum_1, EC_vacuum_1p5, EC_vacuum_2]
SP2_models_vacuum = [SP2_vacuum_1, SP2_vacuum_1p5, SP2_vacuum_2]
A1_models_vacuum = [A1_vacuum_1, A1_vacuum_1p5, A1_vacuum_2]

shorter_runs = [C1_vacuum_short, A1_vacuum_short, SP2_vacuum_short, EC_vacuum_short]

#plot_z_min_distance(C1_models_vacuum, xlim=(-2,100), title=hphob_surf, ylim=(0,3.5), loc_legend='best')
#plot_zcoord_center_of_geometry(C1_models_vacuum, xlim=(-2, 100), title=hphob_surf, ylim=(0,4), loc_legend='lower right')

#plot_z_min_distance(SP2_models_vacuum, xlim=(-2,100), title='Very hydrophilic surface', ylim=(0,3.5), loc_legend='best')

#plot_z_min_distance(EC_models_vacuum, xlim=(-2,100), title='Hydrophilic Surface', ylim=(0,3.5), loc_legend='best')


# plot_z_min_distance(one_vacuum, xlim=(-2,50), ylim=(0,1.5), loc_legend='best')
# plot_zcoord_center_of_geometry(one_vacuum, xlim=(-2,50), ylim=(0,2.5), loc_legend='best')



plot_zcoord_center_of_geometry(shorter_runs, loc_legend='upper right')

#plot_zcoord_center_of_geometry(A1_models_vacuum)
#plot_z_min_distance(A1_models_vacuum)
