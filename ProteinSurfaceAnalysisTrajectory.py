
from tabnanny import verbose
import MDAnalysis as mda
from MDAnalysis.analysis import rms
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


    def r_gyr(self):
        rgyr = []
        time = []
        protein = self.protein_structure.select_atoms('protein')
        for t in self.protein_structure.trajectory:
            time.append(self.protein_structure.trajectory.time)
            rgyr.append(protein.radius_of_gyration())
        
        rgyr_df = pd.DataFrame(rgyr, columns=[column_rgyr], index=time)
        rgyr_df.index.name = 'Time [ps]'

        return rgyr_df

    def surface_values(self):
        surface_val = []
        time = []
        surface = self.protein_structure.select_atoms('resname 1SURF')

        for t in self.protein_structure.trajectory:
            time.append(self.protein_structure.trajectory.time)

            positions = surface.positions
            t = []
            for pos in positions:
                t.append(pos[2])
            t.sort()
            surface_val.append((sum(t[600:])/len(t[600:]))/10)
        
        return surface_val

    def rmsd(self):
        rmsd = []
        time = []
        protein = self.protein_structure.select_atoms('protein')

        R = rms.RMSD(self.protein_structure,
                        self.protein_structure)
        R.run()
        rmsd_array = R.rmsd
        
        for row in rmsd_array:
            time.append(row[1])
            rmsd.append(row[2])
        
        df_rmsd = pd.DataFrame(rmsd, columns=[columns_rmsd], index=time)
        
        return df_rmsd
    
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
                if pos[-1]/10 < limit:
                    number_of_resiudes_current += 1

            residues_within_limit.append(number_of_resiudes_current)
        
        df_residues_within_limit= pd.DataFrame(residues_within_limit, columns=[column_number_of_residues], index=time)
        
        return df_residues_within_limit

    def surface_positions(self):

        time = []
        z_coord_max = []
        z_coord_min = []

        z_positions = []

        surface = self.protein_structure.select_atoms('resname 1SURF')
        for t in self.protein_structure.trajectory:
            time.append(self.protein_structure.trajectory.time)

            z_pos = []

            positions = surface.positions
            zmin = inf
            zmax = -inf
            for pos in positions:
                z_pos.append(pos[2])
                if (pos[2] > zmax):
                    zmax = pos[2]
                if (pos[2] < zmin):
                    zmin = pos[2]
            
            z_positions.append(z_pos)
            z_coord_max.append(zmax/10)
            z_coord_min.append(zmin/10)

        plt.plot(time, z_coord_min, label='Min z')
        plt.plot(time, z_coord_max, label='Max z')
        plt.grid(True)
        plt.legend()
        plt.show()

        max_displacement = []
        for i in range(1,len(z_positions)):
            max_displacement_current = 0
            for j in range(len(z_positions[0])):
                displacement = abs(z_positions[i][j] - z_positions[i-1][j])
                if (displacement > max_displacement_current):
                    max_displacement_current = displacement
            
            max_displacement.append(max_displacement_current)

        plt.plot(time[1:], max_displacement)
        plt.grid(True)
        plt.show()

    

   



