# Analisis de texto. # Crea un programa que analice un texto ingresado por el usuario y devuelva:

# Numero de palabras, palabra mas larga, frecuencia de cada palabra
import re 

texto = input('Ingresa un texto: ')
print(texto)

palabras = texto.split()
print(palabras)

# Limpiamos el texto de caracteres especiales. 

palabras_limpias = [re.sub(r'[^a-zA-Z0-9 ]', '', palabra) for palabra in palabras] # List comprehension que aplica función regex para remplazar los caracteres filtrados.

# Contador de palabras
def contador_palabras(words):
    contador = 0 # Contador inicializa en cero
    for letra in words:
        contador += 1
    print(f'Contador de palabras: {contador}')


# Palabra mas larga

def palabra_mas_larga(words):
    palabra_mas_larga = max(words, key=len)
    print(f'Palabra mas larga: {palabra_mas_larga}')


# Contador de frecuencia de palabras

def frecuencia_palabras(words):
    frecuencia = {}
    for palabra in words:
        palabra = palabra.lower() # Se normaliza antes de contar
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    frecuencia_filtrada = {clave : valor for clave, valor in frecuencia.items() if valor >= 2 or clave == 'reina'} # Filtra las palabras que se repitan 2 o más veces
    print(frecuencia_filtrada)

print()
contador_palabras(palabras_limpias)
palabra_mas_larga(palabras_limpias)
frecuencia_palabras(palabras_limpias)


# ---------------------------------------------------------------------------------------------------------------------------------------------

# Generador de contraseñas. Escribe una función que genera una contraseña aleotoria con letras mayusculas, minusculas, numeros y simbolos.
# El usuario especifica la longitud. Sugerencia: Usa el modulo random y lista de caracteres para elegir al azar 



#--------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------
# Título: Validación de Contraseña Segura en Python
# Descripción:
# Este programa solicita al usuario una contraseña y verifica si cumple
# con los siguientes criterios de seguridad:
#   1. La longitud no debe superar los 12 caracteres.
#   2. Debe contener al menos una letra (mayúscula o minúscula).
#   3. Debe incluir al menos un número.
#   4. Debe tener al menos un carácter especial de la lista permitida.
# Si la contraseña cumple con todas las validaciones, se indica que es válida.
# En caso contrario, se muestra un mensaje de advertencia.
# --------------------------------------------------------------


lst_caracteres = ['!','#','$','%','&','/','=','*','¡','@'] # Caracteres aceptados en contraseña

def validaciones_password():
    contraseña = input('Ingresa una contraseña: ')
    if (len(contraseña) < 12
        and any(c.isdigit for c in contraseña)
        and any(c.isalpha for c in contraseña)
        and any(c in lst_caracteres for c in contraseña)
    ):
        print('Contraseña cumple con las validaciones ✅')
    else:
        print('Contraseña no cumple con los requisitos ⛔')
        print('\nRecuerda cumplir con los siguientes criterios de seguridad:' \
        '\n1. La longitud no debe superar los 12 caracteres.' \
        '\n2. Debe contener al menos una letra (mayúscula o minúscula).' \
        '\n3. Debe incluir al menos un número.' \
        '\n4. Debe tener al menos un carácter especial de la lista permitida.')


validaciones_password()





