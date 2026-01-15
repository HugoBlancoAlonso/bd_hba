```python
from pyspark.sql import SparkSession

spark = ( SparkSession.builder
         .appName("Pruebas")
         .master("spark://spark-master:7077")
         .getOrCreate()
         )
 
sc = spark.sparkContext
```

    Setting default log level to "WARN".
    To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
    26/01/15 08:51:33 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable


# Crear DataFrame


```python
data = [
    ("Ana", 15),
    ("Carlos", 22),
    ("Luis", 10),
    ("Marta", 35),
]

columns =["Nombre", "Edad"]

df = spark.createDataFrame(data, columns)
df.show()
```

                                                                                    

    +------+----+
    |Nombre|Edad|
    +------+----+
    |   Ana|  15|
    |Carlos|  22|
    |  Luis|  10|
    | Marta|  35|
    +------+----+
    


# Crear un esquema


```python
from pyspark.sql.types import StructType, StructField, BooleanType, IntegerType, StringType, DoubleType, LongType

direccion_schema = StructType([
    StructField("calle", StringType(), True), 
    StructField("cp", StringType(), True)
])

main_schema = StructType([
    StructField("id", IntegerType(), True), 
    StructField("nombre", StringType(), True),
    StructField("direccion", direccion_schema, True)
])

data = [
    (1, "Juan", ("Calle Gran Vía 25", "28013")),
    (2, "Maria", ("AV. Diagonal 100", "08018")),
    (3, "Alberto", None)
]

df = spark.createDataFrame(data, schema=main_schema)
df.printSchema()
```

    root
     |-- id: integer (nullable = true)
     |-- nombre: string (nullable = true)
     |-- direccion: struct (nullable = true)
     |    |-- calle: string (nullable = true)
     |    |-- cp: string (nullable = true)
    


# Caragar csv


```python
schema_worldcities = StructType([
    StructField("city", StringType(), True),
    StructField("city_ascii", StringType(), True),
    StructField("lat", DoubleType(), True),
    StructField("lng", DoubleType(), True),
    StructField("country", StringType(), True),
    StructField("iso2", StringType(), True),
    StructField("iso3", StringType(), True),
    StructField("admin_name", StringType(), True),
    StructField("capital", StringType(), True),
    StructField("population", LongType(), True),
    StructField("id", LongType(), True)
])


df_cities = (spark.read
             .format("csv")
             .schema(schema_worldcities)
             .option("header", "True")
             .option("quote", "\"")
             .load("./pruebas/worldcities.csv"))

df_cities.printSchema()
df_cities.show(5)
```

    root
     |-- city: string (nullable = true)
     |-- city_ascii: string (nullable = true)
     |-- lat: double (nullable = true)
     |-- lng: double (nullable = true)
     |-- country: string (nullable = true)
     |-- iso2: string (nullable = true)
     |-- iso3: string (nullable = true)
     |-- admin_name: string (nullable = true)
     |-- capital: string (nullable = true)
     |-- population: long (nullable = true)
     |-- id: long (nullable = true)
    


                                                                                    

    +---------+----------+-------+--------+---------+----+----+-----------+-------+----------+----------+
    |     city|city_ascii|    lat|     lng|  country|iso2|iso3| admin_name|capital|population|        id|
    +---------+----------+-------+--------+---------+----+----+-----------+-------+----------+----------+
    |    Tokyo|     Tokyo| 35.687|139.7495|    Japan|  JP| JPN|      Tōkyō|primary|  37785000|1392685764|
    |  Jakarta|   Jakarta| -6.175|106.8275|Indonesia|  ID| IDN|    Jakarta|primary|  33756000|1360771077|
    |    Delhi|     Delhi|  28.61|   77.23|    India|  IN| IND|      Delhi|  admin|  32226000|1356872604|
    |Guangzhou| Guangzhou|  23.13|  113.26|    China|  CN| CHN|  Guangdong|  admin|  26940000|1156237133|
    |   Mumbai|    Mumbai|19.0761| 72.8775|    India|  IN| IND|Mahārāshtra|  admin|  24973000|1356226629|
    +---------+----------+-------+--------+---------+----+----+-----------+-------+----------+----------+
    only showing top 5 rows
    


#  Cargar JSON


```python
schema_titanic = StructType([
    StructField("PassengerId", IntegerType(), True),
    StructField("Survived", IntegerType(), True),
    StructField("Pclass", IntegerType(), True),
    StructField("Name", StringType(), True),
    StructField("Sex", StringType(), True),
    StructField("Age", DoubleType(), True),
    StructField("SibSp", IntegerType(), True),
    StructField("Parch", IntegerType(), True),
    StructField("Ticket", StringType(), True),
    StructField("Fare", DoubleType(), True),
    StructField("Cabin", StringType(), True),
    StructField("Embarked", StringType(), True)
])

df_titanic = (spark.read
              .format("json")
              .schema(schema_titanic)
              .option("multiline", "true")
              .load("./pruebas/titanic.json"))

df_titanic.printSchema()
df_titanic.show(5)
```

    root
     |-- PassengerId: integer (nullable = true)
     |-- Survived: integer (nullable = true)
     |-- Pclass: integer (nullable = true)
     |-- Name: string (nullable = true)
     |-- Sex: string (nullable = true)
     |-- Age: double (nullable = true)
     |-- SibSp: integer (nullable = true)
     |-- Parch: integer (nullable = true)
     |-- Ticket: string (nullable = true)
     |-- Fare: double (nullable = true)
     |-- Cabin: string (nullable = true)
     |-- Embarked: string (nullable = true)
    
    +-----------+--------+------+--------------------+------+----+-----+-----+----------------+----+-----+--------+
    |PassengerId|Survived|Pclass|                Name|   Sex| Age|SibSp|Parch|          Ticket|Fare|Cabin|Embarked|
    +-----------+--------+------+--------------------+------+----+-----+-----+----------------+----+-----+--------+
    |       NULL|    NULL|  NULL|"Braund, Mr. Owen...|  male|NULL| NULL| NULL|       A/5 21171|NULL|     |       S|
    |       NULL|    NULL|  NULL|"Cumings, Mrs. Jo...|female|NULL| NULL| NULL|        PC 17599|NULL|  C85|       C|
    |       NULL|    NULL|  NULL|"Heikkinen, Miss....|female|NULL| NULL| NULL|STON/O2. 3101282|NULL|     |       S|
    |       NULL|    NULL|  NULL|"Futrelle, Mrs. J...|female|NULL| NULL| NULL|          113803|NULL| C123|       S|
    |       NULL|    NULL|  NULL|"Allen, Mr. Willi...|  male|NULL| NULL| NULL|          373450|NULL|     |       S|
    +-----------+--------+------+--------------------+------+----+-----+-----+----------------+----+-----+--------+
    only showing top 5 rows
    


# Datos Sucios


```python
# Definición del esquema con la columna para errores
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("nombre", StringType(), True),
    StructField("edad", IntegerType(), True),
    StructField("_corrupt_record", StringType(), True) # En esta columna guardaremos los datos corruptos
])

# Lectura del archivo CSV configurando el manejo de errores
df = ( spark.read
        .format("csv")
        .option("header", "true")
        .schema(schema)
        .option("mode", "PERMISSIVE")
        .option("columnNameOfCorruptRecord", "_corrupt_record")
        .load("datos_sucios.csv")
)
```
