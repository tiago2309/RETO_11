# RETO_11
## 1. Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.
| Método                | ¿Qué hace?                                                                                     |
| --------------------- | ---------------------------------------------------------------------------------------------- |
| `endswith(sufijo)`    | Devuelve `True` si la cadena termina con el `sufijo`.                                          |
| `startswith(prefijo)` | Devuelve `True` si la cadena empieza con el `prefijo`.                                         |
| `isalpha()`           | Devuelve `True` si todos los caracteres son letras (no incluye espacios, números, ni signos).  |
| `isalnum()`           | Devuelve `True` si todos los caracteres son letras o números. No acepta espacios ni símbolos.  |
| `isdigit()`           | Devuelve `True` si todos los caracteres son dígitos.                                           |
| `isspace()`           | Devuelve `True` si todos los caracteres son espacios o caracteres en blanco (`\n`, `\t`, etc). |
| `istitle()`           | Devuelve `True` si cada palabra en la cadena empieza con mayúscula.                            |
| `islower()`           | Devuelve `True` si todos los caracteres están en minúscula.                                    |
| `isupper()`           | Devuelve `True` si todos los caracteres están en mayúscula.                                    |

## 2. Procesar el archivo y extraer:

- Cantidad de vocales
- Cantidad de consonantes
- Listado de las 50 palabras que más se repiten

Este programa fue desarrollado para cumplir con los requerimientos del Reto 11 del curso de Programación de Computadores de la Universidad Nacional de Colombia. A continuación se describe el procedimiento paso a paso:

1. Lectura del archivo desde una URL
Como el archivo mbox.txt no se podía descargar directamente, se utilizó el módulo urllib.request para leer el contenido desde internet.
- Se lee el archivo directamente desde la URL.
- Se convierte el contenido a minúsculas con .lower() para evitar duplicados al contar palabras (por ejemplo, "The" y "the").
2. Conteo de vocales y consonantes
Se define un conjunto de vocales y consonantes, y se recorre el texto carácter por carácter para contarlas
- Se usa una lógica condicional para clasificar cada letra.
- No se tienen en cuenta tildes ni caracteres especiales.
3. Limpieza del texto y separación en palabras
Para contar palabras correctamente, se eliminan todos los signos de puntuación
- str.maketrans() y translate() se usan para reemplazar signos de puntuación por espacios.
- Luego, se divide el texto en palabras con split().
4. Conteo de frecuencia de palabras
Se utiliza la clase Counter del módulo collections para contar las palabras
- most_common(50) retorna una lista de tuplas con las 50 palabras más repetidas y su frecuencia.
5. Impresión de resultados
Finalmente, se imprimen:

- El número total de vocales.
- El número total de consonantes.
- El listado de las 50 palabras más comunes en el texto.

```
from collections import Counter  # Para contar la frecuencia de palabras
import string                    # Para acceder a signos de puntuación
import urllib.request            # Para leer el archivo directamente desde internet

# URL del archivo de texto
url = "https://www.py4e.com/code3/mbox.txt"

# Descarga y lectura del contenido desde la URL
response = urllib.request.urlopen(url)         # Abrimos la URL
texto = response.read().decode('utf-8').lower()  # Leemos, decodificamos a texto y pasamos a minúsculas

# Vocales y consonantes a contar
vocales = "aeiou"
consonantes = "bcdfghjklmnpqrstvwxyz"
num_vocales = 0
num_consonantes = 0

# Contar vocales y consonantes recorriendo todo el texto
for c in texto:
    if c in vocales:
        num_vocales += 1
    elif c in consonantes:
        num_consonantes += 1

# Eliminar signos de puntuación del texto
# Para evitar que se cuenten palabras como "email." y "email" como diferentes
limpio = texto.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))

# Dividir el texto en palabras
palabras = limpio.split()

# Contar la frecuencia de cada palabra
frecuencia = Counter(palabras)

# Obtener las 50 palabras más comunes
top_50 = frecuencia.most_common(50)

# Mostrar resultados
print("Cantidad de vocales:", num_vocales)
print("Cantidad de consonantes:", num_consonantes)
print("\nLas 50 palabras más frecuentes:")
for palabra, cuenta in top_50:
    print(f"{palabra}: {cuenta}")

```
RESULTADOS:
```
Cantidad de vocales: 1597835
Cantidad de consonantes: 2612121

Las 50 palabras más frecuentes:
edu: 31260
2007: 24480
org: 22456
sakaiproject: 21747
from: 21721
by: 18028
collab: 17970
x: 16846
0: 16309
received: 16180
iupui: 14820
umich: 14724
8: 14702
src: 14622
id: 14409
ac: 14260
uk: 13874
source: 13307
with: 12757
12: 12716
uhi: 12579
nakamura: 12571
uits: 12571
content: 12241
0500: 11774
java: 11336
11: 10997
branches: 10422
2: 10092
tool: 10039
dec: 9267
sak: 9220
nov: 8988
1: 7755
for: 7715
impl: 7675
mail: 7207
esmtp: 7188
paploo: 7188
dspam: 7188
sakai: 6989
14: 6825
0000: 6729
3: 6114
message: 5507
text: 5480
type: 5442
utf: 5394
plain: 5392
mr: 5391
```
<img width="1919" height="1004" alt="image" src="https://github.com/user-attachments/assets/58331e02-4d5c-4eb6-acbc-80dc54e84224" />
