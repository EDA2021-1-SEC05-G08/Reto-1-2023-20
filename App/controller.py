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

import config as cf
import model
import time
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


def load_resultados (catalog):
    
    resultsfile = cf.data_dir + "results-utf8-"+ "small" + ".csv"
    input_file = csv.DictReader(open(resultsfile, encoding='utf-8'))
    
    for result in input_file:
        model.add_results(catalog, result)
    return model.results_size_resultados(catalog)


def load_anotaciones (catalog):
    
    anotacionesfile = cf.data_dir + "goalscorers-utf8-" + "small" + ".csv"
    input_file = csv.DictReader(open(anotacionesfile, encoding='utf-8'))
    
    for anotacion in input_file:
        model.add_anotaciones(catalog, anotacion)
    return model.results_size_anotaciones(catalog)        


def load_penales (catalog):
    
    penalesfile = cf.data_dir + "shootouts-utf8-" + "small" + ".csv"
    input_file = csv.DictReader(open(penalesfile, encoding='utf-8'))
    
    for penal in input_file:
        model.add_penales(catalog, penal)
    return model.results_size_penales(catalog)


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    model.req_1(control, 5, "g")
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


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

def req_9(control,algoritmo):
    """
    Retorna el resultado del requerimiento 8
    """
    start = get_time()
    print_final = model.req_9(control, algoritmo)
    end = get_time()
    delta_tiempo = delta_time(start, end)
    return print_final, delta_tiempo
    
# Funciones para medir tiempos de ejecucion

def print_req_9(catalog):
    return model.print_req_9(catalog)

def print_general(catalog):
    return model.print_general(catalog)

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

