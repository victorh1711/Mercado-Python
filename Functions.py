#Imports que serão usados para deixar o programa mais intuitivo
import random
import time

#Os dois vetores base de todo o programa S_ é a prateleira e C_ o corrinho
S_ = ["Arroz", "Sal", "Leite"]
C_ = [    ]

#Função para adicionar item ao carrinho
def addItem():
    #Verifica se todos os itens já estão no carrinho e retorna ao inicio se sim
    if not S_:
        print("  A prateleira está vazia")
        print("".center(50, "-"))
        return

    print(f"\n{"ADICIONAR ITEM".center(50, "-")}")
    #Recebe o item desejado e converte em captalize()
    itemA = input("  -> Qual item você quer adicionar? ").capitalize()  

    #Executado se caso o item exista na prateleira e o adicionar ao carrinho
    if itemA in S_:
        C_.append(itemA)
        S_.remove(itemA)
        #Sinaliza ao usuário que a ação foi bem sucedida
        print(f"Item ({itemA}) adicionado ao carrinho \n")

    #Execultado se o item não existir na prateleira     
    elif itemA not in S_:
        #Sinaliza a falha no processo de adição
        print(f"O item ({itemA}) não existe na prateleira\n")
    print("".center(50, "-"))

#Função para remover itens do carrinho 
def removeItem():
    #Verifica se carrinho já está/é vazio retorna ao inicio se sim
    if not C_:
        print("  O carrinho está vazio")
        print("".center(50, "-"))
        return

    print(f"\n{"REMOVER ITEM".center(50, "-")}")
    #Recebe o item que deve ser removido e o converte em capitalize()
    itemR = input("  -> Qual item você quer remover? ").capitalize()

    #Execultado se o item existir no carrinho e remove-o 
    if itemR in C_:
        S_.insert(0, itemR)
        C_.remove(itemR)
        #Sinaliza ao usuário que a ação foi bem sucedida
        print(f"Item ({itemR}) removido do carrinho\n")

    #Execultado se o item não existir no carrinho
    elif itemR not in C_:
        #Sinaliza erro na remoção do item 
        print(f"O item ({itemR}) não existe no carrinho\n")
    print("".center(50, "-"))

#Função para listar os preços usando a biblioteca Random
#Array para armazenar os preços
array_precos = []

#Preenche o arrya com valores aleatorios
for l in range(10):
        num_ram = random.randint(5, 15)
        array_precos.append(num_ram)

#Cria uma biblioteca para associar um item a um valor e não permitir alterções 
precos_d = {}
for k in S_:
    #Faz uma escolha aleatória dentro do array
    price = random.choice(array_precos)
    #Associa um item a um preço
    precos_d[k] = price

#Função para definir os preços uma vez 
def listPrices():
    print(f"\n{"PREÇOS".center(50, "-")}")
    for k,price in precos_d.items():
        #Mostra o preço dos itens
        print(f"[{k} R${price}]")
    print("".center(50, "-"))

#Função para encerrar o programa, mostrando os item comprados e o preço total
def finishsystem():
    #Impede o usuário de finalizar o programa sem nenhum item na prateleira
    if not C_:
        print("Sem itens comprados")
        print("".center(50, "-"))
        return

    print(f"\n{"FINALIZANDO".center(50, "-")}")
    #Mostra os itens comprados
    print(f"ITENS COMPRADOS: [{" - ".join(C_)}] ")
    #Variavel para armazenar o valor da compra
    total = 0 

    for item in C_:
        if item in precos_d:
            total += precos_d[item]
    #Mostra o valor final da compra
    print(f"VALOR DA COMPRA: R${total}")
    print("...")



