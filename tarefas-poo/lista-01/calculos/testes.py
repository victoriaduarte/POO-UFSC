from model.calculos import *

# testando media_de_tres_numeros
try:
    print('\nIniciando teste media_de_tres_numeros...')
    media = media_de_tres_numeros(10,20,30)
    assert media == 20, f'media_de_tres_numeros(10,20,30) deveria retornar 20 mas retornou {media}'
    media = media_de_tres_numeros(10,10,10)
    assert media == 10, f'media_de_tres_numeros(10,10,10) deveria retornar 10 mas retornou {media}'
    media = media_de_tres_numeros(0,0,0)
    assert media == 0, f'media_de_tres_numeros(0,0,0) deveria retornar 0 mas retornou {media}'
    print('media_de_tres_numeros ok')
except Exception as e:
    print(e)
# fim de teste

# testando soma_de_tres_numeros
try:
    print('\nIniciando teste soma_de_tres_numeros...')
    soma = soma_de_tres_numeros(10,20,30)
    assert soma == 60, f'soma_de_tres_numero(10,20,30) deveria retornar 60 mas retornou {soma}'
    soma = soma_de_tres_numeros(0,0,0)
    assert soma == 0, f'soma_de_tres_numero(0,0,0) deveria retornar 0 mas retornou {soma}'
    print('soma_de_tres_numeros ok')
except Exception as e:
    print(e)
# fim de teste

# testando par
try:
    print('\nIniciando teste par...')
    eh_par = par(8)
    assert eh_par == True, f'par(8) deveria retornar True mas retornou {eh_par}'
    eh_par = par(23)
    assert eh_par == False, f'par(23) deveria retornar False mas retornou {eh_par}'
    eh_par = par(0)
    assert eh_par == True, f'par(0) deveria retornar True mas retornou {eh_par}'
    eh_par = par(1)
    assert eh_par == False, f'par(1) deveria retornar False mas retornou {eh_par}'
    print('par ok')
except Exception as e:
    print(e)
# fim de teste

# testando menor_de_tres_numeros
try:
    print('\nIniciando teste menor_de_tres_numeros...')
    menor = menor_de_tres_numeros(5,9,14)
    assert menor == 5, f'menor_de_tres_numeros(5,9,14) deveria retornar 5 mas retornou {menor}'
    menor = menor_de_tres_numeros(20,9,14)
    assert menor == 9, f'menor_de_tres_numeros(20,9,14) deveria retornar 9 mas retornou {menor}'
    menor = menor_de_tres_numeros(14,9,5)
    assert menor == 5, f'menor_de_tres_numeros(14,9,5) deveria retornar 5 mas retornou {menor}'
    menor = menor_de_tres_numeros(8,8,8)
    assert menor == 8, f'menor_de_tres_numeros(8,8,8) deveria retornar 8 mas retornou {menor}'
    menor = menor_de_tres_numeros(0,0,0)
    assert menor == 0, f'menor_de_tres_numeros(0,0,0) deveria retornar 0 mas retornou {menor}'
    menor = menor_de_tres_numeros(0,-5,0)
    assert menor == -5, f'menor_de_tres_numeros(0,-5,0) deveria retornar -5 mas retornou {menor}'
    menor = menor_de_tres_numeros(-10,-5,-23)
    assert menor == -23, f'menor_de_tres_numeros(-10,-5,-23) deveria retornar -23 mas retornou {menor}'
    print('menor_de_tres_numeros ok')
except Exception as e:
    print(e)
# fim de teste

# testando maior_que
try:
    print('\nIniciando teste maior_que...')
    eh_maior = maior_que(15,8)
    assert eh_maior == True, f'maior_que(15,8) deveria retornar True mas retornou {eh_maior}'
    eh_maior = maior_que(4,8)
    assert eh_maior == False, f'maior_que(4,8) deveria retornar False mas retornou {eh_maior}'
    eh_maior = maior_que(8,8)
    assert eh_maior == False, f'maior_que(8,8) deveria retornar False mas retornou {eh_maior}'
    eh_maior = maior_que(-8,8)
    assert eh_maior == False, f'maior_que(-8,8) deveria retornar False mas retornou {eh_maior}'
    eh_maior = maior_que(1,-8)
    assert eh_maior == True, f'maior_que(1,-1) deveria retornar True mas retornou {eh_maior}'
    print('maior_que ok')
except Exception as e:
    print(e)
# fim de teste

# testando divisivel_por
try:
    print('\nIniciando teste divisivel_por...')
    eh_divisivel = divisivel_por(16,8)
    assert eh_divisivel == True, f'divisivel_por(16,8) deveria retornar True mas retornou {eh_divisivel}'
    eh_divisivel = divisivel_por(16,5)
    assert eh_divisivel == False, f'divisivel_por(16,5) deveria retornar False mas retornou {eh_divisivel}'
    eh_divisivel = divisivel_por(16,16)
    assert eh_divisivel == True, f'divisivel_por(16,16) deveria retornar True mas retornou {eh_divisivel}'
    eh_divisivel = divisivel_por(16,16)
    assert eh_divisivel == True, f'divisivel_por(16,16) deveria retornar True mas retornou {eh_divisivel}'
    eh_divisivel = divisivel_por(12,24)
    assert eh_divisivel == False, f'divisivel_por(12,24) deveria retornar False mas retornou {eh_divisivel}'
    print('divisivel_por ok')
except Exception as e:
    print(e)
# fim de teste

# testando multiplica
try:
    print('\nIniciando teste multiplica...')
    produto = multiplica(2,8)
    assert produto == 16, f'multiplica(2,8) deveria retornar 16 mas retornou {produto}'
    produto = multiplica(7,7)
    assert produto == 49, f'multiplica(7,7) deveria retornar 49 mas retornou {produto}'
    produto = multiplica(0,0)
    assert produto == 0, f'multiplica(0,0) deveria retornar 0 mas retornou {produto}'
    produto = multiplica(-8,5)
    assert produto == -40, f'multiplica(-8,5) deveria retornar -40 mas retornou {produto}'
    produto = multiplica(-8,-5)
    assert produto == 40, f'multiplica(-8,-5) deveria retornar 40 mas retornou {produto}'
    print('multiplica ok')
except Exception as e:
    print(e)
# fim de teste

# testando divide
try:
    print('\nIniciando teste divide...')
    divisao = divide(8,2)
    assert divisao == 4, f'divide(8,2) deveria retornar 4 mas retornou {divisao}'
    divisao = divide(8,5)
    assert divisao == 1, f'divide(8,5) deveria retornar 1 mas retornou {divisao}'
    divisao = divide(10,4)
    assert divisao == 2, f'divide(10,4) deveria retornar 2 mas retornou {divisao}'
    print('divide ok')
except Exception as e:
    print(e)
# fim de teste

# testando bissexto
try:
    print('\nIniciando teste bissexto...')
    eh_bissexto = bissexto(1948)
    assert eh_bissexto == True, f'bissexto(1948) deveria retornar True mas retornou {eh_bissexto}'
    eh_bissexto = bissexto(2024)
    assert eh_bissexto == True, f'bissexto(2024) deveria retornar True mas retornou {eh_bissexto}'
    eh_bissexto = bissexto(2021)
    assert eh_bissexto == False, f'bissexto(2021) deveria retornar False mas retornou {eh_bissexto}'
    print('bissexto ok')
except Exception as e:
    print(e)
# fim de teste

# testando mdc
try:
    print('\nIniciando teste mdc...')
    maior_div_comum = mdc(8,7)
    assert maior_div_comum == 1, f'mdc(8,7) deveria retornar 1 mas retornou {maior_div_comum}'
    maior_div_comum = mdc(9,12)
    assert maior_div_comum == 3, f'mdc(9,12) deveria retornar 3 mas retornou {maior_div_comum}'
    maior_div_comum = mdc(12,9)
    assert maior_div_comum == 3, f'mdc(12,9) deveria retornar 3 mas retornou {maior_div_comum}'
    print('mdc ok')
except Exception as e:
    print(e)
# fim de teste

# testando soma_dos_divisores
try:
    print('\nIniciando teste soma_dos_divisores...')
    soma = soma_dos_divisores(2)
    assert soma == 3, f'soma_dos_divisores(2) deveria retornar 3 mas retornou {soma}'
    soma = soma_dos_divisores(25)
    assert soma == 31, f'soma_dos_divisores(25) deveria retornar 31 mas retornou {soma}'
    soma = soma_dos_divisores(36)
    assert soma == 91, f'soma_dos_divisores(36) deveria retornar 91 mas retornou {soma}'
    print('soma_dos_divisores ok')
except Exception as e:
    print(e)
# fim de teste

# testando amigos
try:
    print('\nIniciando teste amigos...')
    sao_amigos = amigos(284,220)
    assert sao_amigos == True, f'amigos(284,220) deveria retornar True mas retornou {sao_amigos}'
    sao_amigos = amigos(1184,1210)
    assert sao_amigos == True, f'amigos(1184,1210) deveria retornar True mas retornou {sao_amigos}'
    sao_amigos = amigos(100,200)
    assert sao_amigos == False, f'amigos(100,200) deveria retornar False mas retornou {sao_amigos}'
    print('amigos ok')
except Exception as e:
    print(e)
# fim de teste

# testando primo
try:
    print('\nIniciando teste primo...')
    eh_primo = primo(2)
    assert eh_primo == True, f'primo(2) deveria retornar True mas retornou {eh_primo}'
    eh_primo = primo(11)
    assert eh_primo == True, f'primo(11) deveria retornar True mas retornou {eh_primo}'
    eh_primo = primo(4)
    assert eh_primo == False, f'primo(4) deveria retornar False mas retornou {eh_primo}'
    print('primo ok')
except Exception as e:
    print(e)
# fim de teste

# testando composto
try:
    print('\nIniciando teste composto...')
    eh_composto = composto(2)
    assert eh_composto == False, f'composto(2) deveria retornar False mas retornou {eh_composto}'
    eh_composto = composto(11)
    assert eh_composto == False, f'composto(11) deveria retornar False mas retornou {eh_composto}'
    eh_composto = composto(4)
    assert eh_composto == True, f'composto(4) deveria retornar True mas retornou {eh_composto}'
    print('composto ok')
except Exception as e:
    print(e)
# fim de teste