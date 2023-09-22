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

from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort
from DISClib.Algorithms.Sorting import insertionsort
from DISClib.Algorithms.Sorting import selectionsort
from DISClib.Algorithms.Sorting import mergesort
from DISClib.Algorithms.Sorting import quicksort

from datetime import datetime
import time as time
from tabulate import tabulate

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

    if anotacion["scorer"] == "":
        anotacion["scorer"] = "Desconocido"

    if anotacion["minute"] == "":
        anotacion["minute"] = -1

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

def compare_paises(resultado1, resultado2):

    country1 = resultado1["country"]
    country2 = resultado2["country"]

    if resultado1["date"] == resultado2["date"]:
        if country1 < country2:
            return True
        else: 
            return False 

def compare_fechas(diccionario_1, diccionario_2):

    fecha_1 = diccionario_1["date"] 
    fecha_2 = diccionario_2["date"] 

    fecha_1 = datetime.strptime(fecha_1, "%Y-%m-%d")
    fecha_2 = datetime.strptime(fecha_2, "%Y-%m-%d")
    
    if fecha_1 < fecha_2:
        return True
    else:
        return False
    
def compare_puntajes(resultado_1, resultado_2):

    fecha_1 = resultado_1["date"]
    puntaje_local_1 = resultado_1["home_score"]
    puntaje_visitante_1 = resultado_1["away_score"]

    fecha_2 = resultado_2["date"]
    puntaje_local_2 = resultado_2["home_score"]
    puntaje_visitante_2 = resultado_2["away_score"]

    if fecha_1 == fecha_2:
        if puntaje_local_1 > puntaje_local_2:
            return True
        elif puntaje_local_1 < puntaje_local_2:
            return False
        elif puntaje_local_1 == puntaje_local_2:
            if puntaje_visitante_1 > puntaje_visitante_2:
                return True
            elif puntaje_visitante_1 <= puntaje_visitante_2:
                return False
    
def compare_minutos(anotacion_1, anotacion_2):

    fecha_1 = anotacion_1["date"]
    minuto_1 = float(anotacion_1['minute'])

    fecha_2 = anotacion_2["date"]
    minuto_2 = float(anotacion_2['minute'])

    if fecha_1 == fecha_2:
        if minuto_1 < minuto_2:
            return True
        elif minuto_1 > minuto_2:
            return False
        
def compare_jugadores(anotacion_1, anotacion_2):

    fecha_1 = anotacion_1["date"]
    minuto_1 = float(anotacion_1['minute'])
    jugador_1 = anotacion_1['scorer']

    fecha_2 = anotacion_2["date"]
    minuto_2 = float(anotacion_2['minute'])
    jugador_2 = anotacion_2['scorer']

    if fecha_1 == fecha_2 and minuto_1 == minuto_2:
        if jugador_1 < jugador_2:
            return True
        elif jugador_1 >= jugador_2:
            return False

def compare_equipos(penal_1, penal_2):

    fecha_1 = penal_1["date"]
    equipo_local_1 = penal_1['home_team']
    equipo_visitante_1 = penal_1['away_team']

    fecha_2 = penal_2["date"]
    equipo_local_2 = penal_2['home_team']
    equipo_visitante_2 = penal_2['away_team']

    if fecha_1 == fecha_2:
        if equipo_local_1 < equipo_local_2:
            return True
        elif equipo_local_1 > equipo_local_2:
            return False
        elif equipo_local_1 == equipo_local_2:
            if equipo_visitante_1 < equipo_visitante_2:
                return True
            elif equipo_visitante_1 >= equipo_visitante_2:
                return False

# Funciones de ordenamiento

def ordenar_resultados(resultados):

    resultados = mergesort.sort(resultados, compare_fechas)
    resultados = mergesort.sort(resultados, compare_puntajes)

    primero = lt.getElement(resultados, 0)
    lt.addLast(resultados, primero)

    return resultados

def ordenar_anotaciones(anotaciones):

    anotaciones = mergesort.sort(anotaciones, compare_fechas)
    anotaciones = mergesort.sort(anotaciones, compare_minutos)
    anotaciones = mergesort.sort(anotaciones, compare_jugadores)

    primero = lt.getElement(anotaciones, 0)
    lt.addLast(anotaciones, primero)

    return anotaciones

def ordenar_penales(penales):

    penales = mergesort.sort(penales, compare_fechas)
    penales = mergesort.sort(penales, compare_equipos)

    primero = lt.getElement(penales, 0)
    lt.addLast(penales, primero)

    return penales

# Funciones de auxiliares

def getSize(lista):
    return lt.size(lista)-1

def getTabla(lista):

    headers = list(lt.getElement(lista, 0).keys())
    data = []

    for i in range(1, 4):
        data.append(list(lt.getElement(lista, i).values()))

    for i in range(getSize(lista)-2, lt.size(lista)):
        data.append(list(lt.getElement(lista, i).values()))

    return tabulate(data, headers)