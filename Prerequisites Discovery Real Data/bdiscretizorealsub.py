# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:55:59 2020

@author: Sara
"""

## LA PRIMERA FILA ES EL IDENTIFICADOR DE CADA TEMA, NO LOS DATOS DE UN ALUMNO.
import xlrd
import xlsxwriter

temaspadre = [18768,24425,24426,24427,20947]
for padres in temaspadre:
    
    librodatos = xlrd.open_workbook('ordenado'+str(padres)+'.xlsx')
    hojadatos = librodatos.sheet_by_index(0)
    
    librodiscretizado = xlsxwriter.Workbook('discretizado'+str(padres)+'.xlsx')
    hojadiscretizada = librodiscretizado.add_worksheet()
    
    numalumnos = hojadatos.nrows-1
    numtemas = hojadatos.ncols-1
    
    for tema in range(numtemas):
        hojadiscretizada.write(0,tema+1,hojadatos.cell_value(0,tema+1))
        
    for alumno in range(numalumnos):
        hojadiscretizada.write(alumno+1,0,hojadatos.cell_value(alumno+1,0))
        for tema in range(numtemas):
            if type(hojadatos.cell_value(alumno+1,tema+1)) is not str :
                if hojadatos.cell_value(alumno+1,tema+1)< 0.7:  
                    hojadiscretizada.write(alumno+1,tema+1,0)
                else:
                    hojadiscretizada.write(alumno+1,tema+1,1)
    
    librodiscretizado.close()

# En este ejemplo, como son numeros aleatorios entre -1 y 1, he puesto el 0 como umbral (criterio para discretizar y considerar que el alumno a suspendido o aprobado)