import pandas as pd
import numpy as np
from datasets import load_dataset
import csv
import requests
import matplotlib.pyplot as plt

df=pd.read_csv("Datos_categorizados_por_edades.csv")
df=pd.DataFrame(df)
hombre=df[(df["sex"] == True)]
mujeres=df[(df["sex"] == False)]
hombre_anemicos=hombre[(hombre["anaemia"] == True)] 

mujeres_anemicas=mujeres[(mujeres["anaemia"] == True)]

data=mujeres_anemicas["anaemia"].value_counts(),hombre_anemicos["anaemia"].value_counts()

h_diabetes=hombre[(hombre["diabetes"] == True)] 

m_diabtes=mujeres[(mujeres["diabetes"] == True)]

data2=h_diabetes["diabetes"],m_diabtes["diabetes"]

h_fumador=hombre[(hombre["smoking"] == True)] 

m_fumador=mujeres[(mujeres["smoking"] == True)]
data3=h_fumador["smoking"],mujeres["smoking"]

h_muertos=hombre[(hombre["DEATH_EVENT"] == True)] 

m_muerta=mujeres[(mujeres["DEATH_EVENT"] == True)]



ancho = 0.4

plt.bar("anemia", hombre_anemicos["anaemia"].count(), width=ancho, color="blue", align="edge", label="Hombres")
plt.bar("anemia", mujeres_anemicas["anaemia"].count(), width=-ancho, color="red", align="edge", label="Mujeres")
plt.bar("diabetes",h_diabetes['diabetes'].count() , width=ancho, color="blue", align="edge")
plt.bar("diabetes", m_diabtes['diabetes'].count(), width=-ancho, color="red", align="edge")
plt.bar("Fumadores",h_fumador['smoking'].count() , width=ancho, color="blue", align="edge")
plt.bar("Fumadores", m_fumador['smoking'].count(), width=-ancho, color="red", align="edge")
plt.bar("Muertes",h_muertos['DEATH_EVENT'].count() , width=ancho, color="blue", align="edge")
plt.bar("Muertes", m_muerta['DEATH_EVENT'].count(), width=-ancho, color="red", align="edge")
plt.xlabel("Categorías")
plt.ylabel("Cantidad")
plt.title("Histogramas por género")
plt.legend()
plt.show()

plt.hist(df["age"], bins=5, edgecolor='black')
plt.title('Distribución de Edades')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')

plt.show()