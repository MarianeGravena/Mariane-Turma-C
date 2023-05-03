def pede_metros():
    return float(input('Digite o valor em metros'))

def metros_para_centimetros(m):
    cm = m * 100
    return cm

def informa_cm(cm):
    print(f'{cm}cm')

def exercicio1():
    metros = pede_metros()
    cm = metros_para_centimetros(metros)
    informa_cm(cm)







def pede_horas():
    return float(input('Digite o valor em horas: '))

def horas_trabalhadas():
    return float(input('Informe a quantidade de horas trabalhadas no mês: '))

def calculo_salario(a, b):
    return a * b

def informa_salario(c):
    print(f'{c}reais')



def exercicio2():
    valor_hora = pede_horas()
    horas_mes = horas_trabalhadas()
    calculo = calculo_salario(valor_hora, horas_mes)
    informa_salario(calculo)




def pede_fahrenheit():
    return float(input('Informe uma temperatura em Fahrenheit: '))

def conversao_para_celsius(f):
    return 5 * ((f - 32) / 9)

def informa_celsius(celsius):
    print(f'{celsius} graus celsius.')


def exercicio3():

    fahrenheit = pede_fahrenheit()
    tempcelsius = conversao_para_celsius(fahrenheit)
    informa_celsius(tempcelsius)




def pede_altura():
    return float(input("Informe sua altura: "))

def pede_peso():
    return float(input("Informe seu peso: "))

def calcular_imc(a, p):
    return p / (a ** 2)

def informa_imc(imc):
    print(f"Seu IMC é: {imc}")


def exercicio4():
    altura = pede_altura()
    peso = pede_peso()
    calculo_imc = calcular_imc(altura, peso)
    informa_imc(calculo_imc)
    







def exercicio5():

    peso_dos_peixes = float(input("Digite o peso dos peixes em kgs: "))
    limite = 30
    excesso = peso_dos_peixes - limite

    if excesso > 0:
        multa_por_kg = 3
        multa = excesso * multa_por_kg
    else:
        multa = 0
    print(f"Peso dos peixes: {peso_dos_peixes:.2f} kg")
    if excesso > 0:
        print(f"Peso excedido: {excesso:.2f} kg")
    if multa > 0:
        print(f"Valor da multa a ser pago será de: R$ {multa:.2f}")


def exercicio6():

    ganho_hora = float(input("Informe o valor que você ganha por hora: "))
    hora_mes = float(input("Informe quantas horas você trabalhou no mês: "))

    salario_bruto = ganho_hora * hora_mes
    imposto_renda = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    salario_liquido = (salario_bruto - imposto_renda) - inss

    print(f"O valor do seu salário bruto será de R${salario_bruto}.")
    print(f"O valor do imposto de renda será de R${imposto_renda}. ")
    print(f"O valor do INSS será de R${inss}")
    print(f"O seu salário no mês com os descontos será de R${salario_liquido}: ")



def exercicio7():

    import math
    area_pintada = float(input("Informe o tamanho em metros quadrados da área a ser pintada: "))

    litros_tinta = area_pintada / 3

    latas_tintas = math.ceil(litros_tinta / 18)

    valor_latas = latas_tintas * 80

    print(f"A quantidade de latas a serem compradas será de: {latas_tintas}. ")
    print(f"O preço total será de: R${valor_latas}. ")

