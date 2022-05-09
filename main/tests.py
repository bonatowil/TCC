from math import sqrt
from reround import reround

def qtest(n, confidence, xq=None):
    table = {'99': [0.994, 0.926, 0.821, 0.740, 0.680, 0.634, 0.598, 0.568], 
            '95':[0.970, 0.829, 0.710, 0.625, 0.568, 0.526, 0.493, 0.466], 
            '90':[0.941, 0.765, 0.642, 0.560, 0.507, 0.468, 0.437, 0.412]}
    automatic_outliner = False
    if xq is None:
        diffs = {}
        automatic_outliner = True
        for value in n:
            mean = sum(n) / len(n)
            diffs[f'{value}'] = abs((value - mean) / mean) * 100
        xq = float(max(diffs, key=diffs.get))
    n.sort()
    xp = n[n.index(xq)+1] if n[n.index(xq)] is not max(n) else n[n.index(xq)-1]
    f = max(n) - min(n)
    q = reround(abs(xq-xp) / f, 2, 'float')
    if str(confidence) == '99':
        qcrit = (table['99'][len(n)-3])
        reject = True if q > qcrit else False
        return {f'{xq}': reject} if automatic_outliner else f"Q: {q} Qcrit: {qcrit}", reject
    elif str(confidence) == '95':
        qcrit = (table['95'][len(n)-3])
        reject = True if q > qcrit else False
        return {f'{xq}': reject} if automatic_outliner else f"Q: {q} Qcrit: {qcrit}", reject
    elif str(confidence) == '90':
        qcrit = (table['90'][len(n)-3])
        reject = True if q > qcrit else False
        return {f'{xq}': reject} if automatic_outliner else f"Q: {q} Qcrit: {qcrit}", reject
    else:
        raise ValueError

def grubbstest(n, sus_n):
    mean = reround(sum(n) / len(n), 2, 'float')
    standard_deviation = reround(sqrt(sum([(values - mean) ** 2 for values in n]) / (len(n)-1)), 2, 'float')
    g = abs(sus_n - mean) / standard_deviation
    return g

if __name__ == '__main__':
    print(grubbstest([4.20, 7.01, 7.31, 7.54, 7.55, 7.58, 7.59], 4.20))
