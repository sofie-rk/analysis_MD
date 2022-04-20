
import matplotlib.pyplot as plt

#color_list = ['#a54a40', '#5c3e46', '#809e54', '#eba176', '#84cacc', '#c6cc4a', '#da6088', '#aaaaaa', '#dd363e', '#f77237', '#2c6047', '#1b2e9b', '#ed908e']

# https://colorbrewer2.org/#type=diverging&scheme=BrBG&n=10
#color_list = ['#d7191c', '#fdae61', '#ffffbf', '#abd9e9', '#2c7bb6']

color_list = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e']

colors_Dark2 = iter([plt.cm.Dark2(i) for i in range(8)])

colors_tab20b = iter([plt.cm.tab20b(i) for i in range(8)])

colors_summer = iter([plt.cm.summer(i) for i in range(0,100, 10)])

colors_seq_orange = iter(['#800026', '#e31a1c', '#fc4e2a', '#fd8d3c'])
colors_seq_pink = iter(['#980043', '#dd1c77', '#df65b0', '#d7b5d8'])
colors_seq_blue = iter(['#08519c', '#3182bd', '#6baed6', '#bdd7e7'])
