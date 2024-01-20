#enquanto
"""
saldo =100

while (saldo != 0):
    print('Saldo', saldo)
    saque=int(input("Valor Saque:"))
    if saque > saldo:
        print("você não tem grana o suficiente!")
    else:
        print("Obrigado por sacar", saque "você ainda tem")
    saldo=saldo-saque
  """ 

saldo = 100

while saldo != 0:
    print('Saldo:', saldo)
    saque = int(input("Valor Saque:"))
    if saque > saldo:
        print("Você não tem grana o suficiente!")
    else:
        print("Obrigado por sacar", saque, "você ainda tem", saldo - saque)
    saldo = saldo - saque