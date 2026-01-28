
# Clase base Personaje
class Personaje:
    def __init__(self, nombre, salud, ataque):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque

    def esta_vivo(self):
        return self.salud > 0

    def recibir_daño(self, cantidad):
        self.salud -= cantidad
        if self.salud < 0:
            self.salud = 0
        print(f"{self.nombre} recibió {cantidad} de daño. Salud restante: {self.salud}")


# Clase Jugador
class Jugador(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, salud=100, ataque=15)
        self.nivel = 1
        self.experiencia = 0
        self.inventario = []
        self.salud_maxima = 100

    def atacar(self, enemigo):
        print(f"{self.nombre} ataca a {enemigo.nombre}")
        enemigo.recibir_daño(self.ataque)

    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad
        print(f"{self.nombre} gana {cantidad} de EXP. Total EXP: {self.experiencia}")
        if self.experiencia >= self.nivel * 100:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.experiencia = 0
        self.salud_maxima += 20
        self.salud = self.salud_maxima
        self.ataque += 5
        print(f"¡{self.nombre} ha subido a nivel {self.nivel}!")

    def añadir_item(self, item):
        self.inventario.append(item)
        print(f"{self.nombre} ha obtenido {item.nombre}.")

    def usar_item(self, item):
        if item in self.inventario:
            item.usar(self)
            self.inventario.remove(item)
        else:
            print(f"{self.nombre} no tiene {item.nombre}.")


# Clase Enemigo
class Enemigo(Personaje):
    def __init__(self, nombre, salud, ataque, exp_otorgada):
        super().__init__(nombre, salud, ataque)
        self.exp_otorgada = exp_otorgada

    def atacar(self, jugador):
        print(f"{self.nombre} ataca a {jugador.nombre}")
        jugador.recibir_daño(self.ataque)


# Clase Item
class Item:
    def __init__(self, nombre, tipo, efecto):
        self.nombre = nombre
        self.tipo = tipo  # 'pocion' o 'arma'
        self.efecto = efecto

    def usar(self, jugador):
        if self.tipo == "pocion":
            jugador.salud += self.efecto
            if jugador.salud > jugador.salud_maxima:
                jugador.salud = jugador.salud_maxima
            print(f"{jugador.nombre} usa {self.nombre} y recupera {self.efecto} de salud.")
        elif self.tipo == "arma":
            jugador.ataque += self.efecto
            print(f"{jugador.nombre} equipa {self.nombre} y aumenta su ataque en {self.efecto}.")


# Sistema de combate
def combate(jugador, enemigo):
    while jugador.esta_vivo() and enemigo.esta_vivo():
        jugador.atacar(enemigo)
        if enemigo.esta_vivo():
            enemigo.atacar(jugador)

    if jugador.esta_vivo():
        print(f"{jugador.nombre} ha derrotado a {enemigo.nombre}!")
        jugador.ganar_experiencia(enemigo.exp_otorgada)
    else:
        print(f"{jugador.nombre} ha sido derrotado por {enemigo.nombre}...")


# Ejemplo de uso
jugador = Jugador("Guerrero")
enemigo = Enemigo("Lobo Salvaje", salud=50, ataque=8, exp_otorgada=50)

# Añadir un ítem al jugador
pocion = Item("Poción de Vida", "pocion", 30)
jugador.añadir_item(pocion)

combate(jugador, enemigo)

# Probar usar ítem
jugador.usar_item(pocion)

