import random 

def imprimir(resultados): #recibe la lista generada por lanzarMonedas()    
    print("RESULTADOS:")
    i=0
    for par in resultados:
        i=i+1
        print("SIMULACION " + str(i) +": " + str(par[0]) + " " + str (par[1]))

def lanzarMonedas(veces):
    resultados = [] # esta lista se utiliza para guardar los pares de lanzamientos de monedas (cada simulacion) 

    for i in range (veces): #numero de simulaciones que seran realiadas

        par = [] # Almacena el par de resultados.

        for i in range (2): # Lanza las monedas
            moneda = random.randint(0,1) 
            if (moneda == 0):
                par.append("Cara")
            else:
                par.append("Sello")

        resultados.append(par) #añade el par a la lista de resultados                 

    imprimir(resultados) 

if __name__ == '__main__':
    lanzarMonedas(10)
    pass