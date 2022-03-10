import MDAnalysis as mda
from ProteinStructure import *
import matplotlib.pyplot as plt

from construct_plots import construct_plot


OPLS_protein = ProteinStructure("OPLS_gro.gro", "OPLS_xtc.xtc", "OPLS", "blue")
MARTINI_protein = ProteinStructure("MARTINI_gro.gro", "MARTINI_xtc.xtc", "MARTINI", "orange")
CHARMM_protein = ProteinStructure("CHARMM_gro.gro", "CHARMM_xtc.xtc", label="CHARMM27", color="red")
AMBER_protein = ProteinStructure("AMBER_gro.gro", "AMBER_xtc.xtc", label="AMBER", color="green")

OPLS_rgyr = OPLS_protein.r_gyr()
MARTINI_rgyr = MARTINI_protein.r_gyr()
CHARMM_rgyr = CHARMM_protein.r_gyr()
AMBER_rgyr = AMBER_protein.r_gyr()

construct_plot([OPLS_rgyr, MARTINI_rgyr, CHARMM_rgyr, AMBER_rgyr], [OPLS_protein.color, MARTINI_protein.color, CHARMM_protein.color, AMBER_protein.color], [OPLS_protein.label, MARTINI_protein.label, CHARMM_protein.label, AMBER_protein.label])



# rmsd_OPLS = OPLS_protein.rmsd()

# print(rmsd_OPLS)

# rmsd_OPLS.plot(title='RMSD')
# plt.show()
