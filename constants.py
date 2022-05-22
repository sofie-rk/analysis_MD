
import matplotlib.pyplot as plt

#color_list = ['#a54a40', '#5c3e46', '#809e54', '#eba176', '#84cacc', '#c6cc4a', '#da6088', '#aaaaaa', '#dd363e', '#f77237', '#2c6047', '#1b2e9b', '#ed908e']

# https://colorbrewer2.org/#type=diverging&scheme=BrBG&n=10
#color_list = ['#d7191c', '#fdae61', '#ffffbf', '#abd9e9', '#2c7bb6']

color_list = iter(['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e'])

colors_Dark2 = iter([plt.cm.Dark2(i) for i in range(8)])

color_C1_vacuum = iter([(0.4588235294117647, 0.4392156862745098, 0.7019607843137254, 1.0),
                        (0.8509803921568627, 0.37254901960784315, 0.00784313725490196, 1.0),
                        (0.10588235294117647, 0.6196078431372549, 0.4666666666666667, 1.0),
                        (0.4588235294117647, 0.4392156862745098, 0.7019607843137254, 1.0)
                    ])


color_EC_vacuum = iter([(0.4, 0.6509803921568628, 0.11764705882352941, 1.0),
                        (0.9019607843137255, 0.6705882352941176, 0.00784313725490196, 1.0),
                        (0.6509803921568628, 0.4627450980392157, 0.11372549019607843, 1.0),
                        (0.4, 0.6509803921568628, 0.11764705882352941, 1.0),
])

color_SP2_vacuum = iter([(0.9058823529411765, 0.1607843137254902, 0.5411764705882353, 1.0),
                        (0.4, 0.4, 0.4, 1.0),
                        (0.10588235294117647, 0.6196078431372549, 0.4666666666666667, 1.0),
                        (0.9058823529411765, 0.1607843137254902, 0.5411764705882353, 1.0),
])

color_A1_vacuum = iter(['brown',
                    'blue',
                    'olive',
                    'brown'
])

color_LIW_ss_proteins = iter(['gray', 'blue'])

colors_tab20b = iter([plt.cm.tab20b(i) for i in range(8)])
colors_tab20c = iter([plt.cm.tab20c(i) for i in range(8)])

colors_summer = iter([plt.cm.summer(i) for i in range(0,100, 10)])

colors_seq_orange = iter(['#800026', '#e31a1c', '#fc4e2a', '#fd8d3c'])
colors_seq_pink = iter(['#980043', '#dd1c77', '#df65b0', '#d7b5d8'])
colors_seq_blue = iter(['#08519c', '#3182bd', '#6baed6', '#bdd7e7'])

xlabel_time = 'Time [ns]'

column_center_of_geometry = 'center_of_geometry'
column_rgyr = 'rgyr'
column_min_distance = 'minimum_distance'
column_number_of_residues = 'number_of_residues'
columns_rmsd = 'RMSD'
columns_hphilres = 'hphil_res_within_limit'
columns_hphobres = 'hphob_res_within_limit'

hphob_surf = 'Hydrophobic Surface'

adsorption_limit = 5.0


