import math
from statistics import mean


def pearson_correlation(list_1, list_2):
    x_mean = mean(list_1)
    t_mean = mean(list_2)
    num = 0
    den_1 = 0
    den_2 = 0
    for i in range(len(list_1)):
        num += (list_1[i] - x_mean) * (list_2[i] - t_mean)
        den_1 += (list_1[i] - x_mean) ** 2
        den_2 += (list_2[i] - t_mean) ** 2
    r = num / (math.sqrt(den_1) * math.sqrt(den_2))
    return r


list_1 = [6, 6, 4, 7, 8, 9]
list_2 = [7, 7, 8, 8, 9, 10]

corr = pearson_correlation(list_1, list_2)
print('Pearsons correlation: %.3f' % corr)
