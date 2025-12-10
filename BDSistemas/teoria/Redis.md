## Tipos de datos en Redis:

- Strings: "hola me llamo Hugo"

  - Guarda los valores en formas de cadenas

  - Se usa para valores simples de texto, numero o Json

- Bitmaps: 001101010110011110010101010
- Bit field: {23303}{13143234}{412343213}
- Hashes: {A:"food", B:"bar", C:"baz"}
  
  - Son mapas 
  
- Lists: [A -> B -> C -> D]

  - Son una colección ordenadas

  - Se usan para implementar colas o pilas

- Sets {A, B, C, D}

  - Se usa para almacenar cadenas desordenadas pero UNICAS

- Sorted Sets: {A:0.1, B:0.3, C:20, D:34}

  - Son conjuntos ordenados por un score

- Geospatial Index: {A:(51.4, 45.7), B:(32.5, 52.7)}
- Hyperloglogs: 011101 001101 01010010
- Streams
