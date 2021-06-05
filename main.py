#Fecha creación 03/06/2021 a las 11:53
#Por Esteban Cruz López

#Variable fundamental del método de clasificación
K=3

#Variable global para manejar la colección de entrenamiento
trainingSet=[]
testSet=[]

#Estructura de dato de cada entrada de la colección
class Documento:
    def __init__(self,docId,clase,numTerminos,pesosXTermino):
        self.docId=docId
        self.clase=clase
        self.numTerminos=numTerminos
        self.pesosXTermino=dict([par.split("/")for par in pesosXTermino.split(" ")])
        

#Se llena la lista de la colección con los documentos extraídos de training-set.csv
with open ("training-set.csv")as trainingDoc:
    trainingSet=[Documento(*linea.split("\t")) for linea in trainingDoc.readlines()]

#Se abre el archivo de la colección de prueba y por cada entrada se ejecuta el algoritmo de clasificación    
with open ("test-set.csv") as testDoc:
    testSet=[Documento(*linea.split("\t")) for linea in trainingDoc.readlines()]

def realizarConsulta(testDoc):
    similitudes={}
    for trainingDoc in trainingSet:
        similitudes[trainingDoc]=0
        for termino,peso in testDoc.pesosXTermino.items():
            if termino in trainingDoc.pesosXTermino:
                similitudes[trainingDoc]+=peso*trainingDoc.pesosXTermino[termino]
    #Se crea el escalafón y se ordena de manera descendente
    escalafon=similitudes.items()
    escalafon.sort(lambda x,y:x[1]>y[1])
    return escalafon

for testDoc in testSet:
    #Se obtiene el escalafón
    escalafon=realizarConsulta(testDoc)
    
    #Se analizan los K más relevantes
    for doc,sim in escalafon[:K]:
        #Escoger la clase para testDoc
#Hacer el análisis de resultados