# -*- coding: utf-8 -*-
"""
Solo nesecitamos llamar a la clase Facade y con un metodo
podremos comprar dos entradas para la pelicula mas taquillera
tambien podemos cancelar la compra si descomentamos la linea 11
"""
from ClaseFacade import*

tienda=Facade()
tienda.comprar_entrada_par_taquillera()
#tienda.cancelar_entrada_par_taquillera()


