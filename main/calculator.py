from math import sqrt
from reround import reround

def fprint(text): #Função para printar letra por letra no terminal
    from time import sleep
    for l in text:
        print(l, end='', flush=True)
        sleep(0.016)
    print()
 
def all(n, trueValue=0, round=True, roundDecimal=2): #Função que une todas as fórmulas presentes
    mean = sum(n) / len(n)
    population_standart_deviation = sqrt(sum([(values - mean) ** 2 for values in n]) / len(n))
    sample_standart_deviation = sqrt(sum([(values - mean) ** 2 for values in n]) / (len(n)-1))
    relative_standard_deviation = sample_standart_deviation / mean
    coefficient_of_variation = (sample_standart_deviation / mean) * 100
    values = [mean, sample_standart_deviation, population_standart_deviation, relative_standard_deviation, coefficient_of_variation]
    if trueValue != 0: #Se o valor for diferenente de zero fará com que essas duas fórmulas entrem para a lista final (values)
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

def mean(n, round=True, roundDecimal=2): #mean (Média)
    mean = sum(n) / len(n)
    if round is True:
        return reround(mean, roundDecimals=roundDecimal)
    else:
        return mean

def ssd(n, round=True, roundDecimal=2): #ssd = sample standart deviation (Desvio padrão amostral)
    mean = sum(n) / len(n) 
    sample_standart_deviation = sqrt(sum([(values - mean) ** 2 for values in n]) / (len(n)-1))
    if round is True:
        return reround(sample_standart_deviation, roundDecimals=roundDecimal)
    else:
        return sample_standart_deviation

def psd(n, round=True, roundDecimal=2): #psd = population standart deviation (Desvio padrão populacional)
    mean = sum(n) / len(n) 
    population_standart_deviation = sqrt(sum([(values - mean) ** 2 for values in n]) / len(n))
    if round is True:
        return reround(population_standart_deviation, roundDecimals=roundDecimal)
    else:
        return population_standart_deviation

def rsd(n, round=True, roundDecimal=2): #rsd = relative standard deviation (Desvio padrão relativo)
    mean = sum(n) / len(n)
    sample_standart_deviation = sqrt(sum([(values - mean) ** 2 for values in n]) / (len(n)-1))
    relative_standard_deviation = sample_standart_deviation / mean
    if round is True:
        return reround(relative_standard_deviation, roundDecimals=roundDecimal)
    else:
        return relative_standard_deviation

def cv(n, round=True, roundDecimal=2): #cv = coefficient of variation (Coeficiente de variação)
    mean = sum(n) / len(n) 
    sample_standart_deviation = sqrt(sum([(values - mean) ** 2 for values in n]) / (len(n)-1))
    coefficient_of_variation = (sample_standart_deviation / mean) * 100
    if round is True:
        return reround(coefficient_of_variation, roundDecimals=roundDecimal)
    else:
        return coefficient_of_variation
    
def aerr(n, trueValue, round=True, roundDecimal=2): #aerr = absolute error (Erro absoluto)
    mean = sum(n) / len(n) 
    absolute_error = mean - trueValue
    if round is True:
        return reround(absolute_error, roundDecimals=roundDecimal)
    else:
        return absolute_error

def rerr(n, trueValue, round=True, roundDecimal=2): #reer = relative error (Erro relativo)
    mean = sum(n) / len(n) 
    relative_error = ((mean - trueValue) / trueValue) * 100
    if round is True:
        return reround(relative_error, roundDecimals=roundDecimal)
    else:
        return relative_error

if __name__ == '__main__':
    i = 1
    number_list = []
    add_numbers = True
    truevalueloop = True
    round_value = 2
    do_round = False
    while True:
        
        try:
            while add_numbers:
                input_numbers = input(f"Digite o {i}º número: (Deixe em branco quando quiser parar)\n> ").strip()
                print()
                if input_numbers == '' and i > 2:
                    add_numbers = False
                    break
                input_numbers = float(input_numbers)
                i += 1
                number_list.append(input_numbers)
            while truevalueloop:
                trueValue = input("Digite o valor tabelado: (Deixe em branco caso não exista)\n> ").strip()
                print()
                if trueValue == '':
                    truevalueloop = False
                    break
                trueValue = float(trueValue)
                truevalueloop = False
                break
            while True:
                if do_round is False:
                    do_round = input("Deseja arrendondar os valores?: (S/N)\n> ").lower().strip()
                if do_round == 's' or do_round is True:
                    do_round = True
                    round_value = int(input("Quantas casas decimais deseja?: \n> "))
                elif do_round == 'n':
                    do_round = False
                else:
                    do_round = False
                    raise(NameError)
                break
        except ValueError:
            print("Por favor digite um número válido!")
            continue
        except NameError:
            print('\nPor favor digite S ou N!')
            continue


        try:
            trueValue = float(trueValue)
        except ValueError:
            trueValue = 0
        
        all_values = {"numbers": number_list, "round": do_round, "roundDecimal": round_value}
        fprint(f'\nA média é = {mean(*all_values.values())}')
        fprint(f'O desvio padrão amostral é = {ssd(*all_values.values())}')
        fprint(f'O desvio padrão populacional é = {psd(*all_values.values())}')
        fprint(f'O desvio padrão relativo é = {rsd(*all_values.values())}')
        fprint(f'O coeficiente de variação é = {cv(*all_values.values())}%\n')
        if trueValue != 0:
            all_values = {"numbers": number_list, 'trueValue': trueValue, "round": do_round, "roundDecimal": round_value}
            fprint(f'O erro absoluto é = {aerr(*all_values.values())}')
            fprint(f'O erro relativo é = {rerr(*all_values.values())}%\n')

        while True:
            try:
                must_finish = False
                if do_round is False:
                    after_round = input("Deseja arrendondar os valores mostrados?: (S/N)\n> ").lower().strip()
                    if after_round == 's':
                        do_round = True
                        break
                    elif after_round == 'n':
                        pass
                    else:
                        raise(NameError)
                        
                again = input("Deseja calcular novos números?: (S/N)\n> ").lower().strip()
                if again == 's':
                    i = 1
                    number_list = []
                    add_numbers = True
                    truevalueloop = True
                    do_round = False
                    print()
                    break
                elif again == 'n':
                    must_finish = True
                    break
                else:
                    raise(NameError)
            except NameError:
                print("\nPor favor digite S ou N!")
                continue
        if must_finish:
            from time import sleep
            print()
            for l in 'FINISHING...':
                print(l, end='', flush=True)
                sleep(0.1)
            break