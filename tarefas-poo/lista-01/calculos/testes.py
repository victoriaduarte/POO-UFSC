from model.calculos import soma_de_tres_numeros

try:
    print('\ntestando soma_de_tres_numeros...')
    soma = soma_de_tres_numeros(10,20,30)
    assert soma == 60, f'soma_de_tres_numero(10,20,30) deveria retornar 60 mas retornou {soma}'
        soma = soma_de_tres_numeros(0,0,0)
    assert soma == 60, f'soma_de_tres_numero(0,0,0) deveria retornar 0 mas retornou {soma}'
    print('soma_de_tres_numeros ok')
except Exception as e:
    print(e)