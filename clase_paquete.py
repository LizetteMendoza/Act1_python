# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 23:05:06 2021

@author: Lizette
"""

class Paquete:
    
    def __init__(self,id,origen,destino,peso):
        self.id=id
        self.origen=origen
        self.destino=destino
        self.peso=peso
    
p1=Paquete("D5436","Mexico","USA",2.5)

print(p1.id)
print(p1.origen)
print(p1.destino)
print(p1.peso)
    
    