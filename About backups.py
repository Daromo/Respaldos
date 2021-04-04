import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib import pyplot as pllt

df = pd.read_excel(R'D:\Development\Python\Respaldos\tamaños.xlsx',sheet_name=0)

print(df)
#TODOS LOS TAMAÑOS
dataSize = list(df.iloc[1])
nameDataBase = dataSize[1]
print(nameDataBase)
del(dataSize[:2])

#ALMACENAMOS LAS FECHAS
allColumns = list(df.columns)
columnas = []
for element in allColumns:
    if element.find('Unnamed:') < 0 and element!='Encargado':
        columnas.append(element)

#SEPRAR LOS BAK Y LOS ZIP
arrayZip = []
arrayBak = []
for size in dataSize:
    posicion = dataSize.index(size)
    if posicion%2 == 0:
        arrayZip.append(size/1048576)
    else:
        arrayBak.append(size/1048576)

data = {'Fechas': columnas, 'BAK': arrayZip}


#1048576
plt.plot(columnas,arrayZip,'o--', label='Respaldos ZIP')
plt.plot(columnas,arrayBak,'o-', label='Respaldos BAK')
plt.ylabel('Tamaños')
plt.xlabel('Fechas')
plt.legend()
plt.title(nameDataBase)
plt.show()
