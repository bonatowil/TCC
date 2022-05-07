from math import sqrt

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
    Q = abs(xq-xp) / f
    if str(confidence) == '99':
        Qcrit = (table['99'][len(n)-3])
        reject = True if Q > Qcrit else False
        return {f'{xq}': reject} if automatic_outliner else reject
    elif str(confidence) == '95':
        Qcrit = (table['95'][len(n)-3])
        reject = True if Q > Qcrit else False
        return {f'{xq}': reject} if automatic_outliner else reject
    elif str(confidence) == '90':
        Qcrit = (table['90'][len(n)-3])
        reject = True if Q > Qcrit else False
        return {f'{xq}': reject} if automatic_outliner else reject
    else:
        raise ValueError

def grubbstest(n, sus_n):
    mean = sum(n) / len(n)
    standard_deviation = sqrt(sum([(values - mean) ** 2 for values in n]) / (len(n)-1))
    G = abs(sus_n - mean) / standard_deviation

if __name__ == '__main__':
    pass
