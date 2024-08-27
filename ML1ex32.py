"""
32. O seno de um ângulo em radianos, no intervalo de 0 à
2

pode ser calculado através

da série de McLaurin, apresentada a seguir:

= − + − +
1! 3! 5! 7!
sen

3 5 7
x x x x
x

a. Escreva uma função que converta um ângulo em graus para seu valor em
radianos (180 =  rad)

b. Escreva uma função que receba como parâmetro um ângulo em graus, a
precisão requerida para o cálculo e retorne o seu seno, utilizando a função de
conversão graus-radiano feita anteriormente

c. Faça um programa que teste a sua função para cálculo do seno.
"""
from math import pi, factorial
def graus_para_rad(angulo):
    return angulo * pi / 180.0

def calcular_seno(angulo, acc):
    angulo_rad = graus_para_rad(float(angulo))
    seno = 0.0
    divisor = 1
    for i in range(acc):
        if i % 2 == 0:
            seno += pow(angulo_rad, divisor) / factorial(divisor) 
            divisor += 2  
        else:
            seno -= pow(angulo_rad, divisor) / factorial(divisor)
            divisor += 2
        
        
    
    return seno

def main():
    angulo = 60
    print(graus_para_rad(angulo))
    print(calcular_seno(angulo, 50))
main()