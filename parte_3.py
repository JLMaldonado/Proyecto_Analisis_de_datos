import pandas as pd
import numpy as np
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

df=pd.DataFrame(data)
#print(df['is_smoker'])

#Verificar que los tipos de datos son correctos en cada colúmna
#  (por ejemplo que no existan colúmnas numéricas en formato de cadena).
verificar=df.dtypes
print(verificar)


#Calcular la cantidad de hombres fumadores vs mujeres fumadoras
#  (usando agregaciones en Pandas).
hombre_fumadores=df[(df["is_male"] == True)]
mujeres_fumadores=df[(df["is_male"] == False)]
a
hombre_fumadores=hombre_fumadores[(hombre_fumadores["is_smoker"] == True)] 
hombre_fumadores=hombre_fumadores["is_smoker"].count()

mujeres_fumadores=mujeres_fumadores[(mujeres_fumadores["is_smoker"] == True)] 
mujeres_fumadores=mujeres_fumadores["is_smoker"].count()

print("\n==================== Cantidad de Hombres y mujeres fumadores ==============================")
print(f"La cantidad de hombres fumadores es de : {hombre_fumadores} hombres " )
print("\n======================================================")
print(f"La cantidad de mujeres fumadores es de : {mujeres_fumadores} mujeres " )
print("\n======================================================")
