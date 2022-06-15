import labshortcut as lab
debug = int(input("Qual script? \n1 - Labshortcut \n2 - Tests\n> "))
if debug == 1:
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
                input_numbers = input_numbers.replace(',', '.')
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

        trueValue = float(trueValue) if isinstance(trueValue, float) else 0
                
        all_values = {"numbers": number_list, "round": do_round, "roundDecimal": round_value}
        lab.fprint(f'\nA média é = {lab.mean(*all_values.values())}')
        lab.fprint(f'O desvio padrão amostral é = {lab.ssd(*all_values.values())}')
        lab.fprint(f'O desvio padrão populacional é = {lab.psd(*all_values.values())}')
        lab.fprint(f'O desvio padrão relativo é = {lab.rsd(*all_values.values())}')
        lab.fprint(f'O coeficiente de variação é = {lab.cv(*all_values.values())}%\n')
        if trueValue != 0:
            all_values = {"numbers": number_list, 'trueValue': trueValue, "round": do_round, "roundDecimal": round_value}
            lab.fprint(f'O erro absoluto é = {lab.aerr(*all_values.values())}')
            lab.fprint(f'O erro relativo é = {lab.rerr(*all_values.values())}%\n')

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