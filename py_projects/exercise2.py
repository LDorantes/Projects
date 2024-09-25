# Ejercicio 1: Descargar la base de datos y describirla
from sklearn.datasets import fetch_openml
import pandas as pd

# Descargar la base de datos desde OpenML
dataset = fetch_openml(name='adult', version=2, as_frame=True)
data = dataset.frame

# Describir la base de datos
print(data.describe(include='all'))

# Ejercicio 2: Gráficas y parámetros estadísticos
import matplotlib.pyplot as plt
import seaborn as sns

# Histograma para variables numéricas
data['age'].hist(bins=20)
plt.title('Histograma de la variable "age"')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()

# Gráfico de barras para variables categóricas
data['workclass'].value_counts().plot(kind='bar')
plt.title('Gráfico de barras de la variable "workclass"')
plt.xlabel('Clase de trabajo')
plt.ylabel('Frecuencia')
plt.show()

# Gráfico de dispersión entre dos variables numéricas
plt.scatter(data['age'], data['hours-per-week'])
plt.title('Dispersión entre Edad y Horas trabajadas por semana')
plt.xlabel('Edad')
plt.ylabel('Horas por semana')
plt.show()

# Obtener los parámetros estadísticos
print(data.describe())
