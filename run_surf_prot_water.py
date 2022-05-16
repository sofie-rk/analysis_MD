from sympy import minimum
from ProteinAnalysisTrajectory import *
from ProteinSurfaceAnalysisTrajectory import ProteinSurfaceAnalysisTrajectory


from construct_plots import *
from statistical_analysis import *
from constants import *
from data_analysis import *

color_surf_prot_water = colors_Dark2

C1_water_0p5nm    = ProteinSurfaceAnalysisTrajectory('surf_prot_water/C1-water-0p5nm/md_C1-water-0p5nm.gro', '/surf_prot_water/C1-water-0p5nm/md_C1-water-0p5nm.xtc', color=next(color_surf_prot_water), label='C1 water - 0.5 nm')
# C1_water_1nm    = ProteinSurfaceAnalysisTrajectory('real_simulations/md_C1-water-1nm.gro', 'real_simulations/md_C1-water-1nm.xtc', color=next(color_surf_prot_water), label='C1 water - 1 nm')
# C1_water_1p5nm  = ProteinSurfaceAnalysisTrajectory('real_simulations/md_C1-water-1p5nm.gro', 'real_simulations/md_C1-water-1p5nm.xtc', color=next(color_surf_prot_water), label='C1 water - 1.5 nm')
# C1_water_2nm    = ProteinSurfaceAnalysisTrajectory('real_simulations/md_C1-water-2nm.gro', 'real_simulations/md_C1-water-2nm.xtc', color=next(color_surf_prot_water), label='C1 water - 2 nm')

SP2_water_0p5nm  = ProteinSurfaceAnalysisTrajectory('surf_prot_water/SP2-water-0p5nm/md_SP2-water-0p5nm.gro', '/surf_prot_water/SP2-water-0p5nm/md_SP2-water-0p5nm.xtc', color=next(color_surf_prot_water), label='SP2 water - 0.5 nm')
# #SP2_water_1nm    = ProteinSurfaceAnalysisTrajectory('real_simulations/md_SP2-water-1nm.gro', 'real_simulations/md_SP2-water-1nm.xtc', color=next(color_surf_prot_water), label='SP2 water - 1 nm')
# SP2_water_1p5nm  = ProteinSurfaceAnalysisTrajectory('real_simulations/md_SP2-water-1p5nm.gro', 'real_simulations/md_SP2-water-1p5nm.xtc', color=next(color_surf_prot_water), label='SP2 water - 1.5 nm')
# #SP2_water_2nm    = ProteinSurfaceAnalysisTrajectory('real_simulations/md_SP2-water-2nm.gro', 'real_simulations/md_SP2-water-2nm.xtc', color=next(color_surf_prot_water), label='SP2 water - 2 nm')

EC_water_0p5    = ProteinSurfaceAnalysisTrajectory('surf_prot_water/EC-water-0p5nm/md_EC-water-0p5nm.gro', '/surf_prot_water/EC-water-0p5nm/md_EC-water-0p5nm.xtc', color=next(color_surf_prot_water), label='EC water - 0.5 nm')
#EC_water_1nm    = ProteinSurfaceAnalysisTrajectory('real_simulations/md_EC-water-1nm.gro', 'real_simulations/md_EC-water-1nm.xtc', color=next(color_surf_prot_water), label='EC water - 1 nm')
#EC_water_1p5nm  = ProteinSurfaceAnalysisTrajectory('real_simulations/md_EC-water-1p5nm.gro', 'real_simulations/md_EC-water-1p5nm.xtc', color=next(color_surf_prot_water), label='EC water - 1.5 nm')
#EC_water_2nm    = ProteinSurfaceAnalysisTrajectory('real_simulations/md_EC-water-2nm.gro', 'real_simulations/md_EC-water-2nm.xtc', color=next(color_surf_prot_water), label='EC water - 2 nm')

#C1_systems = [C1_water_2nm, C1_water_1p5nm, C1_water_1nm]
# EC_systems = [EC_water_1nm]
# SP2_systems = [SP2_water_0p5nm, SP2_water_1p5nm]

# two_nm_systems = [C1_water_2nm]
# onepointfive_nm_systems = [C1_water_1p5nm, SP2_water_1p5nm]
# one_nm_system = [EC_water_1nm, C1_water_1nm]
zeropointfive_nm_systems = [C1_water_0p5nm, SP2_water_0p5nm, EC_water_0p5]


# rgyr_plot(C1_systems)
# z_coord_plot(C1_systems, surface_z=3.2)
#minimum_distance(C1_systems, title='Hydrophobic surface (-CH2)', loc_legend='upper right')

#minimum_distance(EC_systems)


#plot_rgyr(zeropointfive_nm_systems)
plot_zcoord_center_of_geometry(zeropointfive_nm_systems)
plot_z_min_distance(zeropointfive_nm_systems)
plot_residues_within_limit(zeropointfive_nm_systems, 5.0)


