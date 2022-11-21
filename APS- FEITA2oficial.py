
alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
ROT = 13
cifra = 1
def cipher (mensagem, cifra):
    crypto = " "
    for c in mensagem:
        if c in alphabet:
            c_index = alphabet.index(c)
            crypto += alphabet[(c_index +(cifra * ROT)) % len(alphabet)]
        else:
            crypto += c
    return crypto


def criptogra(mensagem):
    return cipher(mensagem, cifra)
def decriptogra (mensagem):
    cifra2=  cifra - (cifra * 2)
    return cipher (mensagem, cifra2)


 



while True:
 usuario = ['jose', 'fabricio', 'caio', 'vinicius']
 senha = ['123456']

 login = str(input("Digite o login:  "))
 if login in usuario:
  senha_usuario = str(input('Digite a senha:  '))
  if senha_usuario in senha:
        executa2 = True
    
        while executa2:
            print("-----------------------------------------")
            print('Digite 0 para sair ')
            print('Digite 1 para criptografar ')
            print('Digite 2 para descriptografar ')
            print('Digite 3 para entrar na configuração ')
            print("-----------------------------------------")
            condicao = int(input('Digite a opção escolhida '))

            if condicao == 0:
                executa2 = False
                continue
            if condicao == 1:
                print("Você escolheu a opção 1")
                print(" ")
                mensagem = str (input('Digite a frase a ser criptografada '))
                print (criptogra(mensagem) )                   
                continue

            if condicao == 2:
                print('Você escolheu a opção 2')
                print("  ")
                mensagem = str (input('Digite a frase a ser descriptografada '))
                print(decriptogra (mensagem))
                continue
            if condicao == 3:
                print('Você escolheu configuração')
                print('Digite 1 para adicionar um usuário ao sistema')
                print('Digite 2 para mudar a cifra')
                print('Digite 3 pra sair')
                print(" ")
                conf = int(input('Digite a opção de configuração '))
                if conf == 1:
                    novoU = str(input('Digite um novo usuário: '))
                    usuario.append(novoU)

                    novoS = str(input('Digite a senha do usuario:  '))
                    senha.append(novoS)
                    print("Usuários no sistema",usuario,"senhas no sistema",senha)
                    continue

                if conf == 2:
                    cifra = int(input('Digite um novo número de cifra'))
                    continue

                if conf == 3:
                    break

            else:
                print("opção inválida")
                continue

  else:
   print('senha inválida')
 else:
  print('usuario inválido')
