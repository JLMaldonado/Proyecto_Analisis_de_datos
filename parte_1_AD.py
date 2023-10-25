import pandas as pd
import numpy as np
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]
convertir=np.array(data["age"]) #convierte el arreglo
promedios=np.mean(convertir) #calcula el promedio de la edades 
print("======================================================")
print(f" Promedio de las edades de todos los pacientes: {int(promedios)} Años")


