# -*- coding: utf-8 -*-
"""
La clase Facade actua como fachada para la compra 
de dos entradas para la pelicula de los vengadores en el Multicine, 
tambien nos permite cancelar la compra de la mencionada pelicula la clase 
Facade es la unica que interactua con la clase CompraEntrada

"""
from ClaseCompraEntrada import*
class Facade:
    compra=CompraEntrada
    
    def __init__(self):
        self.compra=CompraEntrada("Multicine","Vengadores",2,64.99)
    
    def comprar_entrada_par_taquillera(self):
        self.compra.comprar_entrada()
    
    def cancelar_entrada_par_taquillera(self):
        self.compra.cancelar_compra()
        
    
    

