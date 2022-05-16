from urllib3 import encode_multipart_formdata
from ProteinAnalysisTrajectory import *
from ProteinSurfaceAnalysisTrajectory import ProteinSurfaceAnalysis

from construct_plots import *
from statistical_analysis import *
from constants import *
from data_analysis import *

color_vacuum_simulations = colors_Dark2
color_vacuum_simulations2 = colors_tab20c

C1_1 = ProteinSurfaceAnalysis('vacuum_simulations/C1-1.gro', 'vacuum_simulations/C1-1.xtc', color=next(color_vacuum_simulations), label='C1 - 1 nm')
C1_1point5 = ProteinSurfaceAnalysis('vacuum_simulations/C1-1.5.gro', 'vacuum_simulations/C1-1.5.xtc', color=next(color_vacuum_simulations), label='C1 - 1.5 nm')
C1_2 = ProteinSurfaceAnalysis('vacuum_simulations/C1-2.gro', 'vacuum_simulations/C1-2.xtc', color=next(color_vacuum_simulations), label='C1 - 2 nm')
C1_3 = ProteinSurfaceAnalysis('vacuum_simulations/C1-3.gro', 'vacuum_simulations/C1-3.xtc', color=next(color_vacuum_simulations), label='C1 - 3 nm')

P1_1 = ProteinSurfaceAnalysis('vacuum_simulations/P1-1.gro', 'vacuum_simulations/P1-1.xtc', color=next(color_vacuum_simulations), label='P1 - 1 nm')
P1_1point5 = ProteinSurfaceAnalysis('vacuum_simulations/P1-1.5.gro', 'vacuum_simulations/P1-1.5.xtc', color=next(color_vacuum_simulations), label='P1 - 1.5 nm')
P1_2 = ProteinSurfaceAnalysis('vacuum_simulations/P1-2.gro', 'vacuum_simulations/P1-2.xtc', color=next(color_vacuum_simulations), label='P1 - 2 nm')
P1_3 = ProteinSurfaceAnalysis('vacuum_simulations/P1-3.gro', 'vacuum_simulations/P1-3.xtc', color=next(color_vacuum_simulations), label='P1 - 3 nm')

EC_1 = ProteinSurfaceAnalysis('vacuum_simulations/EC-1.gro', 'vacuum_simulations/EC-1.xtc', color=next(color_vacuum_simulations2), label='EC - 1 nm')
EC_1point5 = ProteinSurfaceAnalysis('vacuum_simulations/EC-1.5.gro', 'vacuum_simulations/EC-1.5.xtc', color=next(color_vacuum_simulations2), label='EC - 1.5 nm')
EC_2 = ProteinSurfaceAnalysis('vacuum_simulations/EC-2.gro', 'vacuum_simulations/EC-2.xtc', color=next(color_vacuum_simulations2), label='EC - 2 nm')
EC_3 = ProteinSurfaceAnalysis('vacuum_simulations/EC-3.gro', 'vacuum_simulations/EC-3.xtc', color=next(color_vacuum_simulations2), label='EC - 3 nm')



C1_proteins = [C1_1, C1_1point5, C1_2, C1_3]
P1_proteins = [P1_1, P1_1point5, P1_2, P1_3]
EC_proteins = [EC_1, EC_1point5, EC_2, EC_3]

compare_1point5 = [C1_1point5, P1_1point5, EC_1point5]

# rgyr_plot(C1_proteins, xlim=(0,50))
# rgyr_plot(EC_proteins, xlim=(0,50))
# rgyr_plot(P1_proteins, xlim=(0,50))

# z_coord_plot(C1_proteins, xlim=(0,50))
# z_coord_plot(EC_proteins, xlim=(0,50))
# z_coord_plot(P1_proteins, xlim=(0,50))

# z_coord_plot(compare_1point5, surface_z=3.2)
# rgyr_plot(compare_1point5)

# z_coord_plot(EC_proteins, surface_z=3.2, xlim=(0,100))
# rgyr_plot(EC_proteins, xlim=(0,100))




