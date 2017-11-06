nome = input("Insira o nome: ")

if len(nome) < 6:
    print("Nome invalido")
    exit(0)

email = input("Insira o email: ")
cep = input("Insira o CEP: ")

with open('cadastro.txt', 'a') as f:
    f.write("Nome: %s | Email: %s | CEP: %s\n" % (nome,email,cep))

linha = input("Qual linha deseja visualizar? ")

with open('cadastro.txt', 'r') as f:
    linhas = f.readlines()
    print( linhas[int(linha)] )