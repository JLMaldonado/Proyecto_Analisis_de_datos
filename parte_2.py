import pandas as pd
import numpy as np
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

#PARTE 2 CARGAR DATOS
#Convertir la estructura Dataset en un DataFrame 
# de Pandas usando pd.DataFrame.
df=pd.DataFrame(data)

#Separar el dataframe en dos diferentes, uno conteniendo las 
# filas con personas que perecieron (is_dead=1) y otro con el complemento.
pacientes_fallecidos= df[(df["is_dead"] == 1)]
pacientes_no_fallecidos=df[(df["is_dead"] == 0)]

#Calcular los promedios de las edades de cada dataset e imprimir.
p_pf=pacientes_fallecidos["age"].mean()
p_no_pf=pacientes_no_fallecidos["age"].mean()
print("\n======================================================")
print(f"Promedio de edad de pacientes fallecidos: {int(p_pf)} Años ")
print("\n======================================================")
print(f"Promedio de edad de pacientes no fallecidos: {int(p_no_pf)} Años")
print("\n======================================================")

