import random 

def lanzarMonedas(veces):
    resultados = [] # esta lista se utiliza para guardar los pares de lanzamientos de monedas (cada simulacion) 

    for i in range (veces): #numero de simulaciones que seran realiadas

        par = [] # Almacena el par de resultados.

        for i in range (2): # Lanza las monedas
            moneda = random.randint(0,1) 
            if (moneda == 0):
                par.append("cara")
            else:
                par.append("sello")

        resultados.append(par) #añade el par a la lista de resultados                 

    return (resultados) #devuelve la lista

if __name__ =='__main__':
    resultados = lanzarMonedas(10)
    print( str(resultados))