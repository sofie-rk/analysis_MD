from cmath import inf


def info_of_time_series(values, title=''):

    min_value = inf
    max_value = -inf
    mean = 0

    for value in values:
        if value < min_value:
            min_value = value
        
        if value > max_value:
            max_value = value

        mean += value/len(values)

    print('DATA ANALYSIS: \t' + title)
    print('min value:\t', min_value)
    print('max value:\t', max_value)
    print('mean:\t:', mean)
    print('number of values:\t', len(values))