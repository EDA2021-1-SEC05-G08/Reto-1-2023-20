"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import time as time
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos

def new_controller():

    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    catalog = {'resultados': None,
               'anotaciones': None,
               'penales': None}

    catalog['resultados'] = lt.newList("ARRAY_LIST")
    catalog['anotaciones'] = lt.newList("ARRAY_LIST")
    catalog['penales'] = lt.newList("ARRAY_LIST")
    
    return catalog

# Funciones para agregar informacion al modelo

def add_result(catalog, resultado):
    lt.addLast(catalog['resultados'], resultado)
    return catalog

def add_anotacion(catalog, anotacion):
    lt.addLast(catalog['anotaciones'], anotacion)
    return catalog

def add_penal(catalog, penal):
    lt.addLast(catalog['penales'], penal)
    return catalog

# Funciones de consulta

def req_1(catalog):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass

def req_2(catalog):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(catalog):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(catalog):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(catalog):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(catalog):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(catalog):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(catalog):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass

# Funciones para comparación

def compare_pais(resultado1, resultado2):

    country1 = resultado1["country"]
    country2 = resultado2["country"]

    if resultado1["date"] == resultado2["date"]:
        if country1 < country2:
            return True
        else: 
            return False 

def compare_fechas(resultado1, resultado2):

    resultado1 = resultado1["date"]
    resultado2 = resultado2["date"]
    
    year1 = resultado1.split("-")[0]
    year2 = resultado2.split("-")[0]
    month1 = resultado1.split("-")[1]
    month2 = resultado2.split("-")[1]
    day1 = resultado1.split("-")[2]
    day2 = resultado2.split("-")[2]
    
    if year1 < year2:
        return True
    elif year1 == year2 and month1 < month2:
        return True
    elif year1 == year2 and month1 == month2 and day1 < day2:
        return True
    else:
        return False