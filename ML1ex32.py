"""
32. O seno de um ângulo em radianos, no intervalo de 0 à
2

pode ser calculado através

da série de McLaurin, apresentada a seguir: senx = x/1! - x³/3! + ...

a. Escreva uma função que converta um ângulo em graus para seu valor em
radianos (180 =  rad)

b. Escreva uma função que receba como parâmetro um ângulo em graus, a
precisão requerida para o cálculo e retorne o seu seno, utilizando a função de
conversão graus-radiano feita anteriormente

c. Faça um programa que teste a sua função para cálculo do seno.
"""
from ex33 import calcular_pi
def factorial(n):
     if n == 1:
          return 1
     return n * factorial(n-1)
def graus_para_rad(angulo):
    return angulo * calcular_pi(1000) / 180.0

def calcular_seno(angulo, precisao):
    angulo_rad = graus_para_rad(float(angulo))
    seno = 0.0
    sinal = 1
    for i in range(1, precisao, 2):
            seno += (pow(angulo_rad, i) / factorial(i)) * sinal 
            sinal *= -1
    return seno

def main():
    angulo = 60
    print(graus_para_rad(angulo))
    print(calcular_seno(angulo, 50))
    print(factorial(5))
main()
