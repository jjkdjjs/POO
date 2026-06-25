class Animal:
    def __init__(self, nome, especie, som):
        self.nome = nome
        self.especie = especie
        self.som = som
        self.energia = 100

    def falar(self):
        print(f"{self.nome} diz: {self.som}")   
    
    def comer(self):
        self.energia += 20
        print(f"{self.nome} comeu e agora tem {self.energia} de energia.")

    def status(self):
        print(f"-- {self.nome} --")
        print(f"Espécie: {self.especie}")
        print(f"Energia: {self.energia}")

cachorro = Animal("Kiko", "Cachorro", "Au au")
gato = Animal("Mimi", "Gato", "Miau")
porco = Animal("Rodolfo", "Porco", "Oink")
lystorossauros = Animal("Maicon", "Vencedor", "Grrr")

gato.falar()
cachorro.comer()
cachorro.status()
porco.falar()
lystorossauros.falar()
porco.status()
lystorossauros.status()