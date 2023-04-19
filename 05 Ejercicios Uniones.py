#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:27:23 2023

@author: laptop
"""

import pandas as pd
import os


#####################
# Utilzando Concat #
####################

Saleprice = pd.read_csv("data/SalePrice.csv")

# 1-Dividir el Dataset en tres grupos con
#      usuarios comunes y diferentes y
#      variables diferentes en cada caso.

col_dif_A = Saleprice.iloc[100:120, :4]
col_dif_B = Saleprice.iloc[115:130, 8:11]
col_dif_C = Saleprice.iloc[125:135, 15:18]


# 2-Dividir el Dataset en tres grupos con
#      usuarios comunes y diferentes y
#      variables comunes y diferentes en cada caso.

col_ig_A = Saleprice.iloc[100:120, :5]
col_ig_B = Saleprice.iloc[115:130, 3:8]
col_ig_C = Saleprice.iloc[125:135, 5:10]


# 3-Realizar uniones de los tres primeros grupos:
#   a.	Incluyendo todas las variables y todas las observaciones, por el índice.
lista_a_concatenar = [col_dif_A, col_dif_B, col_dif_C]
incluye_todo = pd.concat(lista_a_concatenar, axis=1)

#   b.	Incluyendo las observaciones comunes de las tres tablas y todas las
#   variables, por el índice.
lista_a_concatenar = [col_dif_A, col_dif_B]
casas_solapadas = pd.concat(lista_a_concatenar, axis=1, join="inner")


#   c.	Incluyendo las observaciones de la tabla dos y enriqueciendo esa información
#   con la información de las otras dos tablas, por el índice.
lista_a_concatenar = [col_dif_A, col_dif_B, col_dif_C]
amplia_info_b = pd.concat(lista_a_concatenar, axis=1).reindex(col_dif_B.index)


# 4-Realizar uniones de los tres grupos creados en el punto 2:
#   a.Incluyendo todas las variables y todas las observaciones, por el índice.
lista_a_concatenar = [col_ig_A, col_ig_B, col_ig_C]
incluye_todo_col_repes = pd.concat(lista_a_concatenar, axis=1)
incluye_todo_filas_repes = pd.concat(lista_a_concatenar, axis=0)

#   b.	Incluyendo las observaciones comunes de las tres tablas y todas las
#   variables, por el índice.
lista_a_concatenar = [col_ig_A, col_ig_B]
casas_solapadas_col_repes = pd.concat(lista_a_concatenar, axis=1, join="inner")
casas_solapadas_filas_repes = pd.concat(
    lista_a_concatenar, axis=0, join="inner")

#   c.Incluyendo las observaciones de la tabla B y enriqueciendo esa
#   información con la información de las otras dos tablas, por el índice.
lista_a_concatenar = [col_ig_A, col_ig_B, col_ig_C]
amplia_info_b = pd.concat(lista_a_concatenar, axis=1).reindex(col_ig_B.index)
amplia_info_b_sin_duplicadas = amplia_info_b.loc[:,
                                                 ~amplia_info_b.columns.duplicated()]


# 5-Realizar dos tablas con algunas observaciones comunes y variables únicas,
#   incluyendo la Id en las dos tablas:
Tabla1 = Saleprice.iloc[5:20, 0:5]
Tabla2 = Saleprice.iloc[15:30, [0, 12, 16, 18, 20]]

# Unir:
#  a.Incluyendo todas las variables y todas las observaciones, por la Id.
todo = pd.merge(Tabla1, Tabla2, on="Id", how="outer")

#  b.Incluyendo las observaciones comunes de las dos tablas y todas las variables, por la Id.
interseccion = pd.merge(Tabla1, Tabla2, on="Id", how="inner")

#  c.Incluyendo las observaciones de la tabla dos y enriqueciendo esa información
#  con la información de la otra tabla, por la Id.
amplia_tabla2 = pd.merge(Tabla1, Tabla2, on="Id", how="right")
amplia_tabla1 = pd.merge(Tabla2, Tabla1, on="Id", how="right")


# 6-Realizar dos grupos con observaciones y variables comunes, incluyendo la Id en
#   las dos tablas:
Tabla1 = Saleprice.iloc[5:20, 0:5]
Tabla2 = Saleprice.iloc[15:30, [0, 4, 12, 16, 18, 20]]

# Unir:
#  a.Incluyendo todas las variables y todas las observaciones, por la Id.
todo = pd.merge(Tabla1, Tabla2, on="Id", how="outer")


todo = Tabla1.join(Tabla2, how="outer", rsuffix="_repe")

#  b.Incluyendo las observaciones comunes de las dos tablas y todas las variables, por la Id.
interseccion = pd.merge(Tabla1, Tabla2, on="Id", how="inner")

#  c.Incluyendo las observaciones de la tabla dos y enriqueciendo esa información
#  con la información de la otra tabla, por la Id.
amplia_tabla2 = pd.merge(Tabla1, Tabla2, on="Id", how="right")
amplia_tabla1 = pd.merge(Tabla2, Tabla1, on="Id", how="right")

# 7-Realizar un cambio de caracteres a una variable.
for columna in Saleprice:
    if type(Saleprice[columna][0]) == str:
        Saleprice[columna] = Saleprice[columna].str.replace("R", "WWW")
