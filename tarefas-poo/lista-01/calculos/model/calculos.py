# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Definição das funções que realizam cálculos diversos.


def media_de_tres_numeros(n1, n2, n3):
    """Calcula a média de três números.
    """ 
    return (n1 + n2 + n3)/3


def soma_de_tres_numeros(n1, n2, n3):
    """Calcula a soma de três números.
    """
    return n1 + n2 + n3


def par(n):
    """Verifica se um número é par.

    Retorna True se for par ou False caso contrário.
    Dica: a expressão 5 % 3 vale 2 pois 2 é o resto da divisão de 5 por 3.
    """
    return n % 2 == 0


def menor_de_tres_numeros(n1, n2, n3):
    """Encontra o menor de três números.
    """
    menor = n1 if n1 < n2 else n2
    return n3 if n3 < menor else menor


def maior_que(n1, n2):
    """Verifica se o primeiro número é maior que segundo número.

    Retorna True se n1 for maior que n2 ou False caso contrário.
    """
    return n1 > n2
    

def divisivel_por(n1, n2):
    """Verifica se o primeiro número é divisível pelo segundo número.

    Retorna True se n1 for divisível por n2 ou False caso contrário.
    Observação: considera que n1 sempre é maior ou igual a zero e que
    n2 sempre é maior que zero.
    """
    return n1 % n2 == 0 
    

def multiplica(n1, n2):
    """Multiplica dois números maiores ou iguais a zero.

    Atenção: seu algoritmo não pode usar o símbolo '*'.
    """        
    produto = 0
    for i in range(abs(n2)):
        produto += n1 
    if n1 and n2 < 0:
        produto *= -1
    return produto


def divide(n1, n2):
    """Faz a divisão inteira do primeiro número pelo segundo número.

    Retorna o resultado da divisão inteira de n1 por n2.
    Exemplo: divide(8,5) retorna 1. O mesmo que 8 // 5.
    Considera que n1 sempre será maior ou igual a zero e que n2
    sempre será maior que zero.
    Atenção: seu algoritmo não pode usar o símbolo '//'.
    """
    divisao = 0
    while n1 >= n2:
        n1 -= n2
        divisao += 1
    return divisao


def bissexto(ano):
    """Verifica se um ano é bissexto.

    Retorna True se ano for bissexto ou False caso contrário.
    Definição de ano bissexto:
    Um ano é bissexto se for divisível por 400 ou então
    se for divisível por 4 e, ao mesmo tempo, não for divisível por 100.
    """
    return ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0
    

def mdc(n1, n2):
    """Calcula o Máximo Divisor Comum entre dois números inteiros positivos.

    Dica: Utilize o Método das Divisões Sucessivas. Veja o método em
    http://www.mundoeducacao.com/matematica/mdc-divisoes-sucessivas.htm
    """

    # Garantir que n1 sempre será maior que n2
    num = 0
    if n1 < n2:
        n1, n2 = n2, n1

    resto = n1 % n2
    while resto != 0:
        n1 = n2
        n2 = resto
        resto = n1 % n2
    return n2


def soma_dos_divisores(n):
    """Calcula a soma dos divisores de um número inteiro maior que zero.

    Dica: a metade de n é n // 2.
    """
    soma_div = 0
    for i in range(1,n+1):
        if n % i == 0:
            soma_div += i
    return soma_div


def amigos(n1, n2):
    """Verifica se dois números inteiros positivos são amigos.

    Retorna True se números são amigos ou False caso contrário.
    Dica: Números Amigos: http://www.matematica.br/historia/namigos.html
    """
    divisores = 0
    antecessor = n1 - 1
    while antecessor != 0:
        if n1 % antecessor == 0:
            divisores += antecessor
        else:
            divisores += 0
        antecessor -= 1

    divisores_2 = 0
    antecessor_2 = n2 - 1
    while antecessor_2 != 0:
        if n2 % antecessor_2 == 0:
            divisores_2 += antecessor_2
        else:
            divisores_2 += 0
        antecessor_2 -= 1
    
    if divisores == n2 and divisores_2 == n1:
        return True
    else:
        return False

def primo(n):
    """Verifica se número é primo.
    
    Considera que n sempre é maior que 1.
    Retorna True se n for primo ou False caso contrário.
    """
    if n % 2 == 0 and n != 2:
        return False
    elif n % 3 == 0 and n != 3:
        return False
    else:
        return True


def composto(n):
    """Verifica se um número é composto.

    Considera que n sempre é maior que 1.
    Retorna True se n for número composto ou False caso contrário.
    Definição: um número é composto se possui mais de dois divisores.
    """
    if n % 2 == 0 and n != 2:
        return True
    elif n % 3 == 0 and n != 3:
        return True
    else:
        return False


