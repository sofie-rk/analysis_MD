
import MDAnalysis as mda
from MDAnalysis.analysis import rms
import pandas as pd

class ProteinStructure:
    def __init__(self, path_file_gro, path_file_xtc, label, color):
        self.path_file_gro = path_file_gro
        self.path_file_xtc = path_file_xtc
        self.label = label
        self.color = color

        self.protein_structure = mda.Universe("./raw_files/"+path_file_gro, "./raw_files/"+path_file_xtc)

    def r_gyr(self):
        rgyr = []
        time = []
        protein = self.protein_structure.select_atoms('protein')
        for t in self.protein_structure.trajectory:
            time.append(self.protein_structure.trajectory.time)
            rgyr.append(protein.radius_of_gyration())
        
        rgyr_df = pd.DataFrame(rgyr, columns=['Radius of gyration [Å]'], index=time)
        rgyr_df.index.name = 'Time [ps]'

        return rgyr_df
    
    def rmsd(self):
        rmsd_analysis = rms.RMSD(self.protein_structure, select='backbone', groupselections=['name CA', 'protein'])
        rmsd_analysis.run()

        rmsd_df = pd.DataFrame(rmsd_analysis.rmsd[:,2:],
                                columns=['Backbone', 'C-alphas', 'Protein'],
                                index=rmsd_analysis.rmsd[:,1])

        rmsd_df.index.name = 'Time [ps]'
        
        return rmsd_df