# Proyecto: Análisis de Ventas - Dataset Superstore
# Objetivo:
# Analizar las ventas, la rentabilidad y el impacto de los descuentos
# para identificar oportunidades de mejora en la estrategia comercial.
# Herramientas utilizadas:
#- Python
#- Pandas
#- Matplotlib
# Esta estructurado de la siguente forma:
# 1 Exploración del dataset
# 2 KPI principales
# 3 Análisis de categoria
# 4 Análisis de impacto del descuento
# 5 Análisis del porcentaje de venta con perdida
# 6 Conclusiones
# 7 Recomendaciones
import pandas as pd
import matplotlib.pyplot as plt
# 1) Exploracion del dataset
## a) Importamos el data set
superstore= pd.read_csv(r"SampleSuperstore.csv")
## b) Conocemos el dataset
print(superstore.info())
## c) Conocemos si hay datos null
print(superstore.isnull().sum())
# 2) KPI´s principales
## a) Conocemos la ventas totales del dataset ($2297200.8603)
vt=superstore["Sales"].sum()
print(vt)
## b) Conocemos la ganancia totatl ($286397.0217)
gt=superstore["Profit"].sum()
print(gt)
# 3) Analisis por categoria
## Dividimos la ventas segun la categoria para conocer que categoria se vendió más
ventasXcategoria=superstore.groupby("Category")["Sales"].sum()
print(ventasXcategoria)
# 4) Analisis por sub-categoria
## Conocemos el producto mas vendido por la subcategoria y su relacion con la ganancia
relacion_Scat_salesXprofit=(superstore.groupby("Sub-Category")[["Sales","Profit"]].sum().sort_values(ascending=False,by=("Sales")))
## Descubrimos que hay 3 categorias que a pesar de la venta generaron perdidas, estas son "Tables","Bookcases" y "Supplies" 
## Realizamos un grafico de barras para conocer mas sobre estas relaciones
relacion_Scat_salesXprofit.plot(kind="bar",figsize=(10,6))
plt.title("Ventas por subcategoria")
plt.xlabel("Categoría")
plt.ylabel("Ventas totales")
plt.show()
# 4) Analisamos el impacto del descuento
## Analizamos los descuentos y sus resultados en la ganancia
descuentos = superstore[superstore["Discount"] > 0].groupby("Discount")["Profit"].mean()
print(descuentos)
## Los descuentos mayores a 0.2 generan perdida para la empresa.
descuentos.plot(kind="bar",figsize=(10,6))
plt.title("Rangos de descuentos y su impacto en el profit")
plt.xlabel("Cantidada de descuento")
plt.ylabel("Perdida o ganancia")
plt.show()
## Relación entre el descuento y el profit
plt.scatter(superstore["Discount"], superstore["Profit"])
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.title("Relación entre descuentos y profit")
plt.show()
# 5) Analizamos el porcentaje de venta con perdida con descuentos mayores al 0.2
## a) Primero guardamos en una variable las ventas que cumplen con un descuento mayor
##  al 0.2 y que generen perdidas
ventas_perdida= len(superstore[(superstore["Discount"] > 0.2) & (superstore["Profit"] < 0)])
## b) Ahora calculamos el porcentaje de ventas con descuentos mayores a 0.2 que generaron perdidas con base al numero total de transacciones
porcentaje_ventas_perdida=ventas_perdida/len(superstore)*100
print(f"El porcentaje total de ventas con descuentos elevados y que generaron perdida fue de: {porcentaje_ventas_perdida:.2f}%")
## c) Grafica del porcentaje con perdida en comparacion del total de ventas
vta_ganancia=len(superstore)-ventas_perdida
pie1=[vta_ganancia,ventas_perdida]
labels= ["Vtas con ganancias","Vtas c/dtos >20% con pérdidas"]
plt.figure(figsize=(8,8))
plt.pie(pie1,
        labels=labels,
        autopct="%1.2f%%",
        startangle=90)
plt.title("Impacto de descuentos altos en la rentabilidad")
plt.show()
# 6) Conclusión del negocio:
## Se identificó que los descuentos superiores al 20% presentan una relación negativa con la rentabilidad.
## Aproximadamente 13,49% de las transacciones presentan descuentos altos que generan pérdidas.
## Esto indica que la política actual de descuentos puede estar afectando el profit total del negocio.
# 7) Recomendación
## Revisar la estrategia de descuentos aplicada a determinadas categorías o productos.
## Evaluar límites máximos de descuento para evitar ventas no rentables.

