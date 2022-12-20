logs = {'user':'12345', 'user2':'123456'}

print("Gostaria de fazer Login")
print(" S para sim - N para não")
login = input("Resposta:")

if login == "S":
    Usuario = input("Usuario:")
    senha = input("Senha:")

elif login == "N":
    print("OK nos vemos na proxima!!")

if Usuario == logs[str(Usuario)] and senha == logs[str(Usuario)][str(senha)]:
    
    print("-----------------------------------")
print("Bem Vindo: {}".format(Usuario))
print("-----------------------------------")
teste = {'Ola':'Olá sou o ZikaBot, em que posso ajuda-lo?',
        'Olá':'Olá sou o ZikaBot, em que posso ajuda-lo?',
        'ola':'Olá sou o ZikaBot, em que posso ajuda-lo?',
        'olá':'Olá sou o ZikaBot, em que posso ajuda-lo?',
        'Oi':'Olá em que posso ajuda-lo?',
        'oi':'Olá em que posso ajuda-lo?',
        'Me manda um pix':'Qual sua Chave PIX',
        'me manda um pix':'Qual sua Chave PIX',
        'Como eu compro na sua loja':'Acesse:"seu link"',
        'xau': 'Muito obrigado por usar o zikaBOT',
        'qual sua loja':'Acesse minha loja pelo link: "seu link"',
        'qual o seu site':'Acesse o link para o meu perfil no instagram: "seu link"',
        'obrigado':'Ajudo em algo mais?',
        'não':'Ok, Muito obrigado por usar o zikaBOT'}

entrada = input("{}:".format(Usuario))

while entrada:
    print("-----------------------------------")
    print("ZikaBOT: {}".format(teste[str(entrada)]))
    print("-----------------------------------")
    if entrada == "xau" or entrada == "não":
        break
    else:
        entrada = input("{}:".format(Usuario))