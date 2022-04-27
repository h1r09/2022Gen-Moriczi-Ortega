from array import array
import secrets
class individuo:
#atributos de cada individuo de la poblacion de la generacion actual
 
    #Declaro una lista de genes de tamaño 10 con valores entre 0 y 1
    genes = []
   

    #bucle para rellenar la lista de genes con valores 0 o 1
    # Se hace uso de secret() para generar un numero aleatorio entre 0 y 1 
    # ya que segun sonarcloud no se puede usar random.randint por seguridad

    def rellenarGenes(self):
        for i in range(10): 
            random = secrets.randbelow(2)
            self.genes.append(random)
        

    #constructor
    def __init__(self, genes):
        self.genes = genes
        
#Metodo para cruzar 2 individuos y devolver un nuevo individuo con los genes de los padres cruzados indicando el punto de cruce 
    def cruzarPunto(self, individuo2, punto):
        #Declaro una lista de genes de tamaño 10 con valores entre 0 y 1
        genesCruza = []
        #bucle para rellenar la lista de genes con valores 0 o 1
        print("Punto de cruce: " + str(punto))
        for i in range(10): 
            if i < punto:
                genesCruza.append(self.genes[i])
            else:
                genesCruza.append(individuo2.genes[i])
        #Creo un nuevo individuo con los genes de los padres cruzados
        individuoCruza = individuo(genesCruza)
        return individuoCruza


#Metodo para cruzar 2 individuos y devolver un nuevo individuo con los genes de los padres cruzados 
    def cruzar(self, individuo2):
        #Declaro una lista de genes de tamaño 10 con valores entre 0 y 1
        genesCruza = []
        #bucle para rellenar la lista de genes con valores 0 o 1
        for i in range(10): 
            random = secrets.randbelow(2)
            if random == 0:
                genesCruza.append(self.genes[i])
            else:
                genesCruza.append(individuo2.genes[i])
        #Creo un nuevo individuo con los genes de los padres cruzados
        individuoCruza = individuo(genesCruza)
        return individuoCruza


#Metodo para mutar un individuo y devolver un nuevo individuo con uno de los genes mutados pasando una probabilidad
    def mutar(self, probabilidad):
        #Declaro una lista de genes de tamaño 10 con valores entre 0 y 1
        genesMutacion = []
        #bucle para rellenar la lista de genes con valores 0 o 1
        for i in range(10): 
            random = secrets.randbelow(2)
            if random <= probabilidad:
                #Descoemtar siguiente linea para imprimir el gen mutado
                # print("Gen mutado: " + str(i))
                if self.genes[i] == 0:
                    genesMutacion.append(1)
                else:
                    genesMutacion.append(0)
            else:
                genesMutacion.append(self.genes[i])
        #Creo un nuevo individuo con los genes de los padres cruzados
        individuoMutacion = individuo(genesMutacion)
        return individuoMutacion
    

#creo un individuo con los genes aleatorios generados y lo imprimo
# individuo1 = individuo([])
# individuo1.rellenarGenes()
# print(individuo1.genes)

# individuo2 = individuo([])
# individuo2.rellenarGenes()
# print(individuo2.genes)

# puntoCruce = secrets.randbelow(10)
# individuoCruzado2 = individuo1.cruzarPunto(individuo2, puntoCruce)
# print(individuoCruzado2.genes)

# individuoMutado = individuo1.mutar(0.2)

# print(individuoMutado.genes)

