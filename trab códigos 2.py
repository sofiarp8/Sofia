def soma(a,b):
    return a + b

def quadrado(a):
    return a**2

def hipotenusa(cat1, cat2):
    return soma (quadrado(cat1), quadrado(cat2)) ** (1/2)

def simples(cor):
    if(cor) == 'azul':
        return 'Escolheu bem'
    if(cor) == 'verde':
        return 'Cor de viado'
    
def medio(cor):
    if cor == 'marrom':
        return 'cor de cocô'
    else:
        return 'berimbal no necrotério'
    
contador = 0
while contador < 10:
    print (contador)
    contador += 1
    
for i in range(10):
    print(i)
    
def triangulo(x):
    for i in range (x):
        print ((i + 1) * "*")
        
        
    

    
    
    