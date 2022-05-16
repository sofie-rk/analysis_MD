from ProteinAnalysisTrajectory import *
from ProteinSurfaceAnalysisTrajectory import ProteinSurfaceAnalysis

from construct_plots import *
from statistical_analysis import *
from constants import *
from data_analysis import *

colors_vacuum = colors_Dark2

C1_surface = ProteinSurfaceAnalysis('/vacuum_surf_prot/C1_md.gro', '/vacuum_surf_prot/C1_md.xtc',label='C1 surface', color=next(colors_vacuum))
P1_surface = ProteinSurfaceAnalysis('/vacuum_surf_prot/P1_md.gro', '/vacuum_surf_prot/P1_md.xtc',label='P1 surface', color=next(colors_vacuum))
EC_surface = ProteinSurfaceAnalysis('/vacuum_surf_prot/EC_md.gro', '/vacuum_surf_prot/EC_md.xtc',label='EC surface', color=next(colors_vacuum))

proteins = [C1_surface, P1_surface, EC_surface]

#z_coord_plot(proteins)
#rgyr_plot(proteins)

plot_rgyr([P1_surface])
plot_zcoord_center_of_geometry([P1_surface])