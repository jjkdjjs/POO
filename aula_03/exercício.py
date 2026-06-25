#Criar uma classe, atribuir a eles (pelo mneos dois, nome e +algo ) pelo menso uma acao mosrte o obnejto realiznado a acao

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.motor_funciona = True

    def acelerar(self):
        if not self.motor_funciona:
            print(f"O {self.marca} {self.modelo} nem liga mais. O motor foi pro pau.")
            return

        if self.modelo.lower() == "marea":
            print(f"O {self.marca} {self.modelo} tentou acelerar... e o MOTOR FUNDIU!")
            self.motor_funciona = False
        else:
            print(f"O {self.marca} {self.modelo} acelerou: Vrumm!")


meu_carro = Carro("Fiat", "Marea")
print("--- Testando o Primeiro Carro ---")
meu_carro.acelerar()

outro_carro = Carro("Chevrolet", "Corsa")
print("\n--- Testando o Segundo Carro ---")
outro_carro.acelerar()