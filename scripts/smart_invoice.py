# Crear una aplicación que permita a freelancers, pequeños negocios o
#  técnicos independientes generar, guardar y enviar facturas de manera rápida,
#
from fpdf import FPDF
import random 
from datetime import datetime, timedelta

Electrical_services = {
    "Instalacion enchufe": 15000,
    "Reparacion cortocircuito": 25000,
    "Cambio interruptor": 10000,
    "Instalacion luminaria": 20000,
    "Mantenimiento tablero_electrico": 30000,
    "Instalacion timbre": 12000,
    "Revision red domestica": 18000,
    "Instalacion automatico": 22000,
    "Colocacion toma_corriente_exterior": 17000,
    "Emergencia electrica": 40000
}
# lista de datos 

facturas = []
costo_solicitados = []
servicios_solicitados = []


# Función que agrega el costo total del servicio menos por la identificación de la factura.
# Esta función despues debe ser agregada a la función facturas

def costo_recargo_servicio(servicio):
    if servicio in Electrical_services:                           
        total = Electrical_services[servicio] * 1.145
        return int(total)
    else:
        return None
    
# Funciones (factura y costo total)


def random_ID(): # Función que genera un numero randon de 7 digitos 
    factura_id = random.randint(1000000, 9999999)
    return f'A{factura_id}'


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 16)
        self.set_text_color(30, 30, 30)
        self.cell(0, 10, "FACTURA ELECTRÓNICA", ln=1, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(100)
        self.cell(0, 10, f"Generado el {datetime.today().strftime('%d/%m/%Y')}", align="C")

def generar_pdf_factura(datos):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 10, "Datos del Cliente", ln=1, fill=True)
    pdf.cell(100, 10, f"Cliente: {datos['cliente']}", ln=1)
    pdf.cell(100, 10, f"Factura ID: {datos['factura ID ']}", ln=1)
    pdf.ln(5)

    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 10, "Detalle del Servicio", ln=1, fill=True)

    pdf.cell(100, 10, "Servicio", border=1)
    pdf.cell(60, 10, "Costo + Impuestos", border=1, ln=1)

    for servicio, costo in zip(datos["servicios"], datos["costos"]):
        pdf.cell(100, 10, servicio, border=1)
        pdf.cell(60, 10, f"${costo}", border=1, ln=1)

    total_general = sum(datos["costos"])
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(100, 10, "TOTAL", border=1)
    pdf.cell(60, 10, f"${total_general}", border=1, ln=1)
    pdf.set_font("Arial", size=12)

    pdf.ln(5)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 10, "Resumen de Fechas", ln=1, fill=True)
    pdf.cell(100, 10, f"Fecha de emisión: {datos['fecha emisión'].strftime('%d/%m/%Y')}", ln=1)
    pdf.cell(100, 10, f"Fecha de vencimiento: {datos['fecha de vencimiento'].strftime('%d/%m/%Y')}", ln=1)
    pdf.ln(10)

    nombre_archivo = f"factura_{datos['factura ID ']}.pdf"
    pdf.output(nombre_archivo)
    print(f"Factura guardada como {nombre_archivo}")

def Factura():
    while True:
        client = input('Cliente (nombre y apellido, "q" para salir):  ').capitalize().strip()
        if client.lower() == 'q':
            break

        servicios_solicitados = []
        costo_solicitados = []

        print('\nIngrese los servicios uno a uno. Escriba "q" para terminar.\n')
        while True:
            servicio = input('Ingrese el servicio ("q" para salir): ')
            if servicio.lower() == 'q':
                break
            if servicio not in Electrical_services:
                print('Servicio no valido. Intente nuevamente.')
                continue

            costo = costo_recargo_servicio
            servicios_solicitados.append(servicio)
            costo_solicitados.append(costo)

        if not servicios_solicitados:
            print('No se ingresó ningún servicio válido. Reiniciando factura.\n')
            continue

        fecha_emision = datetime.strptime(input('Fecha (YYYY-MM-DD): '),  "%Y-%m-%d")
        fecha_vencimiento = fecha_emision + timedelta(days=7)

        datos = {
            "cliente": client,
            "servicios": servicios_solicitados,
            "costos": costo_solicitados,
            "fecha emisión": fecha_emision,
            "fecha de vencimiento": fecha_vencimiento,
            "factura ID ": random_ID()
        }

        facturas.append(datos)

        print('\nFactura creada: ')
        for k, v in datos.items():
            print(f'{k.capitalize()}: {v}')
        print()

        generar_pdf_factura(datos)





Factura()

'''def costo_recargo_servicio2():
    z = input('Servicio realizado: ').capitalize().strip()
    costo_recargo = Electrical_services[z] * 0.145 + (Electrical_services[z]) if z in Electrical_services else False
    print(int(costo_recargo))'''

