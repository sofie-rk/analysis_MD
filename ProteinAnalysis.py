import MDAnalysis as mda
from MDAnalysis.analysis import rms
import pandas as pd

class ProteinAnalysis:

    def __init__(self, path_file_gro, label, color, id):
        self.path_file_gro = path_file_gro
        self.label = label
        self.color = color
        self.id = id

        self.protein_structure = mda.Universe("./raw_files/"+path_file_gro)

    def r_gyr(self):

        protein = self.protein_structure.select_atoms('protein')

        return protein.radius_of_gyration()
