class CuentaBancaria:

    def __init__(self, balance):
        self.balance = balance
        self.movimientos = []  # Lista de movimientos (historial)

    def retirar(self):
        print('------------RETIRAR------------')
        while True:
            try:
                retirar = float(input('Ingresa la cantidad a retirar: '))
                if retirar > 1000:
                    print('Has excedido el límite de retiro por transacción')
                elif retirar <= self.balance:
                    self.balance -= retirar
                    self.movimientos.append(f'Retiro: -${round(retirar,2)}')
                    print(f'Se han retirado ${retirar}')
                    exit = input('Quieres realizar otro retiro (Oprime cualquier letra para continuar /"no" para salir): ')
                    if not exit.lower() == 'no':
                        continue
                    else:
                        break
                else:
                    print('Balance insuficiente')
                    break
            except ValueError:
                print('Entrada invalida')

    def depositar(self):
        print('-----------DEPOSITAR--------')
        while True:
            try:
                depositar = float(input('Ingresa la cantidad a depositar: '))
                if depositar > 0:
                    self.balance += depositar
                    self.movimientos.append(f'Depósito: +${round(depositar,2)}')
                    print(f'Se han depositado ${depositar}')
                    exit = input('Quieres realizar otro deposito (Oprime cualquier letra para continuar / "no" para salir): ')
                    if not exit.lower() == 'no':
                        continue
                    else:
                        break
                else:
                    print('La cantidad debe ser mayor que cero')
            except ValueError:
                print('Entrada invalida')
    
    def transferir(self, cuenta_destino):
        print('---------TRANSFERENCIA---------')
        while True:
            try: 
                transferir = float(input('Ingresa el monto a transferir: '))
                if transferir > 1000:
                    print('Has excedido el limite de transferencia por transacción.')
                elif transferir < self.balance:
                    self.balance -= transferir
                    cuenta_destino.balance += transferir
                    self.movimientos.append(f'Transferencia realizada a cuenta destino: -${round(transferir,2)}')
                    print('Transacción realizada exitosamente')
                    exit = input('Quieres realizar otra transferencia (Oprime cualquier letra para continuar / "no" para salir): ')
                    if not exit.lower() == 'no':
                        continue
                    else:
                        break
                else:
                    print('Saldo insuficiente')
        
            except ValueError:
                print('Oops! Entrada invalida')

    def mostrarDatos(self, cuenta = 'cuenta'):
        print(f'\nResumen de cuenta: {cuenta}')
        print((f'Balance actual: ${round(self.balance,2)}'))

    def mostrarHistorial(self, cuenta = 'cuenta'):
        print('\nHistorial de Movimientos:')
        print(f'Cuenta: {cuenta}')
        if not self.movimientos:
            print('No hay movimientos.')
        else:
            for mov in self.movimientos:
                print(mov)


# Uso
anthonyCuenta = CuentaBancaria(2000)
camilaCuenta = CuentaBancaria(1500)
anthonyCuenta.retirar()
anthonyCuenta.depositar()
anthonyCuenta.transferir(camilaCuenta)
anthonyCuenta.mostrarHistorial('usuario2')
anthonyCuenta.mostrarDatos('usuario2')
camilaCuenta.mostrarDatos('usuario1')
