# Proyecto: Análisis de venta geografica y categorica - Dataset Superstore
# Objetivo:
# Analizar las ventas geografica y la venta por categoria
# para identificar oportunidades de mejora en la estrategia comercial.
# Esta estructurado de la siguente forma:
# 1 Exploración del dataset
# 2 KPI principales
# 3 Análisis geográfico
# 4 Análisis por categoría
# 5 Conclusiones
# 6  Recomendaciones

# 1) Exploración del dataset
## a) Importamos las librerias a utilizar
import pandas as pd
import matplotlib.pyplot as plt
## b) Importamos la base de datos
clientes=pd.read_csv(r"SampleSuperstore.csv")
# 2) KPI principales
## a) Imprimimos la informacion del dataset
print(clientes.info())
## b) Buscamos la venta total
ventas_totales=clientes["Sales"].sum()
print("Las ventas totales fueron de: $",ventas_totales)
## c) Buscamos la ganancia total
profit_total=clientes["Profit"].sum()
print("El profit_total es de: $", profit_total)
# 3) Análisis geográfico
## a) Buscamos la venta por region y realizamos un grafico para mayor compresion
ventas_region=clientes.groupby("Region")["Sales"].sum().sort_values(ascending=True)
ventas_region.plot(kind="bar",figsize=(10,6),color="green")

plt.title("Ventas por region")
plt.xlabel("Regiones")
plt.ylabel("Ventas en dolares")

plt.subplots_adjust(left=0.2, right=0.8, top=0.85, bottom=0.2)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.xticks(rotation=0)

plt.show()

## b) Buscamos las 5 ciudades que mas participacion tuvieron
ventas_ciudad=clientes.groupby("City")["Sales"].sum()
top_ciudades=ventas_ciudad.sort_values(ascending=False).head(5)
top_ciudades.plot(kind="bar",figsize=(10,6),color="lightblue")

plt.title("Top 5 de ventas por ciudad")
plt.xlabel("Ciudades")
plt.ylabel("Ventas en dolares")

plt.subplots_adjust(left=0.2, right=0.8, top=0.85, bottom=0.2)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.xticks(rotation=0)

plt.show()
# 4 Análisis por categoría
## a) Conocemos la categoria que mas se vende
ventas_categorias=clientes.groupby("Category")["Sales"].sum().sort_values(ascending=False)
ventas_categorias.plot(kind="bar",figsize=(10,6),color="yellow")

plt.title("Ventas por categorias")
plt.xlabel("Categorias")
plt.ylabel("Ventas en dolares")

plt.subplots_adjust(left=0.2,right=0.8, top=0.85, bottom=0.2)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.xticks(rotation=0)

plt.show()

## b) Conocemos la categoria que mas ganancia dio
profit_categoria=clientes.groupby("Category")["Profit"].sum().sort_values(ascending=False)
profit_categoria.plot(kind="bar",figsize=(10,6),color="red")

plt.title("Gananacias por categoria")
plt.xlabel("Categoria")
plt.ylabel("Ganancias en dolares")

plt.subplots_adjust(left=0.2,right=0.8,top=0.85,bottom=0.2)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.xticks(rotation=0)

plt.show()

## c) Analizamos si la categoria que mas se vendio es la que dio mas ganancia dio
ventas_sinprofit=ventas_categorias-profit_categoria
df_comparacion = pd.DataFrame({
    "Profit": profit_categoria,
    "Ventas sin profit": ventas_sinprofit})
df_comparacion.plot(kind="bar", figsize=(10,6), stacked=True)

plt.title("Ventas y Profit por categoría")
plt.xlabel("Categoría")
plt.ylabel("Diferencia")

plt.subplots_adjust(left=0.2,right=0.8,top=0.85,bottom=0.2)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.xticks(rotation=0)

plt.show()
## d) Conocemos que porcentaje de la venta total equivale a la ganancia que dio cada categoria
porcentaje_de_ganancia=profit_categoria*100/ventas_categorias
ax=porcentaje_de_ganancia.plot(kind="bar", figsize=(10,6))

ax.set_title("Porcentaje de ganancia aportado por cada categoria")
ax.set_xlabel("Categoría")
ax.set_ylabel("Porcentaje")   

plt.subplots_adjust(left=0.2,right=0.8,top=0.85,bottom=0.2)
ax.grid(axis="y", linestyle="--", alpha=0.6)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
for i in range(len(porcentaje_de_ganancia)):
    ax.text(
        i,
        porcentaje_de_ganancia.iloc[i],
        f"{porcentaje_de_ganancia.iloc[i]:.2f}%",
        ha="center"
    )

plt.show()
## e) Analizamos el margen total
margen_total = (profit_total / ventas_totales) * 100
print("Margen total:", round(margen_total,2), "%")

# 5 Conclusiones
## En este proyecto detectamos que:
## 1 - La zona que mas vendio fue la zona del Oeste y esto puede ser a distintas politicas de la empresa.
## 2 - la ciudad que mas compro fue New York un monto mayor a USD 250000 seguramente tenga que ver por su alta densidad poblacional
## 3 - Tecnologia fue lo que mas se vendio con montos superiores a USD 800000
## 4 - Las mayores ganancias fueron del rubro tecnologia
## 5 - Encontramos que la ganancia de la categoria de muebles es mucho menor que las del resto
## 6 - En relacion de porcentajes, la ganancia de cada categoria equivale al:
##          * 2.49% para muebles (Forniture)
##          * 17.04% para materiales de oficina (Office Supplies)
##          * 17.40% para tecnologia (Technologhy)
##    - de la venta total de cada categoria
## 7 - El margen de ganancia total fue de un 12.47%, debido a que la diferencia es muy amplia entre los 2 rubros que mas gananacia dieron
##     con respecto al que menos ganancia dio 
# 6 Recomendaciones:
## a) Hacer una revision en los descuentos y margenes para mejorar el profit de las futuras ventas 
## b) Realizar evaluaciones de las variables externas e internas para ver como mejorar la venta en las otras zonas
