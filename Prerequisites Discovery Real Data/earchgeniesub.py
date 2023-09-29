# -*- coding: utf-8 -*-
"""
Created on Sun May 24 13:53:33 2020

@author: Sara
"""


import pysmile
import pysmile_license
from dtablasprobcondsub import *

temaspadre = [18768,24425,24426,24427,20947]
for indice in range (len(temaspadre)):
    
    libro = load_workbook('discretizado'+str(temaspadre[indice])+'.xlsx')
    hoja = libro['Sheet1']
        
    numtemas = hoja.max_column-1
    prerequisitos = prere[indice]
    probabilidades = probfinal[indice]
    padres = padresfinal[indice]

    class RedBayesianaGenie:
    
        def __init__(self):
            net = pysmile.Network()
            
            for i in range(numtemas):
                tema = hoja.cell(row=1,column=i+2).value 
                self.create_cpt_node(net,"Tema"+str(tema),"Tema"+str(tema),["Suspenso","Aprobado"],60+100*(i//2),40+200*(i%2==1))
            
            for [[t1],padrest1] in padres:
                tema1 = hoja.cell(row=1,column=t1+2).value
                for cada in padrest1:
                    tema2 = hoja.cell(row=1,column=cada+2).value
                    net.add_arc("Tema"+str(tema2),"Tema"+str(tema1));
            
            for [[t1],prob] in probabilidades:
                tema1 = hoja.cell(row=1,column=t1+2).value
                tabla = []
                for pos in prob:
                    tabla.append(1-pos)
                    tabla.append(pos)
                net.set_node_definition("Tema"+str(tema1),tabla)
    
            net.write_file(str(temaspadre[indice])+".xdsl")
     
    
        def create_cpt_node(self, net, id, name, outcomes, x_pos, y_pos):
            handle = net.add_node(pysmile.NodeType.CPT, id)
            net.set_node_name(handle, name)
            net.set_node_position(handle, x_pos, y_pos, 85, 55)
            initial_outcome_count = net.get_outcome_count(handle)
    
            for i in range(0, initial_outcome_count):
                net.set_outcome_id(handle, i, outcomes[i])
    
            for i in range(initial_outcome_count, len(outcomes)):
                net.add_outcome(handle, outcomes[i])
    
            return handle
    
     
    ejecuto = RedBayesianaGenie()