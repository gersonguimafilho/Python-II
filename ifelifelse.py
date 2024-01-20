#vamos tirar a média de uma materia

materia = input("escreva a materia:")

nota1 = float(input("escreva a primeira nota:"))
nota2 = float(input("escreva a segunda nota:"))
nota3 = float(input("escreva a terceira nota:"))
nota4 = float(input("escreva a quarta nota:"))

resultado = (nota1+nota2+nota3+nota4)/4

print("a sua nota média na materia de", materia, "foi de", resultado)

if resultado > 7:
    print("voce foi aprovado")
elif resultado > 5 < 6:
    print("voce esta de recuperação")
else:
    print("voce esta reprovado reprovado")