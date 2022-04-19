from punto import Punto

class Linea:
    def __init__(self, puntoA, puntoB):
        self.pA=puntoA
        self.pB=puntoB
        
    def mueve_izquerda(self, unidades):
        self.pA.set_x(self.pA.get_x()-unidades)
        self.pB.set_x(self.pB.get_x()-unidades)

    def mueve_derecha(self, unidades):
        self.pA.set_x(self.pA.get_x()+unidades)
        self.pB.set_x(self.pB.get_x()+unidades)

    def mueve_arriba(self, unidades):
        self.pA.set_y(self.pA.get_y()+unidades)
        self.pB.set_y(self.pB.get_y()+unidades)

    def mueve_abajo(self, unidades):
        self.pA.set_y(self.pA.get_y()-unidades)
        self.pB.set_y(self.pB.get_y()-unidades)
        

    def mostrar_linea(self):
        print(" La linea se encuentra en la posiscion PA ({0};{1})  PB ({2};{3}) ".format(str(self.pA.get_x()),str(self.pA.get_y()),str(self.pB.get_x()),str(self.pB.get_y())))

puntA= Punto(2,4)
puntB= Punto(6,8)

nueva_linea= Linea(puntA, puntB)

nueva_linea.mostrar_linea()

nueva_linea.mueve_derecha(2)

print("---------------")
nueva_linea.mostrar_linea()
print("-------------")
nueva_linea.mueve_arriba(2)
nueva_linea.mostrar_linea()