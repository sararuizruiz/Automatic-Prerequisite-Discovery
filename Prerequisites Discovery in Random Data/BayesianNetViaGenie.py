# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:14:05 2020

@author: Sara
"""

import pysmile
import pysmile_license
from tablasprobcondicionadas import *


class RedBayesianaGenie:

    def __init__(self):
        net = pysmile.Network()
        
        for i in range(numtemas):
            tema = hoja.cell(row=1,column=i+1).value ##El título del tema que viene en la primera fila del excel
            self.create_cpt_node(net,"Tema"+tema,"Tema"+tema,["Suspenso","Aprobado"],60+100*(i//2),40+200*(i%2==1))
        
        for [[t1],padrest1] in padres:
            tema1 = hoja.cell(row=1,column=t1+1).value
            for cada in padrest1:
                tema2 = hoja.cell(row=1,column=cada+1).value
                net.add_arc("Tema"+tema2,"Tema"+tema1);
        
        for [[t1],prob] in probabilidades:
            tema1 = hoja.cell(row=1,column=t1+1).value
            tabla = []
            for pos in prob:
                tabla.append(1-pos)
                tabla.append(pos)
            net.set_node_definition("Tema"+tema1,tabla)

## Explicación del orden de estos números: https://support.bayesfusion.com/docs/Wrappers/using_arrays.html

        net.write_file("automaticogenie.xdsl")

 

 

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