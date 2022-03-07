import MDAnalysis as mda
from ProteinStructure import *
import matplotlib.pyplot as plt


OPLS_protein = ProteinStructure("OPLS_gro.gro", "OPLS_xtc.xtc", "OPLS", "blue")
MARTINI_protein = ProteinStructure("MARTINI_gro.gro", "MARTINI_xtc.xtc", "MARTINI", "orange")
   
rmsd_OPLS = OPLS_protein.rmsd()

print(rmsd_OPLS)

rmsd_OPLS.plot(title='RMSD')
plt.show()
