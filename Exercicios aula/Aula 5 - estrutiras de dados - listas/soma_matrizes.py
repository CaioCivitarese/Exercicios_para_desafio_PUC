def soma_matrizes(m1,m2,d1,d2):
    temp=[[0,0,0],[0,0,0]]
    i=0
    while i<d1:
        j=0
        while j<d2:
            # atualização de sublistas
            temp[i][j]=m1[i][j]+m2[i][j]  
            j+=1
        i+=1
    return temp

matriz1=[[1,2,3],[4,5,6]]
matriz2=[[6,5,4],[3,2,1]]
dimensao1=2
dimensao2=3
resultado=soma_matrizes(matriz1,matriz2,dimensao1,dimensao2)
print('resultado =', resultado)
    

    


