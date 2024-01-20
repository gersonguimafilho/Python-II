class Automovel:
    def __init__(self, cor, modelo, num_portas, tipo_cambio, placa, marca):
        self.cor = cor
        self.modelo = modelo
        self.num_portas = num_portas
        self.tipo_cambio = tipo_cambio
        self.motor = False
        self.placa = placa
        self.marca = marca
    def ligar(self):
        if(self.motor==True):
            print("carro ja esta ligado!")
        else:
             self.motor = True



carro=Automovel("Branco", "fusca", "3","manual","tuto2024", "volks")
print(carro.motor)
carro.ligar()
print(carro.motor)
carro.ligar()
