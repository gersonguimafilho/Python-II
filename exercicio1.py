#guardar informações de classe  em um lista
class Pessoas:
   seq = 0
   pessoas = []

   def __init__(self, nome, datansc,cpf, filiacao1, filiacao2):
       self.id = None
       self.nome = nome
       self.datansc = datansc
       self.cpf = cpf
       self.filiacao1 = filiacao1
       self.filiacao2 = filiacao2

   def salvar(self):
       self.seq =+ 1
       self.id = self.seq
       self.pessoas.append(self)

   def __repr__(self):
         return "Id: {} - Nome {} - datascimento {} - CPF {} - Filiacao1 {} - filiacao 2 {}" .format(self.id, self.nome, self.datansc, self.cpf, self.filiacao1, self.filiacao2)   
   
   @classmethod
   def listar(cls):
         return cls.pessoas


pessoa1 = Pessoas("fulano", "12/12/1988", "12345566788", "fulana mae", "fulano pai")
pessoa1.salvar()
print(Pessoas.listar())