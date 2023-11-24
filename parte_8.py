import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("Datos_categorizados_por_edades.csv")
df=pd.DataFrame(df)
# Generamos una lista de valores
x = ["Si","No"]
# Aplicamos la función elemento a elemento
y1 = df['anaemia'].value_counts()
y2 = df['diabetes'].value_counts()
y3 = df['smoking'].value_counts()
y4 = df['DEATH_EVENT'].value_counts()

# Creamos una figura con una cuadrícula de 2x2
fig, axes = plt.subplots(nrows=1, ncols=4,figsize=(12, 8))
axes[0].pie(y1, labels=x, autopct="%1.1f%%",startangle=90)
axes[0].set_title("Anémicos")


axes[1].pie(y2, labels=x, autopct="%1.1f%%",startangle=90)
axes[1].set_title("Diabeticos")

axes[2].pie(y3, labels=x, autopct="%1.1f%%",startangle=90)
axes[2].set_title("Fumadores")

axes[3].pie(y4, labels=x, autopct="%1.1f%%",startangle=90)
axes[3].set_title("Muertes")

# Ajustar los espacios entre los subgráficos
plt.tight_layout()

# Mostrar la figura con los subgráficos
plt.show()



