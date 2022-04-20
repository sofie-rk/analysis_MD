from scipy.stats import pearsonr, ttest_ind

def pearson_correlation_coefficient(x,y, title=''):

    '''
    x [array_like]
    y [array_like]

    Finds the Pearson's correlation coefficient for x and y,
    when x and y are lists (array_like) of the same length.
    '''
    coeff, p_value = pearsonr(x,y)

    print(title)
    print('Pearson\'s correlation coefficient: ', coeff, '\n')
    return coeff

def t_test(x,y, title=''):
    '''
    x [array_like]
    y [array_like]
    '''

    t_statistic, p_value = ttest_ind(x,y)

    print(title)
    print("Calculated t-statistic: ", t_statistic, '\n')

    return t_statistic
