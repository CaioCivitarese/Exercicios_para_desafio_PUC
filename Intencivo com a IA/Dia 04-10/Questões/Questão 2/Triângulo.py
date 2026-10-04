# triengolo equilatero == 3 lados iguais
# triangolo isosceles == 2 lados iguais 
# triengulo escaleno == 3 lados diferentes

A = int(input())
B = int(input())
C = int(input())

if A == B and A == C:
    print("equilatero")
elif (A == B or A == C or B == C) and ((A + B) > C and ( A + C ) > B and ( C + B ) > A):
    print("isosceles")
elif (A + B) > C and ( A + C ) > B and ( C + B ) > A:
    print("escaleno")
else:
    print("invalido")
