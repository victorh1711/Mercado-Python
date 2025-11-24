#Imports para usar as funções de Functions.py 
import time
import Functions

#Mensagem de inicio do programa
print(f"{"fazendo compras".upper().center(50, "_")}\n")

#while loop para permitir o funcionamento constante
while True:
    #Mostra a prateleira, definida e importa em Function.py
    print(f"PRATELEIRA: {" - ".join(Functions.S_)} ".center(50, " "))
    
    #Mostra o carrinho, definido e importado de Functions.py
    print(f"CARRINHO: {" - ".join(Functions.C_)} ".center(50, " "))

    #Mostra as opções de função e recebe a função a ser efetuada
    print(f"\n1. ADICIONAR\n2.  REMOVER\n3.  PREÇOS\n4. FINALIZAR")
    action = input("  -> Escolha o que quer fazer: ")

    #Inicia a função de adicionar item caso a entrada seja '1'
    if action == "1":
        Functions.addItem()

    #Inicia a função de remover item caso a entrada seja '2'
    elif action == "2":
        Functions.removeItem()

    #Inicia a função de listar preços caso a entrada seja '3'
    elif action == "3":
        Functions.listPrices()

    #Inicia a função que encerrar a programa caso a entrada seja '4'
    elif action == "4":
        Functions.finishsystem()
        #Finaliza o programa após a execução da função
        break
    
    #Trata de possíveis intradas invalidas em choice
    else:
        print("".center(50, "-"))
        




