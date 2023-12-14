import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
# Cargar el conjunto de datos
df = pd.read_csv('Datos_categorizados_por_edades.csv')

# Eliminar la columna Categoria_por_edad
df = df.drop(columns=['Categoria_por_edad'])

# Graficar la distribución de clases
plt.hist(df['DEATH_EVENT'])
plt.xlabel('Clase')
plt.ylabel('Frecuencia')
plt.title('Distribución de clases')
plt.show()



# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=['DEATH_EVENT']), df['DEATH_EVENT'], test_size=0.2, stratify=df['DEATH_EVENT'], random_state=42)



# Ajustar un árbol de decisión
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Calcular la precisión sobre el conjunto de prueba
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión: {accuracy:.2f}')
