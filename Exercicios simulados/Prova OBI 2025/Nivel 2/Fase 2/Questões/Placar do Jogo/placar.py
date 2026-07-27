# PG = Paila Gols
# CG = Camila Gols
# PM = Paula minutos
# GM = Camila minutos

PM = 0
GM = 0
NGP = 0
NGC = 0
NP = 0
NC = 0
Pm = []
Cm = []

PG = int(input('Quantos gols Paula fez: '))

for i in range(PG):
    PM = int(input('Quais os monentos que Paula marcou: '))
    Pm.append(PM)

CG = int(input('Quantos gols Camila fez: '))

for i in range(CG):
    CM = int(input('Qual os momentos que Camila marcou: '))
    Cm.append(CM)

TotalDeGols = PG + CG

for i in range(TotalDeGols):
    if Pm[NP] > Cm[NC]:
        NC += 1
        NGC += 1
        print(NGP, ' X ', NGC);
    else:
        NP += 1
        NGP += 1
        print(NGP, ' X ', NGC)


# # PG = Paula Gols
# # CG = Camila Gols

# NGP = 0
# NGC = 0
# NP = 0
# NC = 0

# Pm = []
# Cm = []

# PG = int(input('Quantos gols Paula fez: '))

# for i in range(PG):
#     PM = int(input('Qual momento Paula marcou: '))
#     Pm.append(PM)


# CG = int(input('Quantos gols Camila fez: '))

# for i in range(CG):
#     CM = int(input('Qual momento Camila marcou: '))
#     Cm.append(CM)


# TotalDeGols = PG + CG


# for i in range(TotalDeGols):

#     if NP < PG and NC < CG:

#         if Pm[NP] < Cm[NC]:
#             NP += 1
#             NGP += 1

#         else:
#             NC += 1
#             NGC += 1

#     elif NP < PG:
#         NP += 1
#         NGP += 1

#     else:
#         NC += 1
#         NGC += 1


#     print(NGP, "X", NGC)# PG = Paula Gols
# # CG = Camila Gols

# NGP = 0
# NGC = 0
# NP = 0
# NC = 0

# Pm = []
# Cm = []

# PG = int(input('Quantos gols Paula fez: '))

# for i in range(PG):
#     PM = int(input('Qual momento Paula marcou: '))
#     Pm.append(PM)


# CG = int(input('Quantos gols Camila fez: '))

# for i in range(CG):
#     CM = int(input('Qual momento Camila marcou: '))
#     Cm.append(CM)


# TotalDeGols = PG + CG


# for i in range(TotalDeGols):

#     if NP < PG and NC < CG:

#         if Pm[NP] < Cm[NC]:
#             NP += 1
#             NGP += 1

#         else:
#             NC += 1
#             NGC += 1

#     elif NP < PG:
#         NP += 1
#         NGP += 1

#     else:
#         NC += 1
#         NGC += 1


#     print(NGP, "X", NGC)
