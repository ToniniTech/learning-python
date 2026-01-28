'''productos_disponibles = {'leche' : 1500,
             'arroz' : 2000,
             'aceite' : 2300,
             'aceitunas' : 4000,
             'sopaipillas' : 3000,
             'mantequilla' : 5000,
             'torta selva negra' : 3000,
             'pan arabe' : 1500,
             'jugo de naranja' : 4200,
             'leche de avena' : 1200,
             'platano' : 1000,
             'vienesa venezolana' : 0,
             'mantequilla de mani' : 3200,
             'galletas' : 1000,
             'jamon' : 1000,
             'queso' : 2000

              

            }

def ask_user():
    lista_productos = []
    while True:
        productos = input('Enter the products ("s" to stop): ').strip().lower()
        if productos == 's':
             break
        if productos not in productos_disponibles:
             print('Producto no encontrado. Intente nuevamente.')
             continue
        lista_productos.append(productos)
        print(f'Producto {productos} agregado...')
    return lista_productos

def calcular_total(lista_shopping):
     return sum(productos_disponibles[producto] for producto in lista_shopping)

def mostrar_factura(lista_shopping):
     print('\n-------BOLETA-------')
     for producto in lista_shopping:
          precio = productos_disponibles[producto]
          print(f'{producto.title()} : ${precio}')
     total = calcular_total(lista_shopping)
     print(f'Total de la compra: ${total}')
     return total

def metodo_pago(balance, total_compra):
    print('\n----- MÉTODO DE PAGO -----')
    if balance >= total_compra:
        print(f'Pago realizado con éxito. Saldo restante: ${balance - total_compra}')
        return balance - total_compra
    else:
        print('Saldo insuficiente.')
        return balance
            

# ---------- Programa principal ----------

saldo_usuario = 10000
productos = ask_user()
if productos:
    total = mostrar_factura(productos)
    saldo_usuario = metodo_pago(saldo_usuario, total)
else:
    print("No se seleccionaron productos.")'''


'''datosPersonales = {
    "nombre" : 'Anthony',
    "edad" : 25,
    "Profesión": 'Ingenieniero en Ciencias de la computación',
    "Cuidad" : 'Santiago de Chile',
    "Idioma favorito" : 'Inglés'
}
'''
'''for i in datosPersonales.values():
    print(i)'''

# Elimina una clave existente usando del.
'''del datosPersonales['Idioma favorito']
''''''
print('\n-----Diccionario------\n')
for i, j in datosPersonales.items():
    print(f'{i} : {j}')'''

# Usa .get() para obtener una clave que no existe (con valor por defecto).
'''print()
print(datosPersonales.get('Apellido'))
print(datosPersonales.get('Madre, Virginia'))'''

# Verifica si una clave existe usando el operador in.

'''if 'madre' in datosPersonales:
    print('Existe')
else:
    print(False)'''

# 🔹 Nivel 2 – Iteración y métodos

'''
for i in datosPersonales.keys():
    print(i)'''

# Itera por todos los valores 
'''
for i in datosPersonales.values():
    print(i)'''

# Itera por todos los claves pares 

'''for i, j in datosPersonales.items():
    print(f'{i} : {j}')
'''
# Genera una copia de tu lista y manipulala
'''
copied_list = datosPersonales.copy()'''



'''copied_list['nombre'] = 'Camila'
copied_list['edad'] = 30
copied_list['Profesión'] = 'Ingenieria Comercial'
copied_list['Idioma favorito'] = 'Aleman'
 
for i, j in copied_list.items():
    print(f'{i} : {j}')

print()

for i, j in datosPersonales.items():
    print(f'{i} : {j}')'''

# Limpia todos los datos de tu lista con .clear()

'''copied_list.clear()
print(copied_list['Idioma favorito'])'''

# Cuantas veces aparece cada letra en una palabra o frase

'''dict = {}
palabra = input('Ingresa una frase: ').strip()

for i in palabra:
    if i.isalpha():
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

print(dict) 
'''
# Crea un diccionario que almacene estudiantes y sus notas. Agrega nuevos estudiantes dinámicamente.

'''StudentsGrade = {
    'Romina' : 7.0,
    'Alejandro' : 6.8
}
 
while True:
    
    students = input('Enter a student ("s" to stop): ').strip().capitalize() # Add a students
    if students.lower() == 's':
            break
    if not all(i.isalpha() or i.isspace() for i in students):
        print('Only letters and spaces are allowed')
        continue

    try:   

        grades = float(input('Enter a grade (0.0 to 7.0): ')) # Student's grade
        if grades > 7.0 or grades < 0:
            print('El rango calificativo es entre 0.0 - 7.0')
            continue

        StudentsGrade[students] = grades # Guardamos en el diccionario 

    except ValueError:
        print('Enter only numbers!')
        continue

print('---------Students grade register--------')
for i,j in StudentsGrade.items():
    print(f'{i} : {j}')
'''
# Dado un diccionario de productos y precios, pide al usuario una lista de productos y precios, pide al usuario
# y calcula el total a pagar.

#Crea 4 funciones: 1) para registrar los productos 2) calcular el total 3) mostrar factura 4) metodo de pago


productos_disponibles = {'leche' : 1500,
             'arroz' : 2000,
             'aceite' : 2300,
             'aceitunas' : 4000,
             'sopaipillas' : 3000,
             'mantequilla' : 5000,
             'torta selva negra' : 3000,
             'pan arabe' : 1500,
             'jugo de naranja' : 4200,
             'leche de avena' : 1200,
             'platano' : 1000,
             'vienesa venezolana' : 0,
             'mantequilla de mani' : 3200,
             'galletas' : 1000,
             'jamon' : 1000,
             'queso' : 2000

              

            }

def registrar_productos():
    lista_productos = []
    while True:
        producto = input('Ingresa un producto: ')
        if producto == 's':
            break
        elif producto not in productos_disponibles:
            print('Producto no disponible. Intenta con otro producto')
            continue
        print('Producto ingresado...')
        lista_productos.append(producto)
    return lista_productos

def calcular_total(productos_cliente):
    return sum(productos_disponibles[producto] for producto in productos_cliente)   

def mostrar_factura(productos_cliente):
    print('\n------ BOLETA -------')
    for products in productos_cliente:
        precio = productos_disponibles[products]
        print(f'{products} : ${precio}')
        total_compra = calcular_total(productos_cliente)
    print(f'\nTotal de la compra: ${total_compra}')
    return total_compra

def metodo_pago(balance, total_compra):
    if balance >= total_compra:
        print('Compra realizada')
    else:
        print('Saldo insuficiente')


    

# ---------- Programa principal ----------

productos = registrar_productos()
if productos:
    total = mostrar_factura(productos)
    metodo_pago(20000, total)
else:
    print('No se seleccionaron productos')
