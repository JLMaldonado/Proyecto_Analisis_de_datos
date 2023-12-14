import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
genero = ['Hombre', 'Mujer']
anemicos = [25, 35]  # Cantidad de anémicos por género
diabeticos = [15, 20]  # Cantidad de diabéticos por género
fumadores = [30, 25]  # Cantidad de fumadores por género
muertos = [10, 15]  # Cantidad de muertos por género

# Ancho de las barras
bar_width = 0.35
index = np.arange(len(genero))

# Configuración de gráficos
plt.figure(figsize=(10, 6))

# Gráfico de anémicos y diabéticos
plt.subplot(221)
plt.bar(index - bar_width/2, anemicos, bar_width, color='b', label='Anémicos', align='edge')
plt.bar(index + bar_width/2, diabeticos, bar_width, color='g', label='Diabéticos', align='edge')
plt.bar(index + bar_width/2, fumadores, bar_width, color='r', label='Fumadores', align='edge')
plt.xticks(index, genero)
plt.title('Anémicos y Diabéticos por Género')
plt.legend()

# Gráfico de fumadores
plt.subplot(222)
plt.bar(index - bar_width/2, fumadores, bar_width, color='b', label='Fumadores', align='edge')
plt.xticks(index, genero)
plt.title('Fumadores por Género')
plt.legend()

# Gráfico de muertos
plt.subplot(223)
plt.bar(index - bar_width/2, muertos, bar_width, color='b', label='Muertos', align='edge')
plt.xticks(index, genero)
plt.title('Muertos por Género')
plt.legend()

# Ajustar espaciado entre subplots
plt.tight_layout()

# Mostrar los gráficos
plt.show()
