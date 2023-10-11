class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.balance = 0

    def hacer_retiro(self, cantidad):
        if cantidad > 0 and cantidad <= self.balance:
            self.balance -= cantidad
            return True
        else:
            return False

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}, Balance: ${self.balance}")

    def transfer_dinero(self, otro_usuario, cantidad):
        if self.hacer_retiro(cantidad):
            otro_usuario.depositar_dinero(cantidad)
            return True
        else:
            return False

    def depositar_dinero(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            return True
        else:
            return False

# Ejemplo de uso:
usuario1 = Usuario("sam")
usuario2 = Usuario("eve")

usuario1.depositar_dinero(200)
usuario1.mostrar_balance_usuario()

usuario1.transfer_dinero(usuario2, 50)

usuario1.mostrar_balance_usuario()
usuario2.mostrar_balance_usuario()
