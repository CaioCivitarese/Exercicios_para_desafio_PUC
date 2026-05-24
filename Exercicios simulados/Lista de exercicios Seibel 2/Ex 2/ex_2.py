# 2) Dado um triângulo retângulo a, b e c onde a é a hipotenusa e os catetos medem 3 e 4, calcule o valor de:
#     ◦ a 
#     ◦ seno de a 
#     ◦ coseno de a 
#     ◦ tangente de a
#     ◦ o perímetro do triângulo
#     ◦ a área do triângulo
# Obs: Use o módulo math para calcular as funções trigonométricas.
import math

b = 3
c = 4

a = math.hypot(b, c)
sen = math.sin(a)
cos = math.cos(a)
tan = math.tan(a)
peri = a + b + c
aria = (b + c) / 2

print('A hipotenusa e: {}, o seno de a é: , já o coseno e: {}, e a tangente é: {}, o perimetro é: {}, e a aria é: {}'.format(a, sen, cos, tan, peri, aria))