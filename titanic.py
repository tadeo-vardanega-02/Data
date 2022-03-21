import pandas as pd

# Traigo el dataset que va a ser procesado
data = pd.read_csv(r'https://raw.githubusercontent.com/Club-datos-FCEN/ClubDeDatos/main/01%20-%20Titanic/titanic_test.csv')

# Elimino columnas que no voy a usar
data = data.drop(['SibSp', 'Parch', 'Cabin', 'Ticket'], axis=1)
print(data)
# Elimino los valores nulos
data = data.dropna()

# Cambio male y female de la columna Sex por 1 y 0

data['Sex'] = data['Sex'].map({'male': 1, 'female': 0})

# Cambio los datos de embarque por numeros

data['Embarked'] = data['Embarked'].replace(['Q', 'S', 'C'], [0, 1, 2])

# Paso la columna Age a entero

data['Age'] = data['Age'].astype(int)

# Borro las comas y puntos de la columna name

data['Name'] = data['Name'].str.replace(',', '')
data['Name'] = data['Name'].str.replace('.', '')

# Reseteo el indice
data.reset_index(drop=True, inplace=True)

print(data)

# Descargo el nuevo csv

data.to_csv('titanic.csv')
