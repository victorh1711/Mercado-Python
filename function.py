import random
import sys

S_ = ["Arroz", "Sal", "Leite"]
C_ = [    ]

def addItem():
    if not S_:
        print("  A prateleira está vazia")
        print("".center(50, "-"))
        return

    print(f"\n{"ADICIONAR ITEM".center(50, "-")}")
    itemA = input("  -> Qual item você quer adicionar? ").capitalize()  

    if itemA in S_:
        C_.append(itemA)
        S_.remove(itemA)
        print(f"Item ({itemA}) adicionado ao carrinho \n")
  
    elif itemA not in S_:
        print(f"O item ({itemA}) não existe na prateleira\n")
    print("".center(50, "-"))

def removeItem():
    if not C_:
        print("  O carrinho está vazio")
        print("".center(50, "-"))
        return

    print(f"\n{"REMOVER ITEM".center(50, "-")}")
    itemR = input("  -> Qual item você quer remover? ").capitalize()


    if itemR in C_:
        S_.insert(0, itemR)
        C_.remove(itemR)
        print(f"Item ({itemR}) removido do carrinho\n")

    elif itemR not in C_:
        print(f"O item ({itemR}) não existe no carrinho\n")
    print("".center(50, "-"))


array_precos = []

for l in range(10):
        num_ram = random.randint(5, 15)
        array_precos.append(num_ram)

precos_d = {}
for k in S_:
    price = random.choice(array_precos)
    precos_d[k] = price

def listPrices():
    print(f"\n{"PREÇOS".center(50, "-")}")
    for k,price in precos_d.items():

        print(f"[{k} R${price}]")
    print("".center(50, "-"))


def finishsystem():
    if not C_:
        print("Sem itens comprados")
        print("".center(50, "-"))
        return

    print(f"\n{"FINALIZANDO".center(50, "-")}")
    print(f"ITENS COMPRADOS: [{" - ".join(C_)}] ")
    total = 0 

    for item in C_:
        if item in precos_d:
            total += precos_d[item]
    print(f"VALOR DA COMPRA: R${total}")
    print("...")
    sys.exit()