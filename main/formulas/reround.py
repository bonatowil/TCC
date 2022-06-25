def reround(number=int, roundDecimals=2, returnClass='float'):
    if 'e' in str(number):
        from numpy import format_float_positional
        number = str(format_float_positional(number, trim='k'))
    number = str(number)
    whole_number, decimals = number.split('.', 1)
    whole_number, decimals = list(whole_number), list(decimals)

    if len(decimals) != roundDecimals:
        zero_decimals = '0' * (roundDecimals - len(decimals))
        decimals = decimals + list(zero_decimals)

    round_zeros = '0' * roundDecimals
    round_difference_list = ['0', '.'] + list(round_zeros) + (decimals[(roundDecimals):])
    round_difference = ''
    for x in round_difference_list:
        round_difference += x
    round_difference = float(round_difference)
    decimal_index = int(decimals[roundDecimals - 1])

    if roundDecimals == 0:
        decimal_numbers = '0.'
        for x in decimals:
            decimal_numbers += x
        decimal_numbers = float(decimal_numbers)
        if decimal_numbers > 0.5: 
            whole_number[-1] = str(int(whole_number[-1]) + 1)
        if decimal_numbers == 0.5 and int(whole_number[-1]) % 2 != 0:
            whole_number[-1] = str(int(whole_number[-1]) + 1)
        while '10' in whole_number:
            final_number = ''
            for x in whole_number:  
                final_number += x
            if int(final_number) == 10**(len(final_number)-1):
                return str(final_number) if returnClass == 'str' else float(final_number)
            final_number = int(final_number)
            index = whole_number.index('10')
            whole_number[index] = '0' 
            whole_number[index-1] = str(int(whole_number[index-1]) + 1)
        final_number = ''
        for x in whole_number:
            final_number += x
        final_number = int(final_number)
        return str(final_number) if returnClass == 'str' else float(final_number)
    if round_difference > 5 * 10**(-roundDecimals-1):
        decimals[roundDecimals-1] = str(int(decimals[roundDecimals-1]) + 1)

    elif round_difference == 5 * 10**(-roundDecimals-1) and decimal_index % 2 != 0: 
        decimals[roundDecimals-1] = str(int(decimals[roundDecimals-1]) + 1)

    must_add = False
    if '10' in decimals:
        must_add = True
        nd = '0.'
        decimals[decimals.index('10')] = '9'
        for x in decimals:
            nd += (x)
        nd = str(float(nd) + (1 * 10 ** (-roundDecimals)))

    whole_number = whole_number + ['.']
    final_number = ''
    
    if must_add:
        whole_number_add = nd.split('.', 1)[0]
        whole_number_add = float(whole_number_add)
        nd = list(nd)
        new_decimals = nd[2:]
        decimals = new_decimals[:roundDecimals]
        for x in whole_number:
            final_number += x
        final_number = str(float(final_number) + whole_number_add)
        final_number = final_number.split('.', 1)[0] + '.'
        for x in decimals:
            final_number += x

    else:
        decimals = decimals[:roundDecimals]
        for x in whole_number:
            final_number += x
        for x in decimals:
            final_number += x
    final_number = float(final_number)
    
    if returnClass == 'str':
        return (f"{final_number:.{roundDecimals}f}")
    else:
        return final_number

if __name__ == '__main__':
    from numpy import arange
    deviation = 0
    same = 0
    for i in arange(0, 2, 0.0001):
        rounds = round(i, 2)
        tround = reround(i, returnClass='float', roundDecimals=2)
        equal = True if rounds == tround else False
        if rounds != tround:
            deviation += 1
            print(f'{"Valor":^25}', '|', f'{"Python":^9}', '|', f'{"Função":^9}','|', "Iguais?")
            print(f'{i:^25}', '|', f'{rounds:^9}', '|', f'{tround:^9}','|', equal)
            print()
        if rounds == tround:
            same += 1
    print(f"Different values: {deviation}\nSame values: {same}")