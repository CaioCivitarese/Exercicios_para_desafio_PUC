a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))

delta = b**2 - 4 * a * c
if delta < 0:
    print('Não tem raiz')
elif delta == 0:
    raiz = -b / (a * 2)
    print('Tem uma raiz x = ',raiz)
else:
    raiz1 = (-b + delta**(1/2)) / (a * 2)
    raiz2 = (-b - delta**(1/2)) / (a * 2)
    print('Tem duas raízes x1 =', raiz1,' x2 = ', raiz2)
