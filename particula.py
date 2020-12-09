from algoritmo import Distancia_euclidiana

class Particula:
    def __init__(self, 
                id=0, origen_x=0, 
                origen_y=0, destino_x=0, destino_y=0,
                velocidad=0, red=0, green=0, blue=0, distancia=0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = Distancia_euclidiana(10, 20, 30, 40)
            
    def __str__(self):
        return (
            'id: ' + str(self.__id) + '\n' +
            'origen_x: ' + str(self.__origen_x) + '\n' +
            'origen_y: ' + str(self.__origen_y) + '\n' +
            'destino_x: ' + str(self.__destino_x) + '\n' + 
            'destino_y: ' + str(self.__destino_y) + '\n' +
            'velocidad: ' + str(self.__velocidad) + '\n' +
            'red: ' + str(self.__red) + '\n' +
            'green: ' + str(self.__green) + '\n' +
            'blue: ' + str(self.__blue) + '\n' +
            'distancia: ' + str(self.__distancia) + '\n'
        )
#l01 = Libro(id=1, origen_x=2, origen_y=3, destino_x=4, destino_y=5, velocidad=6,
#red=7, green=8, blue=9)
#print (l01)
#l02 = Libro("9", "10", "11", "12", "13", "14", "15", "16", "17")
#print (l02)
