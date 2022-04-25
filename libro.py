'''Ejercicio 5:
Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre 
cada libro: título, autor (usa la clase Persona), ISBN, páginas, edición, editorial ,
 lugar (ciudad y país) y fecha de edición (como texto). 
 La clase debe proporcionar los siguientes servicios: 
 getters y setters, método para leer la información y método para mostrar la información. 
Este último método mostrará la información del libro con este formato: 
'''
from persona import Persona
class Libro:

    def __init__(self, titulo, autor,ISBN, paginas, edicion, editorial, ciudad, pais, fecha_edicion):
        self.titulo=titulo
        self.autor=autor
        self.ISBN=ISBN
        self.paginas=paginas
        self.edicion=edicion
        self.editorial=editorial
        self.ciudad=ciudad
        self.pais=pais
        self.fecha_edicion=fecha_edicion

    
        
        
    def get_titulo(self):
        return self.titulo
    def set_titulo(self, nuevo_titulo):
        self.titulo=nuevo_titulo
    
    def get_autor_objeto(self):
        return self.autor
    def get_autor_descripcion(self):
        return "Autor: "+self.autor.get_nombre()+ " "+ "Apellido :"+self.autor.get_apellido()+" Nacionalidad : "+ self.autor.get_nacionalidad()
    def set_autor(self, nuevo_autor):
        self.autor=nuevo_autor
        
    def get_ISBN(self):
        return self.ISBN
    def set_ISBN(self, nuevo_ISBN):
        self.ISBN=nuevo_ISBN
    
    def get_paginas(self):
        return str(self.paginas)
    def set_paginas(self, nueva_pagina):
        self.paginas=nueva_pagina
        
    def get_edicion(self):
        return self.edicion
    def set_edicion(self, nueva_edicion):
        self.edicion=nueva_edicion
    
    
    def get_editorial(self):
        return self.editorial
    def set_editorial(self, nueva_editorial):
        self.editorial=nueva_editorial
        
    def get_ciudad(self):
        return self.ciudad
    def set_ciudad(self, nueva_ciudad):
        self.ciudad=nueva_ciudad
    
    def get_pais(self):
        return self.pais
    def set_pais(self, nuevo_pais):
        self.pais=nuevo_pais
        
    def get_fecha(self):
        return self.fecha_edicion
    def set_fecha(self, nueva_fecha):
        self.fecha_edicion=nueva_fecha
    # se puede leer la informacion del libro a travez de los metodos get de manera individual
    # por eso entiendo que el metodo requerido para leer informacion debe proporcionar toda la informacion junta
    # ¿ esta bien hacer un metodo que devuelva un diccionario con la informacion requerida?    
    def leer_informacion(self):
        informacion={'Titulo':self.titulo,'Autor':self.get_autor_descripcion(),'ISBN':self.ISBN,'Paginas':self.paginas,'Edicion':self.edicion,'Editorial':self.editorial,'Ciudad':self.ciudad,'Pais':self.pais,'Fecha':self.fecha_edicion }
        return informacion
    
    def mostrar_informacion(self):
        print("")
        print("Titulo : "+ self.get_titulo()+ " "+self.get_edicion())
        print("")
        print("Autor : "+self.autor.get_apellido()+", "+self.autor.get_nombre())
        print()
        print("ISBN : "+ self.ISBN) #¿se debe acceder a la variable directamente o atravez del metodo get?
        print()
        print(self.editorial+", "+ self.ciudad+ " ("+self.pais+" )")
        print()
        print(self.get_fecha())
        print()
        print(str(self.paginas)+" paginas")
        
    
    
# testeo de la clase

#crear un objeto Persona para guardar el autor
autor_1= Persona("Pedro Bonifacio", "Palacios", "Argentino")

libro_1=Libro("Poesia y Prosa",autor_1,"987-571-059-8",160,"1ra edicion","Gradifco SRL","CABA","Argentina","Agosto 2006")

lectura=libro_1.leer_informacion()
print(str(lectura))

print("------------------------")
libro_1.mostrar_informacion()