import random 

def lanzarMonedas(veces):
    posiblesResultados = ("Cara Cara", "Cara Sello", "Sello Cara", "Sello Sello") # 4 posibilidades 
    for i in range (veces):
        resultado = random.randint(0,3) 
        print ("SIMULACION "+ str(i+1) +": " + posiblesResultados[resultado])

if __name__ == '__main__':
    lanzarMonedas(20)
    pass