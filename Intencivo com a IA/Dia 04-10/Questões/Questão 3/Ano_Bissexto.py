# ano bissexto e divisivel por 4
# exceto os anos divisiveis por 100 e por 400

N = int(input())

if N % 4 == 0 and (N % 100 != 0) or (N % 100 == 0) and (N % 400 == 0):
    print("SIM")
else:
    print("NAO")