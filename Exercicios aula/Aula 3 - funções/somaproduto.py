def soma (a,b):
    return a+b
def produto(x,y):
    return(x*y)
def somaprod(w,z):
    s=soma(w,z)
    p=produto(w,z)
    return(s,p)
i=5
j=10
k=0
l=0
(k,l)=somaprod(i,j)
print(k,l)
