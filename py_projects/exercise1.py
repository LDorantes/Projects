from sklearn.datasets import fetch_openml
import pandas as pd

# Descargar la base de datos desde OpenML
dataset = fetch_openml(name='adult', version=2, as_frame=True)

# Obtener el dataframe
data = dataset.frame

# Mostrar las primeras filas para entender la estructura
print(data.head())

# Describir la base de datos
print(data.describe(include='all'))

# Identificar el tipo de variable
print(data.dtypes)

