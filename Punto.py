class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def Impresion(self):
        print("el punto se encuentra en la coordenada x={0} coordenada y={1}".format( str(self.x), str(self.y)))

    def Opuesto(self):
        return "el punto se encuentra en la coordenada x={0} coordenada y={1}".format( str(self.x*-1), str(self.y*-1))

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def set_x(self, x):
        self.x=x
    def set_y(self, y):
        self.y=y

a= Punto(2,4)

a.Impresion()

print()
print(a.Opuesto())
        

