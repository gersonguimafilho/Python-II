numero_secreto= 82
total_de_tentativas= 3 

for rodada in range(1, total_de_tentativas + 1):
    print("\ntentativa {:02d} de {:02d}".format(rodada,total_de_tentativas))

    tentativa=input("tente acertar o numero de 1 a 100:)")
    print("Voce digitou:", tentativa)
    tentativa_int=int(tentativa)

    if(tentativa_int<1 or tentativa_int>100):
        print("Tentativa invalida, somentenumeros de 1 a 100")
        continue

    acerto = tentativa_int == numero_secreto

    if (acerto):
        print("boa taentativa acertou!")    
        break
    else:
        print("Não foi desta vez errou!")

