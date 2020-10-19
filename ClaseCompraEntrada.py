# -*- coding: utf-8 -*-
"""
Clase CompraEntrada gestiona la compra de entradas en un cine
"""
class CompraEntrada:
    nombre_cine=""
    nombre_pelicula=""
    cantidad_entradas=0;
    precio_entrada=0.0
    
    def __init__(self, nc, np,ce,pe):
        self.nombre_cine=nc
        self.nombre_pelicula=np
        self.cantidad_entradas=ce
        self.precio_entrada=pe
    
    def get_nombre_cine(self):
        return self.nombre_cine
         
    def get_nombre_pelicula(self):
        return self.nombre_pelicula
    
    def get_cantidad_entradas(self):
        return self.cantidad_entradas
         
    def get_precio_entrada(self):
        return self.precio_entrada
    
    def set_nombre_cine(self,arg):
        self.nombre_cine=arg
         
    def set_nombre_pelicula(self,arg):
        self.nombre_pelicula=arg
    
    def set_cantidad_entradas(self,arg):
        self.cantidad_entradas=arg
         
    def set_precio_entrada(self,arg):
        self.precio_entrada=arg
        
    def comprar_entrada(self):
        print("************************************************************")
        print("Felicidades por adquirir su entrada en el cine "+self.nombre_cine)
        print("Pelicula: "+self.nombre_pelicula)
        print("Cantidad de entradas: "+str(self.cantidad_entradas))
        print("Costo: "+str(self.cantidad_entradas*self.precio_entrada))
        print("************************************************************")

    
    def cancelar_compra(self):
        print("************************************************************")
        print("Usted cancelo su compra para la pelicula "+self.nombre_pelicula)
        print("Cine: "+self.nombre_cine)
        print("Reembolso: "+str(self.cantidad_entradas*self.precio_entrada))
        print("************************************************************")







