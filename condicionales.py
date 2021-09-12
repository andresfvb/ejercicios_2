# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 16:45:54 2021

@author: Andres Vasquez
"""
from random import randrange

# Punto 1 --------------------------------------------------------------------


cant_camisas = int(input("Cuantas camisas desea comprar: "))
precio = 0
precio_aux = 0
for x in range(cant_camisas):
    precio_aux = int(input(f"Cuanto cuesta la prenda #{x+1}: $"))
    precio = precio_aux + precio

if cant_camisas >= 3:
    precio_aux = precio*0.30
    descuento = "30%"
else:
    precio_aux = precio*0.10
    descuento = "10%"
precio = precio - precio_aux
print(f"\nUsted compro {cant_camisas} prendas\n"
      f"Precio antes de descuento: ${precio+precio_aux}\n"
      f"Descuento del {descuento}: ${precio_aux}\n"
      f"Dando un total a pagar de: ${precio}")

# Punto 2 --------------------------------------------------------------------


precio_compra = int(input("Valor de la compra: $"))
descuento = randrange(0, 100)
if descuento < 74:
    precio_aux = precio_compra*0.15
    descuento_text = "15%"
else:
    precio_aux = precio_compra*0.20
    descuento_text = "20%"
precio_compra = precio_compra - precio_aux
print(f"\nPrecio compra: ${precio_compra+precio_aux}"
      f"\nBalota sacada: {descuento}"
      f"\nDescuento ganado {descuento_text}: ${precio_aux}"
      f"\nTotal a pagar: ${precio_compra}")
