# BIG DATA APLICADO - Examen 2ª Evaluación

### **Nombre**:

**INSTRUCCIONES**:

- Si realizas este examen desde tu ordenador debes **grabar la pantalla** con OBS Studio en formato MKV y entregar el vídeo junto con el examen. Para entregarlo, debes subirlo a OneDrive y adjuntar fichero de texto con la URL del recurso compartido.
- Si lo haces en un equipo del centro, grabaré yo la pantalla desde el ordenador del profesor.
- Debes contestar cada pregunta del examen en la celda del cuaderno Jupyter que hay después de cada pregunta. Si necesitas más celdas, puedes agregarlas a continuación de la que hay.
- Todo tu código **tiene que estár ejecutado**.
- La **entrega** del examen práctico se realizará en el canal de Teams habilitado a tal efecto y consistirá en:
  - Notebook de Jupyter (`.ipynb`).
  - Notebook exportado en formato Markdown (`.md`)
  - Fichero de texto (`.txt.`) con la URL al vídeo compartido en caso de haberlo hecho en tu ordenador.
  - Estos tres ficheros deberán entregarse en un único fichero comprimido en formato ZIP (`.zip`) con el nombre `{apellidos}, {nombre} - BDA Ev2`

### Introducción

Trabajas para una startup de **análisis turístico**. Te han proporcionado un dataset crudo (`alojamientos.csv`) extraído mediante *web scraping* de diferentes portales de reservas.

El objetivo de este examen es realizar las siguientes tareas como paso previo a que el equipo de Inteligencia Artificial entrene su modelo:

- Ingestar estos datos
- Limpiar las inconsistencias de texto
- Realizar transformaciones de negocio para normalizar precios
- Estudiar estadísticamente la distribución de los mismos
- Eliminar propiedades atípicas (mansiones de lujo).

### Muestra del Dataset (`alojamientos.csv`)

El fichero tiene separador de comas (`,`) y contiene los siguientes datos. Algunos registros tienen errores de formato o valores nulos.

| id_alojamiento | nombre_local | descripcion_categoria | precio_noche | num_habitaciones | ciudad | puntuacion |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | pIso en el cEntro | x - Apartamento | 45.50 | 2 | Madrid | 4.5 |
| 2 | CHALET con PISCINA | y - Casa Rural | 1200.00 | 5 | Madrid | 4.8 |
| 3 | estudio acogedor | x - Estudio | 38.00 | 1 | Valencia |  |
| 4 | Loft Vistas Mar | x - Loft | 55.20 | 1 | Valencia | 3.9 |
| 5 | habitacion compartida | z - Habitacion | 22.00 | 1 | Sevilla | 4.1 |
| 6 | VILLA DE LUJO EXCLUSIVA | y - Villa | 3500.00 | 8 | Sevilla | 5.0 |


Los datos completos los tienes en el fichero `alojamientos.csv`.


```python
%cd practicas/
```

    [Errno 2] No such file or directory: 'practicas/'
    /workspace/practicas


    /usr/local/lib/python3.10/site-packages/IPython/core/magics/osm.py:393: UserWarning: This is now an optional IPython functionality, using bookmarks requires you to install the `pickleshare` library.
      bkms = self.shell.db.get('bookmarks', {})


### Ejercicio 1: Ingesta

El motor de Machine Learning es muy sensible a los tipos de datos. No puedes permitir que Spark infiera el esquema por su cuenta.

Carga los datos en el dataframe `df_raw` definiendo manualmente el esquema, asumiendo que `precio_noche` y `puntuacion` tienen decimales, y que `id_alojamiento` y `num_habitaciones` son enteros.


```python
from pyspark.sql import SparkSession

spark = ( SparkSession.builder
         .appName("Examen")
         .master("spark://spark-master:7077")
         .getOrCreate()
         )
```

    26/03/10 09:49:14 WARN SparkSession: Using an existing Spark session; only runtime SQL configurations will take effect.



```python
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType
from pyspark.sql import functions as f
from pyspark.sql import Window

schema = StructType([
    StructField("id_alojamiento", IntegerType(), True),
    StructField("nombre_local", StringType(), True),
    StructField("descripcion_categoria", StringType(), True),
    StructField("precio_noche", DoubleType(), True),
    StructField("num_habitaciones", IntegerType(), True),
    StructField("ciudad", StringType(), True),
    StructField("puntuacion", DoubleType(), True),
])

df_raw = (spark.read
             .format("csv")
             .schema(schema)
             .option("header", "True")
             .load("./data/alojamientos.csv"))
df_raw.show(5)

```

    +--------------+------------------+---------------------+------------+----------------+-------+----------+
    |id_alojamiento|      nombre_local|descripcion_categoria|precio_noche|num_habitaciones| ciudad|puntuacion|
    +--------------+------------------+---------------------+------------+----------------+-------+----------+
    |             1|lOfT vIstas Al MaR|       z - Habitacion|      140.87|               2| Bilbao|      NULL|
    |             2|    ATiCO luminOsO|       y - Casa Rural|       125.3|               4|Sevilla|       4.0|
    |             3|    aTICo lUmInoSo|          x - Estudio|        58.5|               2| Madrid|       4.3|
    |             4|    aTicO luMiNoSo|             x - Loft|      159.47|               4|Sevilla|       2.9|
    |             5| piSo En eL CeNTRo|       z - Habitacion|       171.4|               4|Sevilla|      NULL|
    +--------------+------------------+---------------------+------------+----------------+-------+----------+
    only showing top 5 rows
    


### Ejercicio 2: Limpieza de strings y manejo de nulos 

La información textual viene muy sucia del *scraping* y faltan valoraciones de algunos usuarios.

A partir de `df_raw`, crea un nuevo DataFrame `df_limpio` aplicando, en una única sentencia encadenada, las siguientes transformaciones:

1. **`nombre_local`**: convierte el texto al formato *Title Case* (primera letra de cada palabra en mayúscula y el resto en minúscula) para estandarizar los títulos.
2. **`descripcion_categoria`**: elimina los prefijos de clasificación (ej. "x - ", "y - "). Extrae **únicamente** el texto real de la categoría (ej. "Apartamento", "Casa Rural").
3. **`puntuacion`**: si un alojamiento no tiene puntuación (valor nulo), rellénalo con un `0.0`.
4. Muestra los 10 primeros registros del dataframe.


```python
df_limpio = df_raw.withColumn(
        "nombre_local", f.initcap(f.col("nombre_local"))
    ).withColumn(
        "descripcion_categoria", f.substring(f.col("descripcion_categoria"), 5, 20)
    ).withColumn(
        "puntuacion", f.when(f.col("puntuacion").isNull(), f.lit(0.0)).otherwise(f.col("puntuacion"))
    )

df_limpio.show(10)
```

    +--------------+--------------------+---------------------+------------+----------------+---------+----------+
    |id_alojamiento|        nombre_local|descripcion_categoria|precio_noche|num_habitaciones|   ciudad|puntuacion|
    +--------------+--------------------+---------------------+------------+----------------+---------+----------+
    |             1|  Loft Vistas Al Mar|           Habitacion|      140.87|               2|   Bilbao|       0.0|
    |             2|      Atico Luminoso|           Casa Rural|       125.3|               4|  Sevilla|       4.0|
    |             3|      Atico Luminoso|              Estudio|        58.5|               2|   Madrid|       4.3|
    |             4|      Atico Luminoso|                 Loft|      159.47|               4|  Sevilla|       2.9|
    |             5|   Piso En El Centro|           Habitacion|       171.4|               4|  Sevilla|       0.0|
    |             6|   Piso En El Centro|              Estudio|       72.83|               2|  Sevilla|       3.8|
    |             7|Habitacion Compar...|              Estudio|        86.3|               3| Valencia|       4.5|
    |             8|  Loft Vistas Al Mar|              Estudio|       99.61|               4|   Madrid|       2.5|
    |             9|  Loft Vistas Al Mar|           Habitacion|      138.08|               1| Valencia|       3.3|
    |            10|    Estudio Acogedor|          Apartamento|      112.38|               4|Barcelona|       4.8|
    +--------------+--------------------+---------------------+------------+----------------+---------+----------+
    only showing top 10 rows
    


### Ejercicio 3: Transformaciones matemáticas y reglas de negocio 

El departamento de marketing va a lanzar una campaña de *Precio Garantizado*. Sobre `df_limpio`, añade dos nuevas columnas para esta campaña:

1. **`precio_redondeado`**: redondea el `precio_noche` original hacia arriba para no mostrar céntimos.
2. **`precio_oferta`**: la plataforma va a ofrecer todos los alojamientos a un tope promocional de 100€. Crea esta columna que compare el `precio_redondeado` del alojamiento y el precio fijo de la campaña (100€) y se quede siempre **con el valor más bajo de los dos**.
3. Muestra los primeros 10 registros del dataframe


```python
df_limpio = df_limpio.withColumn(
    "precio_redondeado", f.ceil(f.col("precio_noche"))
).withColumn(
    "precio_oferta", f.when(f.col("precio_redondeado") <= 100, f.col("precio_redondeado")).otherwise(f.lit(100))
)

df_limpio.show(10)
```

    +--------------+--------------------+---------------------+------------+----------------+---------+----------+-----------------+-------------+
    |id_alojamiento|        nombre_local|descripcion_categoria|precio_noche|num_habitaciones|   ciudad|puntuacion|precio_redondeado|precio_oferta|
    +--------------+--------------------+---------------------+------------+----------------+---------+----------+-----------------+-------------+
    |             1|  Loft Vistas Al Mar|           Habitacion|      140.87|               2|   Bilbao|       0.0|              141|          100|
    |             2|      Atico Luminoso|           Casa Rural|       125.3|               4|  Sevilla|       4.0|              126|          100|
    |             3|      Atico Luminoso|              Estudio|        58.5|               2|   Madrid|       4.3|               59|           59|
    |             4|      Atico Luminoso|                 Loft|      159.47|               4|  Sevilla|       2.9|              160|          100|
    |             5|   Piso En El Centro|           Habitacion|       171.4|               4|  Sevilla|       0.0|              172|          100|
    |             6|   Piso En El Centro|              Estudio|       72.83|               2|  Sevilla|       3.8|               73|           73|
    |             7|Habitacion Compar...|              Estudio|        86.3|               3| Valencia|       4.5|               87|           87|
    |             8|  Loft Vistas Al Mar|              Estudio|       99.61|               4|   Madrid|       2.5|              100|          100|
    |             9|  Loft Vistas Al Mar|           Habitacion|      138.08|               1| Valencia|       3.3|              139|          100|
    |            10|    Estudio Acogedor|          Apartamento|      112.38|               4|Barcelona|       4.8|              113|          100|
    +--------------+--------------------+---------------------+------------+----------------+---------+----------+-----------------+-------------+
    only showing top 10 rows
    


### Ejercicio 4: Análisis estadístico de dispersión 

Antes de enviar los datos al algoritmo de IA, necesitamos saber si en las ciudades hay mucha desigualdad de precios provocada por propiedades de extremo lujo.

1. Agrupa el DataFrame por `ciudad`.
2. Calcula simultáneamente para la columna `precio_noche` original:
   - La **media**.
   - La **desviación estándar**.
   - La **curtosis**.
3. Muestra los valores obtenidos

**Pregunta de teoría (añade un comentario en tu código o en una celda aparte en formato Markdown):** En mi caso he obtenido los siguientes valores para la ciudad de Sevilla:

   - Media: 218.4883
   - Desviación: 615.7425
   - Curtosis: 28.9143

Interpreta estos resultados e indica qué quieren decir o qué conclusiones puedes sacar de estos datos.


```python
df_estadistico = df_limpio.groupBy("ciudad").agg(
    f.mean("precio_noche").alias("Media"),
    f.stddev("precio_noche").alias("Desviacion Estandar"),
    f.kurtosis("precio_noche").alias("Curtosis"),
)

df_estadistico.show()
```

    +---------+------------------+-------------------+-------------------+
    |   ciudad|             Media|Desviacion Estandar|           Curtosis|
    +---------+------------------+-------------------+-------------------+
    |   Madrid|106.18530864197538|  43.74734054983972|-1.3537951129749515|
    |   Bilbao| 101.1660465116279|  43.54278509680023|-1.2052510663957536|
    |Barcelona|107.88247058823525|  41.17001361523957|-1.0440217774103302|
    |     León| 97.96630872483223|  43.71184421636699|-1.1664732902607693|
    | Valencia|101.40708074534164|  40.59219470291905|-1.0776502097855514|
    |  Sevilla|218.48838709677406|  615.7425801311565| 28.914363118281646|
    +---------+------------------+-------------------+-------------------+
    


Interpretacion de las estadisticas de Sevilla

- Media: Tiene un precio medio superior al resto de ciudades pero tampoco nos da mucha mas información este campo
  
- Desviación Estándar: La desviación en este caso es de 615.74, esto es un valor muy alto y quiere decir que hay valores muy alejados de la media y pueden ser outliers

- Curtosis: La curtosisi al ser mayor que tres nos indica que los datos tienen una forma leptocúrtica y que habria que quitar outliers de forma radical

### Ejercicio 5: Limpieza de outliers 

Como sospechábamos en el ejercicio anterior, las mansiones y villas de súper lujo están distorsionando la media. Vamos a eliminarlas.

1. Utiliza el método `.approxQuantile()` para calcular cuál es la barrera del **percentil 95** (0.95) de la columna `precio_noche` en todo el dataset. (Permite un error del 0.01).
2. Extrae ese valor numérico y filtra tu DataFrame para quedarte **exclusivamente** con los alojamientos cuyo `precio_noche` sea menor o igual a dicho valor límite. Guarda el resultado como `df_sin_outliers`.


```python
p95 = df_limpio.approxQuantile("precio_noche", [0.95], 0.01)[0]
df_sin_outliers = df_limpio.filter(f.col("precio_noche")<= p95)


df_estadistico = df_sin_outliers.groupBy("ciudad").agg(
    f.mean("precio_noche").alias("Media"),
    f.stddev("precio_noche").alias("Desviacion Estandar"),
    f.kurtosis("precio_noche").alias("Curtosis"),
)

df_estadistico.show()
```

    +---------+------------------+-------------------+-------------------+
    |   ciudad|             Media|Desviacion Estandar|           Curtosis|
    +---------+------------------+-------------------+-------------------+
    |   Madrid|102.70928571428577|  42.03674267567101|-1.3484311206291018|
    |   Bilbao| 97.13693251533743| 41.093420748388176| -1.166599736051865|
    |Barcelona|104.51549382716045|  39.19601863817053|-1.0636029177989432|
    |     León| 93.66283687943263|  40.89130826831822|-1.1922418703256397|
    | Valencia| 98.09714285714287| 38.330180496332375|-1.0559910902705123|
    |  Sevilla|102.49620481927714|  41.35686570893504|-1.1787977568705916|
    +---------+------------------+-------------------+-------------------+
    


### Ejercicio 6: Ranking analítico con funciones de ventana 

Con nuestro dataset ya limpio de valores extremos, un analista quiere saber cuáles son los alojamientos más exclusivos de cada ciudad.

1. Define una partición de ventana (`Window`) agrupada por `ciudad` y ordenada por `precio_noche` de forma **descendente**.
2. Añade una columna llamada `ranking_ciudad` a tu DataFrame usando la función `dense_rank()` sobre dicha ventana.
3. Muestra por pantalla los 5 primeros registros del resultado final para validar tu trabajo.


```python
ventana = ( Window.partitionBy("ciudad").orderBy(f.desc("precio_noche")) )

df_ventana = df_sin_outliers.withColumn(
    "ranking_ciudad", f.dense_rank().over(ventana)
)

df_ventana.show(5)
```

    +--------------+--------------------+---------------------+------------+----------------+---------+----------+-----------------+-------------+--------------+
    |id_alojamiento|        nombre_local|descripcion_categoria|precio_noche|num_habitaciones|   ciudad|puntuacion|precio_redondeado|precio_oferta|ranking_ciudad|
    +--------------+--------------------+---------------------+------------+----------------+---------+----------+-----------------+-------------+--------------+
    |           893|      Atico Luminoso|                 Loft|      169.57|               4|Barcelona|       3.3|              170|          100|             1|
    |           410|Apartamento Refor...|                Villa|      169.28|               2|Barcelona|       2.8|              170|          100|             2|
    |           724|      Duplex Moderno|                Villa|      167.11|               1|Barcelona|       4.8|              168|          100|             3|
    |           658|Apartamento Refor...|           Habitacion|      166.87|               1|Barcelona|       3.1|              167|          100|             4|
    |           483|      Atico Luminoso|          Apartamento|      166.62|               1|Barcelona|       2.5|              167|          100|             5|
    +--------------+--------------------+---------------------+------------+----------------+---------+----------+-----------------+-------------+--------------+
    only showing top 5 rows
    

