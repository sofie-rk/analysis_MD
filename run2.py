from ProteinAnalysis import *
from constants import *
import matplotlib.pyplot as plt
import pandas as pd

noss_filenames = ['noss_7lyz_wo_HOH.pdb', 'noss_lys_CG.pdb', 'noss_lysozyme_centered.gro', 'noss_minimization_vacuum.gro', 'noss_solvated.gro', 'noss_ions_solv_lys.gro', 'noss_em.gro', 'noss_nvt.gro', 'noss_npt.gro', 'noss_md_0_1.gro']
ss_filenames = ['7lyz_wo_HOH.pdb', 'lys_CG.pdb', 'lysozyme_centered.gro', 'minimization_vacuum.gro', 'solvated.gro', 'ions_solv_lys.gro', 'em.gro', 'nvt.gro', 'npt.gro', 'md_0_1.gro']

proteins_noss = []
proteins_ss = []

if (len(noss_filenames) != len(ss_filenames)):
    print('Something wrong with length of input files')
else:
    for i in range(len(noss_filenames)):
        p_noss = ProteinAnalysis(noss_filenames[i], noss_filenames[i], color_list[i], i+1)
        proteins_noss.append(p_noss)

        p_ss = ProteinAnalysis(ss_filenames[i], ss_filenames[i], color_list[i], i+1)
        proteins_ss.append(p_ss)


for i in range(len(proteins_noss)):
    print(proteins_noss[i].id, '\t\t', round(proteins_noss[i].r_gyr(),4), '\t\t', round(proteins_ss[i].r_gyr(),4))


x_axis = [proteins_noss[i].id for i in range(len(proteins_noss))]
y_axis_noss = [proteins_noss[i].r_gyr() for i in range(len(proteins_noss))]
y_axis_ss = [proteins_ss[i].r_gyr() for i in range(len(proteins_ss))]

df = pd.DataFrame({'no-ss': y_axis_noss,
                    'ss':y_axis_ss},
                    index=x_axis)

df.plot.bar(rot=0)
plt.ylim(13,14.3)
plt.grid(True)
plt.show()


# plt.plot(x_axis, y_axis_noss, '.', label='no-ss', color='black')
# plt.plot(x_axis, y_axis_ss, '.', label='ss', color='blue')
# plt.xlabel('File index')
# plt.ylabel('Radius of gyration [Å]')
# plt.show()