import pandas as pd
import numpy as np
from datasets import load_dataset
import csv
import requests
import matplotlib.pyplot as plt

df=pd.read_csv("Datos_categorizados_por_edades.csv")
df=pd.DataFrame(df)


#plt.show()
hombre=df[(df["sex"] == True)]
mujeres=df[(df["sex"] == False)]
hombre_anemicos=hombre[(hombre["anaemia"] == True)] 

mujeres_anemicas=mujeres[(mujeres["anaemia"] == True)]

data=mujeres_anemicas["anaemia"],hombre_anemicos["anaemia"]
h_diabetes=hombre[(hombre["diabetes"] == True)] 

m_diabtes=mujeres[(mujeres["diabetes"] == True)]

data2=h_diabetes["diabetes"],m_diabtes["diabetes"]

h_fumador=hombre[(hombre["smoking"] == True)] 

m_fumador=mujeres[(mujeres["smoking"] == True)]
data3=h_fumador["smoking"],mujeres["smoking"]
categorias=[1]

plt.bar( data,  color="blue", align="edge", label="Hombres")


plt.title('Distribución de Edades')

plt.xlabel('categorias')
plt.ylabel('Cantidad')
plt.show()
