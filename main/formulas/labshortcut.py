from math import sqrt
try:
    from reround import reround
except ModuleNotFoundError:
    from formulas.reround import reround
def fprint(text): #Função para printar letra por letra no terminal
    from time import sleep
    for l in text:
        print(l, end='', flush=True)
        sleep(0.016)
    print()
 
def all(n, trueValue=0, round=False, roundDecimal=2): #Função que une todas as fórmulas presentes
    mean = sum(n) / len(n)
    population_standard_deviation = sqrt(sum([(x - mean) ** 2 for x in n]) / len(n))
    sample_standard_deviation = sqrt(sum([(x - mean) ** 2 for x in n]) / (len(n)-1))
    relative_standard_deviation = sample_standard_deviation / mean
    coefficient_of_variation = (sample_standard_deviation / mean) * 100
    values = [mean, sample_standard_deviation, population_standard_deviation, relative_standard_deviation, coefficient_of_variation]
    if trueValue != 0: #Se o valor for diferente de zero fará com que essas duas fórmulas entrem para a lista final (values)
            absolute_error = mean - trueValue
            relative_error = ((mean - trueValue) / trueValue) * 100
            values.extend([absolute_error, relative_error])
    if round is True:  #If que retorna o valor arredondado ou o valor cheio (se for desabilitado)
        rounded_values = []
        for i in values:
            i = reround(i, roundDecimals=roundDecimal)
            rounded_values.append(i)
        return rounded_values
    else:
        return values

def mean(n, round=False, roundDecimal=2): #mean (Média)
    mean = sum(n) / len(n)
    if round is True:
        return reround(mean, roundDecimals=roundDecimal)
    else:
        return mean

def ssd(n, round=False, roundDecimal=2): #ssd = sample standard deviation (Desvio padrão amostral)
    mean = sum(n) / len(n) 
    sample_standard_deviation = sqrt(sum([(x - mean) ** 2 for x in n]) / (len(n)-1))
    if round is True:
        return reround(sample_standard_deviation, roundDecimals=roundDecimal)
    else:
        return sample_standard_deviation

def psd(n, round=False, roundDecimal=2): #psd = population standard deviation (Desvio padrão populacional)
    mean = sum(n) / len(n) 
    population_standard_deviation = sqrt(sum([(x - mean) ** 2 for x in n]) / len(n))
    if round is True:
        return reround(population_standard_deviation, roundDecimals=roundDecimal)
    else:
        return population_standard_deviation

def rsd(n, round=False, roundDecimal=2): #rsd = relative standard deviation (Desvio padrão relativo)
    mean = sum(n) / len(n)
    sample_standard_deviation = sqrt(sum([(x - mean) ** 2 for x in n]) / (len(n)-1))
    relative_standard_deviation = sample_standard_deviation / mean
    if round is True:
        return reround(relative_standard_deviation, roundDecimals=roundDecimal)
    else:
        return relative_standard_deviation

def cv(n, round=False, roundDecimal=2): #cv = coefficient of variation (Coeficiente de variação)
    mean = sum(n) / len(n) 
    sample_standard_deviation = sqrt(sum([(x - mean) ** 2 for x in n]) / (len(n)-1))
    coefficient_of_variation = (sample_standard_deviation / mean) * 100
    if round is True:
        return reround(coefficient_of_variation, roundDecimals=roundDecimal)
    else:
        return coefficient_of_variation
    
def aerr(n, trueValue, round=False, roundDecimal=2): #aerr = absolute error (Erro absoluto)
    mean = sum(n) / len(n) 
    absolute_error = mean - trueValue
    if round is True:
        return reround(absolute_error, roundDecimals=roundDecimal)
    else:
        return absolute_error

def rerr(n, trueValue, round=False, roundDecimal=2): #reer = relative error (Erro relativo)
    mean = sum(n) / len(n) 
    relative_error = ((mean - trueValue) / trueValue) * 100
    if round is True:
        return reround(relative_error, roundDecimals=roundDecimal)
    else:
        return relative_error

