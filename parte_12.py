import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score

# Cargar el conjunto de datos
df = pd.read_csv('Datos_categorizados_por_edades.csv')

# Eliminar la columna Categoria_por_edad
df = df.drop(columns=['Categoria_por_edad'])

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=['DEATH_EVENT']), df['DEATH_EVENT'], test_size=0.2, stratify=df['DEATH_EVENT'], random_state=42)

# Ajustar un modelo de Random Forest
clf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
clf.fit(X_train, y_train)

# Calcular la precisión y el F1-Score sobre el conjunto de prueba
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
print(f'Precisión: {accuracy:.2f}')
print(f'F1-Score: {f1:.2f}')

# Calcular la matriz de confusión
cm = confusion_matrix(y_test, y_pred)
print('Matriz de confusión:')
print(cm)
