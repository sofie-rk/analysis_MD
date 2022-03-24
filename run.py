import MDAnalysis as mda
from ProteinStructure import *
import matplotlib.pyplot as plt

from construct_plots import construct_plot


OPLS1 = ProteinStructure('OPLS_sc1.gro', 'OPLS_sc1.xtc', "OPLS neutral", "blue")
OPLS2 = ProteinStructure('OPLS_sc2.gro', 'OPLS_sc2.xtc', "OPLS 0.3 mol/L", "red")
OPLS3 = ProteinStructure('OPLS_sc3.gro', 'OPLS_sc3.xtc', "OPLS 0.6 mol/L", "pink")
OPLS4 = ProteinStructure('OPLS_sc4.gro', 'OPLS_sc4.xtc', "OPLS 0.9 mol/L", "orange")

MARTINI1 = ProteinStructure('MARTINI_sc1.gro', 'MARTINI_sc1.xtc', 'MARTINI neutral', 'blue')
MARTINI2 = ProteinStructure('MARTINI_sc2.gro', 'MARTINI_sc2.xtc', 'MARTINI 0.3 mol/L', 'red')
MARTINI3 = ProteinStructure('MARTINI_sc3.gro', 'MARTINI_sc3.xtc', 'MARTINI 0.6 mol/L', 'pink')
MARTINI4 = ProteinStructure('MARTINI_sc4.gro', 'MARTINI_sc4.xtc', 'MARTINI 0.9 mol/L', 'orange')

proteins = [OPLS1, OPLS2, OPLS3, OPLS4, MARTINI1, MARTINI2, MARTINI3, MARTINI4]
labels = [p.label for p in proteins]
colors = [p.color for p in proteins]
r_gyrs = [p.r_gyr() for p in proteins]

construct_plot(r_gyrs, colors=colors, labels=labels)

# OPLS_protein = ProteinStructure("OPLS_gro.gro", "OPLS_xtc.xtc", "OPLS", "blue")
# MARTINI_protein = ProteinStructure("MARTINI_gro.gro", "MARTINI_xtc.xtc", "MARTINI", "orange")
# CHARMM_protein = ProteinStructure("CHARMM_gro.gro", "CHARMM_xtc.xtc", label="CHARMM27", color="red")
# AMBER_protein = ProteinStructure("AMBER_gro.gro", "AMBER_xtc.xtc", label="AMBER", color="green")

# OPLS_rgyr = OPLS_protein.r_gyr()
# MARTINI_rgyr = MARTINI_protein.r_gyr()
# CHARMM_rgyr = CHARMM_protein.r_gyr()
# AMBER_rgyr = AMBER_protein.r_gyr()

# construct_plot([OPLS_rgyr, MARTINI_rgyr, CHARMM_rgyr, AMBER_rgyr], [OPLS_protein.color, MARTINI_protein.color, CHARMM_protein.color, AMBER_protein.color], [OPLS_protein.label, MARTINI_protein.label, CHARMM_protein.label, AMBER_protein.label])



# rmsd_OPLS = OPLS_protein.rmsd()

# print(rmsd_OPLS)

# rmsd_OPLS.plot(title='RMSD')
# plt.show()
