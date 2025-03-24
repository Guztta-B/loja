print('Bem-Vindo a area de cadastro')
nome = input('Insira seu nome: ')
senha = input('Insira sua senha: ')
email= input('Insira seu email: ')

print('Confira se estão corretos')
print(f'''
Nome: {nome}
Senha: {senha}
email: {email}
      ''')

opcao1 = ('Sim')
opcao2 = ('Nao')
opcao = input('Os dados estão corretos? ') 

if opcao == opcao1: print('Obrigado pelo seu cadastro!')

else:
    print(f'''Onde está o erro? 
             opção 1: Nome
             opção 2: E-mail 
             ''') 

    ajuste1 = 1
    ajuste2 = 2
    ajuste = int(input('Insira o número da opção: '))  

    if ajuste == ajuste1:
        novonome = input('Coloque seu novo nome: ')
        nome = novonome 

    else: 
        novoemail = input('Insira seu novo e-mail: ')
        email = novoemail 

    print('Confira se estão corretos')
    print(f'''
Nome: {nome}
E-mail: {email} 
''')  
    print('Obrigado pelo seu cadastro!!!')
produtos =  ['GABINETE', 'GBRAM','TECLADO', 'MOUSE']
valores  =  [500.0,200.00,200.00,150.50]
carrinho = []
meu_valores = []

produto1 =  int(input(f'''
0 - GABINETE
1 - GBRAM 
2 - TECLADO
3 - MOUSE
 '''))

produto2 = int(input(f'''
0 - GABINETE
1 - GBRAM 
2 - TECLADO
3 - MOUSE
'''))


carrinho = [produtos[produto1], produtos[produto2]]
meu_valores = [valores[produto1], valores[produto2]]
SOMA =  sum(meu_valores)

print(f'''
.................................
CUPOM

1 - {produtos[produto1]} R$ {valores[produto1]:.2f}
2 - {produtos[produto2]} R$ {valores[produto2]:.2f}

.................................
R$ {SOMA:.2f}

''')
print(f'''Metodos de pagamentos aceitos: 
         1 - PIX
         2 - Cartão
         3 - Dinheiro
         ''')

pagamento = input('Qual será o método de pagamento? (1/2/3): ')

if pagamento == '1': 
    print('Gerando QR code...')
elif pagamento == '2': 
    print('Insira os dados do seu cartão')
elif pagamento == '3': 
    print('Gerando boleto...')
else:
    print('Método de pagamento inválido.')

print('Pagamento concluído! Volte sempre!')