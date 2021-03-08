CPF = list(input('Digite um CPF e verifique se ele é VÁLIDO [digite apenas os números]:\n'))
soma1 = soma2 = cont2 = repetido = 0
cont1 = cont = 1
for i in CPF:
    if int(i) == cont:
        repetido += 1
        cont -= 1
    cont += 1
if repetido > 6:
    print('CPF INVÁLIDO')
else:
    if len(CPF) == 11:
        for s1 in CPF[:-2]:
            soma1 = soma1 + (cont1 * int(s1))
            cont1 = cont1 + 1
        for s2 in CPF[:-1]:
            if len(s2) <= 9:
                soma2 = soma2 + (cont2 * int(s2))
                cont2 = cont2 + 1
            else:
                soma2 = soma2 + (cont2 * modDigito1)
                break
        modDigito1 = soma1 % 11
        if modDigito1 > 9:
            modDigito1 = 0
        modDigito2 = soma2 % 11
        if modDigito2 > 9:
            modDigito2 = 0
        print('CPF VÁLIDO' if modDigito1 == int(CPF[9]) and modDigito2 == int(CPF[10]) else 'CPF INVÁLIDO')
    else:
        print('CPF INVÁLIDO')






