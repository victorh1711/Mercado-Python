from price import*
import time
shelf=['arroz']
cart=[]

start=input('Ola, vamos ás compras?(sim/nao)').lower()
if start=='nao' or start=='não':
    print('Talvez outro dia')  
    time.sleep(2)
    print('saindo...')
elif start=='sim':
    print('Otimo, vamos lá...')
    time.sleep(1)

    
    if not cart:
     print('Esse é seu carrinho:',cart,',ele está vazio no momento.')
     print('Essa são os itens desponiveis na prateleira:',shelf)

    elif len(cart)!=0: 
      print('Esse é seu carrrinho',cart)
      print('Esse são os itens disponiveis na prateleira:',shelf)

    while True:
     time.sleep(0.15)
     print('O que você quer fazer:')
     time.sleep(0.1)
     print('1.adicionar')
     time.sleep(0.1)
     print('2.remover')
     time.sleep(0.1)
     print('3.sair')

     choice=input('Digite sua escolha:')
     if choice=='1':
        if not shelf:
           print('Não há mais itens na prateleira.')
           time.sleep(0.15)
           c=input('Já podemos finalizar?(sim/nao)').lower()

           if c=='sim':
              time.sleep(0.1)
              print('Sua compra:',cart,len(cart),'itens comprado')
              time.sleep(0.5)
              print('Saindo do sistema...')
              break
           elif c=='nao' or c=='não':
              time.sleep(0.1)
              print('Então, continuemos...')

        elif len(shelf)>0:
           time.sleep(0.2)
           add=input('Qual item você quer adicionar ao seu carrinho?').lower()
           if add not in shelf:
              time.sleep(0.15)
              print('Item não presente na prateleira, tente outro.')
           elif add in shelf:
              shelf.remove(add)
              cart.insert(0,add)
              time.sleep(0.1)
              print('Prateleira:',shelf)
              time.sleep(0.1)
              print('Esse é seu carrinho:',cart)

     elif choice=='2':
        if not cart:
           time.sleep(0.15)
           print('Seu carrinho já está vazio, não há nada a se retirar.')

        elif len(cart)>0:
           time.sleep(0.2)
           rev=input('Que item você quer voltar para a prateleira?').lower()
           if rev not in cart:
             time.sleep(0.15)
             print('este item não está no seu carrinho.')
           elif rev in cart:
              cart.remove(rev)
              shelf.insert(0,rev)
              time.sleep(0.1)
              print('Prateleira:',shelf)
              time.sleep(0.1)
              print('Esse é seu carrinho:',cart)

     elif choice=='3':
        time.sleep(0.2)
        print('Obrigado.')
        time.sleep(0.1)
        print('Resultado das compras:',cart,len(cart),'itens comprados.')
        time.sleep(0.5)
        print('Saindo do sistema...')
        time.sleep(2)
        break 
            