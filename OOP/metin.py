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
        print(f'{self.nombre} recibio {cantidad} de daño. Salud restante: {self.salud}')

class Jugador(Personaje): # Hereda de personaje
    def __init__(self,nombre):
        super().__init__(nombre, salud=10, ataque=15)
        self.nivel = 1
        self.experiencia = 0
        self.salud_maxima = 100 

    def atacar(self, enemigo):
        if enemigo.salud > 0:
            print(f'{self.nombre} ataca a {enemigo.nombre}')
            enemigo.recibir_daño(self.ataque)

    
    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad
        print(f'{self.nombre} gana {cantidad} de EXP. Total EXP: {self.experiencia}')
        if self.experiencia >= self.nivel * 100:
            self.subir_nivel()
        

    def subir_nivel(self):
        self.nivel += 1
        self.experiencia = 0
        self.salud_maxima += 20
        self.salud = self.salud_maxima
        self.ataque += 5
        print(f'{self.nombre} ha subido a nivel {self.nivel}.')


    def añadir_item(self):
        pass

    def usar_item(self):
        pass


class Enemigo(Personaje): # Hereda de personaje 

    def __init__(self, nombre, salud, ataque, exp_otorgada):
        super().__init__(nombre, salud, ataque)
        self.exp_otorgada = exp_otorgada

    def atacar(self,jugador):
        print(f'{self.nombre} ataca a {jugador.nombre}')
        jugador.recibir_daño(self.ataque)


# Sistema de combate

def combate(jugador, enemigo):
    while jugador.esta_vivo() and enemigo.esta_vivo():
        print('-------------------------------------')
        jugador.atacar(enemigo)
        if enemigo.esta_vivo():
            enemigo.atacar(jugador)
            

    if jugador.esta_vivo():
        print(f'{jugador.nombre} ha derrotado a {enemigo.nombre}')
        print(f'{jugador.nombre} ha adquirido EXP')
        jugador.ganar_experiencia(enemigo.exp_otorgada)
    else:
        print(f'{jugador.nombre} ha sido derrotado por {enemigo.nombre}')

# Ejemplo de uso

jugador = Jugador("Marcelo")
enemigo = Enemigo("Lobo salvaje", salud=50, ataque=8, exp_otorgada=50)

combate(jugador, enemigo)


