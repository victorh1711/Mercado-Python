import time
import function

print(f"{"fazendo compras".upper().center(50, "_")}\n")

while True:

    print(f"PRATELEIRA: {" - ".join(function.S_)} ".center(50, " "))
    print(f"CARRINHO: {" - ".join(function.C_)} ".center(50, " "))
    print(f"\n1. ADICIONAR\n2.  REMOVER\n3.  PREÇOS\n4. FINALIZAR")
    action = input("  -> Escolha o que quer fazer: ")

    if action == "1":
        function.addItem()

    elif action == "2":
        function.removeItem()

    elif action == "3":
        function.listPrices()

    elif action == "4":
        function.finishsystem()
    
    else:
        print("".center(50, "-"))
        




