# Validador de entrada 

# La cadena de texto ingresa tiene que cumplir con 3 requisitos:
# 1) Debe ser alfanumerica 2) Debe tener 10 digitos 3) Debe tener 2 caracteres especiales
caracteres = ['$','#','&','/','|','!','*','%']
entrada = input('Entra una cadena de texto: ')

# Contar cuántos caracteres especiales están en la cadena
contador = sum(1 for i in entrada if i in caracteres)

# Verificar si hay al menos una letra
tiene_letra = any(i.isalpha() for i in entrada)


# Verificar si hay al menos un número
tiene_numero = any(i.isdigit() for i in entrada)


if tiene_numero and tiene_letra and 8 <= len(entrada) <= 10 and contador >= 2:
    print(True)
    print('Tu entrada cumple con los parametros')
else:
    print(False)
    print('ERROR. Cumple los parametros!')

