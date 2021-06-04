#Fecha creación 03/06/2021 a las 11:53
#Por Esteban Cruz López

#Variable global para manejar la colección de entrenamiento
trainingSet=[]
testSet=[]

#Estructura de dato de cada entrada de la colección
class Documento:
    def __init__(self,docId,clase,numTerminos,pesosXTermino):
        self.docId=docId
        self.clase=clase
        self.numTerminos=numTerminos
        self.pesosXTermino=generarMapaPesosXTermino(pesosXTermino)

#Función para generar un mapa de los pesos por termino presentes en los documentos
def generarMapaPesosXTermino(pesosXTermino):
    return dict([par.split("/")for par in pesosXTermino.split(" ")])

#Se llena la lista de la colección con los documentos extraídos de training-set.csv
with open ("training-set.csv")as trainingDoc:
    trainingSet=[Documento(*linea.split("\t")) for linea in trainingDoc.readlines()]

#Se abre el archivo de la colección de prueba y por cada entrada se ejecuta el algoritmo de clasificación    
with open ("test-set.csv") as testDoc:
    testSet=[Documento(*linea.split("\t")) for linea in trainingDoc.readlines()]

for testDoc in testSet:
    #Ejecutar como consulta el testDoc en el set de entrenamiento
    #Sacar el escalafón
    #Escoger los k más relevantes
    #Promediar las calificaciones por clase 
    #Asignar al testDoc, la clase con mejor promedio