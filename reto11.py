from collections import Counter
import string
import urllib.request

# Descargar contenido directamente desde el enlace
url = "https://www.py4e.com/code3/mbox.txt"
response = urllib.request.urlopen(url)
texto = response.read().decode('utf-8').lower()

# Inicializar contadores
vocales = "aeiou"
consonantes = "bcdfghjklmnpqrstvwxyz"
num_vocales = 0
num_consonantes = 0

# Contar vocales y consonantes
for c in texto:
    if c in vocales:
        num_vocales += 1
    elif c in consonantes:
        num_consonantes += 1

# Limpiar texto y separar en palabras
limpio = texto.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
palabras = limpio.split()

# Contar frecuencia de palabras
frecuencia = Counter(palabras)
top_50 = frecuencia.most_common(50)

# Mostrar resultados
print("Cantidad de vocales:", num_vocales)
print("Cantidad de consonantes:", num_consonantes)
print("\nLas 50 palabras más frecuentes:")
for palabra, cuenta in top_50:
    print(f"{palabra}: {cuenta}")

