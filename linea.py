from Punto import Punto

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
        

    def mostrar_recta(self):
        m=(self.pB.get_x()-self.pA.get_x()) / (self.pB.get_y()-self.pA.get_y())
        b=m*self.pA.x-self.pA.y
        
        filas = 31
        columnas= 31
        matriz=[]

        for i in range(filas):
            matriz.append([' '])
            for j in range(columnas):
                matriz[i].append(' ')

        
        for i in range(31):
            y=int(((m*i)+b))
            matriz[y][i]='O'
    
        for i in range(30,0,-1):
            print(matriz[i])
    
puntA= Punto(2,2)
puntB= Punto(4,4)

nueva_linea= Linea(puntA, puntB)

nueva_linea.mostrar_linea()

#nueva_linea.mueve_derecha(2)

print("---------------")
nueva_linea.mostrar_linea()
print("-------------")
#nueva_linea.mueve_arriba(2)
nueva_linea.mostrar_linea()

nueva_linea.mostrar_recta()
