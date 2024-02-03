class Pessoas:
    def __init__(self, nome, datansc, cpf, filiacao1, filizacao2):
        self.nome = nome
        self.datansc = datansc
        self.cpf = cpf
        self.filiacao1 = filiacao1
        self.filiacao2 = filizacao2


#tupla
        frutas =("banana", "maça", "uva")

#leitura de da tupla
        for fruta in frutas:
            print(fruta)

#Lista
            nomes = ["fabio", "lucas", "vitora"]
#inserir novo item de lista
            nomes.append("fulano")

#leitura de lista
            for nome in nomes:
                print(f"Nome: ${nomes}")

#dicionario
funcionario = {
    "nome": "fulano",
    "cargo": "Analista sr",
    "Salario":8500.00
    }
print(funcionario ["nome"])
