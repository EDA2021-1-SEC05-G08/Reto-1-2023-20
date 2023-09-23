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
 """

from DISClib.ADT import list as lt
import config as cf
import model
import csv

csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    return model.new_controller()

def load_data(catalog):

    catalog, resultados_ordenados = load_resultados(catalog)
    catalog, anotaciones_ordenadas = load_anotaciones(catalog)
    catalog, penales_ordenados = load_penales(catalog)

    return catalog, model.getSize(resultados_ordenados), model.getTabla(resultados_ordenados), model.getSize(anotaciones_ordenadas), model.getTabla(anotaciones_ordenadas), model.getSize(penales_ordenados), model.getTabla(penales_ordenados)


def load_resultados(catalog):
    
    resultsfile = cf.data_dir + "results-utf8-"+ "large" + ".csv"
    #resultsfile = cf.data_dir + "resultados.csv"
    input_file = csv.DictReader(open(resultsfile, encoding='utf-8'))
    
    for result in input_file:
        model.add_result(catalog, result)

    resultados = catalog["resultados"]
    resultados = model.ordenar_resultados(resultados)
    catalog["resultados"] = resultados

    return catalog, resultados


def load_anotaciones (catalog):
    
    anotacionesfile = cf.data_dir + "goalscorers-utf8-" + "large" + ".csv"
    #anotacionesfile = cf.data_dir + "anotaciones.csv"
    input_file = csv.DictReader(open(anotacionesfile, encoding='utf-8'))
    
    for anotacion in input_file:
        model.add_anotacion(catalog, anotacion)

    anotaciones = catalog["anotaciones"]
    anotaciones = model.ordenar_anotaciones(anotaciones)
    catalog["anotaciones"] = anotaciones

    return catalog, anotaciones   


def load_penales (catalog):
    
    penalesfile = cf.data_dir + "shootouts-utf8-" + "large" + ".csv"
    #penalesfile = cf.data_dir + "penales.csv"
    input_file = csv.DictReader(open(penalesfile, encoding='utf-8'))
    
    for penal in input_file:
        model.add_penal(catalog, penal)

    penales = catalog["penales"]
    penales = model.ordenar_penales(penales)
    catalog["penales"] = penales

    return catalog, penales


def req_1(catalog, numero_partidos, nombre_equipo, condicion_equipo):
    """
    Retorna el resultado del requerimiento 1
    """
    respuesta = model.req_1(catalog, numero_partidos, nombre_equipo, condicion_equipo)
    return model.getTabla(respuesta[0]), respuesta[1], respuesta[2], respuesta[3]


def req_2(catalog, nombre_jugador, numero_goles):
    """
    Retorna el resultado del requerimiento 2
    """
    resultado = model.req_2(catalog, nombre_jugador, numero_goles)
    return model.getTabla(resultado[0]), resultado[1] 


def req_3(catalog, equipo_nombre, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 3
    """
    resultado = model.req_3(catalog, equipo_nombre, fecha_inicial, fecha_final)
    return model.getTabla(resultado[0]), resultado[1], resultado[2], resultado[3]


def req_4(catalog, torneo, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 4
    """
    resultado = model.req_4(catalog, torneo, fecha_inicial, fecha_final)
    return model.getTabla(resultado[0]), resultado[1], resultado[2], resultado[3], resultado[4]


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass