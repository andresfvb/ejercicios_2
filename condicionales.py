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

# Punto 3 --------------------------------------------------------------------

fianza = int(input("Valor de la fianza: "))

if fianza >= 50000:
    fianza_aux = fianza*0.02
    descuento = "2%"
else:
    fianza_aux = fianza*0.03
    descuento = "3%"
print(f"\nEl monto por el cual se aplico la fianza es de {fianza}\n"
      f"la cuota a pagar sera del {descuento} del monto: ${fianza_aux}\n")

# Punto 4 --------------------------------------------------------------------

ganancia = int(input("Cuanto es la ganacia diaria de la empresa: $"))
total = 0

for x in range(5):
    cantidad = int(input(f"Cantidad de emitida el dia #{x+1}: "))
    total = total + cantidad

if total > 170:
    pago = (ganancia*0.50)
    lista = [total, "Parar 1 semana", "Pagar 50% de la ganancia diaria", pago]
else:
    lista = [total, "No aplica", "No aplica", "0"]
print("---------- INFORME ----------")
print(f"\nCantidad emitida: {lista[0]}\n"
      f"Sanción: {lista[1]}\n"
      f"Multa: {lista[2]}\n"
      f"Valor a pagar: ${lista[3]}")

# Punto 5 --------------------------------------------------------------------

valor = int(input("Valor del inmueble y el carro: $"))

devaluacion_anual = valor*0.27
devaluacion_consecuente = valor*0.10
incremento_anual = valor*0.10

devaluacion_total = devaluacion_anual+(devaluacion_consecuente*2)
incremento_total = incremento_anual*3

if devaluacion_total < (incremento_total/2):
    comprarlo = "Debe comprarlo"
else:
    comprarlo = "No debe comprarlo"
print("\nNota:\n- La devaluación del auto es de 27% el primer año y 10% "
      "los años consecuentes"
      "\n- El incremento de los terrenos es del 10% anual"
      f"\nDevaluación total: ${devaluacion_total}"
      f"\nMitad del incremento anual del terreno: ${incremento_total}"
      f"\n{comprarlo}")

# Punto 6 --------------------------------------------------------------------

cant_computador = int(input("Cuantos computadores llevara: "))
total = cant_computador*11000
if cant_computador < 5:
    total_aux = total*0.10
    total = total-total_aux
    descuento = "10%"
elif cant_computador >= 5 and cant_computador < 10:
    total_aux = total*0.20
    total = total-total_aux
    descuento = "20%"
else:
    total_aux = total_aux*0.40
    total = total-total_aux
    descuento = "40%"

print(f"\nCantidad de computadoras: {cant_computador}"
      f"\nDescuento a aplicado {descuento}: ${total_aux}"
      f"\nValor antes de descuento: ${total+total_aux}"
      f"\nValor a pagar: ${total}")

# Punto 7 --------------------------------------------------------------------

equipo = int(input("Que marca desea comprar:\n"
                   "1. Samsung\n2. Panasonic\n3. Nosy\n"
                   "Escriba el numero de la marca: "))
equipos_lista = ["Samsung", "Panasonic", "Nosy"]
precio = int(input("Precio del equipo que desea comprar: $"))
desc_marca = 0
descuentom = "0%"
descuentop = "0%"
precio_m = 0
precio_aux = 0

if precio >= 2000:
    precio_aux = precio*0.10
    descuentop = "10%"
    precio = precio-precio_aux
if equipo == 3:
    desc_marca = precio*0.05
    descuentom = "5%"
    precio = precio-desc_marca
iva = precio*0.16

print(f"\nEl equipo que desea llevar es de marca: {equipos_lista[equipo-1]}"
      "\n------Valores antes de IVA-------"
      f"\nValor antes de descuentos: ${precio+precio_aux+desc_marca}"
      f"\nDescuento por valor producto {descuentop}: ${precio_aux}"
      f"\nPrecio de producto con descuento de P.: ${precio+desc_marca}"
      f"\nDescuento marca {descuentom}: ${desc_marca}"
      f"\nPrecio de producto con descuento de M.: {precio_m}"
      f"\nValor producto antes de IVA: ${precio}"
      f"\n------Valores despues de IVA"
      f"\nIVA 16%: ${iva}"
      f"\nTotal a pagar: ${precio+iva}")
