class usuario:
    def __init__(self, nome, telefone, idade, sexo, endereco):
        self.nome=nome
        self.telefone=telefone
        self.idade=idade
        self.sexo=sexo
        self.endereco=endereco
        self.cadastro=False
    def cadastrok(self):
        if (self.cadastro==True):
            print('cadastro ok')
        else:
            self.cadastro = True
            
