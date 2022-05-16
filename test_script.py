import matplotlib.pyplot as plt
import pandas as pd
import MDAnalysis as mda
from MDAnalysis.tests.datafiles import PSF, DCD, GRO, XTC

print(mda.__version__)

u = mda.Universe(PSF, DCD)

structure = mda.Universe("./raw_files//surf_prot_vacuum/4surf_prot_vacuum.gro", "./raw_files//surf_prot_vacuum/4surf_prot_vacuum.xtc")
print(structure)
print(len(structure.trajectory))
print(hasattr(structure, 'trajectory'))

print('\n.atoms: \n', structure.atoms[-3:])
print('\n.atoms.names: \n', structure.atoms[:5].names)
print('\n.atoms.masses: \n', structure.atoms[:5].masses)
print('\n.atoms.residues: \n', structure.atoms[:100].residues)
print('\n.atoms.resnames: \n', structure.atoms[:10].resnames)
print('\n.residues: \n', structure.residues[-3:])
print('\n.select_atoms: \n', structure.select_atoms('resname GLU'))
print('\n.select_atoms...n_residues: \n', structure.select_atoms('resid 50-100').n_residues)


print('\n.select_atoms.positions: \n', structure.select_atoms('resid 1-5').positions)


print("******************************")

print("\nLength of trajectory: ", len(structure.trajectory))

rgyr = []
time = []
protein = structure.select_atoms("protein")
for ts in structure.trajectory:
    time.append(structure.trajectory.time)
    rgyr.append(structure.atoms.radius_of_gyration())
    #print("Frame: {:3d}, Time: {:4.0f} ps, Rgyr: {:.4f} A".format(ts.frame, time, rgyr))

rgyr_df = pd.DataFrame(rgyr, columns=['Radius of gyration (A)'], index=time)
rgyr_df.index.name = 'Time (ps)'

#print(len('CBCCHHHHHHHHHHTTCTTBTTBCTHHHHHHHHHHTSSBTTCEECCSSSCCEETTTTEETTTTEECSSCTTCCCTTCEEGGGGGSSSCHHHHHHHHHHHHSSGGGGSHHHHHHTTTSCGGGSSTTCCC'))
#print(len('CBCCHHHHHHHHHHTTCTTBTTBCTHHHHHHHHHHTSSBTTCEECCSSSCCEETTTTEETTTTEECSSCTTCCCTTCEEGGGGGSSSCHHHHHHHHHHHHSSGGGGSHHHHHHTTTSCGGGSSTTCCC'))

#print(len('CCHHHHHHHHHCCEEEEEECTTSCEEEETTEEEESSSCHHHHHHHHHHHHTSCCTTBCCHHHHHHHHHHHHHHHHHHHHHCTTTHHHHHHSCHHHHHHHHHHHHHHHHHHHHTCHHHHHHHHTTCHHHHHHHHHSSHHHHHSHHHHHHHHHHHHHSSSGGGC'))

#print(len('CBCCHHHHHHHHHHTTCTTBTTBCTHHHHHHHHHHTSSBTTCEECCSSSCCEETTTTEETTTTEECSSCTTCCCTTCEEGGGGGSSSCHHHHHHHHHHHHHSSGGGGSHHHHHHTTTSCGGGSSTTCCC'))

# plt.plot(time, rgyr)
# plt.xlabel('Time (ps)')
# plt.ylabel('Radius of gyration (nm)')
# plt.show()

C = structure.select_atoms('protein')
time2 = []
center = []
for ts in structure.trajectory:
    time.append(structure.trajectory.time)
    center.append(C.atoms.center_of_geometry())

print(center[0:10])

