import csv

with open('alunos.csv', 'r') as csvfile:
    arquivo = csv.reader(csvfile, delimiter=';')

    for a in arquivo:
        print(a)

with open('alunos.csv', 'a') as csvfile:
    arquivo = csv.writer(csvfile, delimiter=';')
    arquivo.writerow(['joao', 'joao@joao'])