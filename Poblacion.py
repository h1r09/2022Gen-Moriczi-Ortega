#Declaro una lista de individuos
import secrets
import Individuo

poblacion = []
#Declaro una lista de individuos que se van a cruzar y mutar
poblacionCruzaMutacion = []


#metodo para rellenar la lista poblacion con x individuos
def rellenar_poblacion(x):
    for i in range(x):
        #Declaro una lista de genes de tamaño 10 con valores entre 0 y 1
        genes = []
        #bucle para rellenar la lista de genes con valores 0 o 1
        for i in range(10): 
            random = secrets.randbelow(2)
            genes.append(random)
        #Creo un nuevo individuo con los genes de los padres cruzados
        individuo = Individuo.individuo(genes)
        poblacion.append(individuo)

#creo una funcion para mostrar la poblacion
def mostrar_poblacion(listaIndividuos):
    for individuo in listaIndividuos:
        print(individuo.genes)  

#metodo que devuelve una lista con los individuos cruzados pasando una lista de individuos ademas 
# de una probabilidad de mutacion pasada por parametro
def cruzar_mutar_individuos(listaIndividuos, probabilidad):
    punto = secrets.randbelow(10)
    listaCruzaMutacion = []
    if probabilidad < 0.5:
        print("Ha habido mutación en la poblacion ")
    for individuo in listaIndividuos:
        random = secrets.randbelow(len(listaIndividuos))
        individuoCruza = individuo.cruzar_punto(listaIndividuos[random], punto)
        if probabilidad < 0.5:
            individuoMutacion = individuoCruza.mutar(probabilidad)
            listaCruzaMutacion.append(individuoMutacion)
        else:
            listaCruzaMutacion.append(individuoCruza)
    return listaCruzaMutacion


#Pruebo el metodo de cruzarMutarIndividuos, generando una poblacion inicial de individuos.
#Luego genero una lista con los individuos cruzados y mutados aleatoriamente
#muestro la poblacion inicial y la poblacion cruzada y mutada
rellenar_poblacion(10)
random = secrets.randbelow(2)


print("Población inicial:")
mostrar_poblacion(poblacion)
print("\n")
poblacionCruzaMutacion = cruzar_mutar_individuos(poblacion,random)
print("Población cruzada y mutada: ")
mostrar_poblacion(poblacionCruzaMutacion)




