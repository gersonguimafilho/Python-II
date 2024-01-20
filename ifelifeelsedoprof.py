#notas - media - situação

nota1 = float(input("digite a nota 1"))
nota2 = float(input("digite a nota 2"))
nota3 = float(input("digite a nota 3"))
nota4 = float(input("digite a nota 4"))

#media = (nota1+nota2+nota3+nota4)//4

soma=nota1+nota2+nota3+nota4
media = soma / 4

#se / senaose / senao 
if (media >=7):
    print("aprovado")
elif (media >=4 or media <= 6):
    print("recuperação")
else:
    print("reprovado")
