
import MDAnalysis as mda
from numpy import inf
import pandas as pd
import matplotlib.pyplot as plt
from constants import *

class ProteinSurfaceAnalysisTrajectory:

    def __init__(self, path_file_gro, path_file_xtc, label=None, color=None):
        self.path_file_gro = path_file_gro
        self.path_file_xtc = path_file_xtc
        self.label = label
        self.color = color

        self.protein_structure = mda.Universe("./raw_files/"+path_file_gro, "./raw_files/"+path_file_xtc)

        #self.z_center_of_geometry_df, self.rgyr_df, self.z_min_distance_df, self.residues_within_adslimit = self.protein_information()

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
    
    def zcoord_center_of_geometry(self):
        time = []
        z_center_of_geometry = []

        protein = self.protein_structure.select_atoms('protein')

        for t in self.protein_structure.trajectory:

            time.append(self.protein_structure.trajectory.time)

            z_center_of_geometry.append(protein.center_of_geometry()[2]/10)        

        df_z_center_of_geometry = pd.DataFrame(z_center_of_geometry, columns=[column_center_of_geometry], index=time)
        
        return df_z_center_of_geometry

    def z_min_distance(self):
        time = []
        z_min_distance = []

        protein = self.protein_structure.select_atoms('protein')

        for t in self.protein_structure.trajectory:

            time.append(self.protein_structure.trajectory.time)

            min_z_current = inf
            positions = protein.positions
            for pos in positions:
                if pos[-1]/10 < min_z_current:
                    min_z_current = pos[-1]/10
    

            z_min_distance.append(min_z_current)

        df_min_z = pd.DataFrame(z_min_distance, columns=[column_min_distance], index=time)

        
        return df_min_z

    def residues_within_limit(self, limit):
        time = []
        residues_within_limit = []

        protein = self.protein_structure.select_atoms('protein')

        for t in self.protein_structure.trajectory:

            time.append(self.protein_structure.trajectory.time)

            number_of_resiudes_current = 0
            positions = protein.positions
            for pos in positions:
                if pos[-1]/10 < adsorption_limit:
                    number_of_resiudes_current += 1

            residues_within_limit.append(number_of_resiudes_current)
        
        df_residues_within_limit= pd.DataFrame(residues_within_limit, columns=[column_number_of_residues], index=time)
        
        return df_residues_within_limit

    def surface_positions(self):

        time = []
        z_coord_max = []
        z_coord_min = []

        surface = self.protein_structure.select_atoms('resname 1SURF')
        for t in self.protein_structure.trajectory:
            time.append(self.protein_structure.trajectory.time)

            positions = surface.positions
            zmin = inf
            zmax = -inf
            for pos in positions:
                if (pos[2] > zmax):
                    zmax = pos[2]
                if (pos[2] < zmin):
                    zmin = pos[2]
                
            z_coord_max.append(zmax/10)
            z_coord_min.append(zmin/10)

        plt.plot(time, z_coord_min, label='Min z')
        plt.plot(time, z_coord_max, label='Max z')
        plt.grid(True)
        plt.legend()
        plt.show()

   



