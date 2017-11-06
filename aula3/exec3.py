alunos = [
	{
		"nome": "Gabriel",
		"notas": [
			1,4,5,6
		]
	},
	{
		"nome": "Joao",
		"notas": [
			3,5,7,7
		]
	}
]

nome = input("Digite o nome: ")

for a in alunos:
    if a["nome"] == nome:
        total = 0
        for n in a["notas"]:
            total += n

        media = total / len(a["notas"])

        if media >= 7:
            print("APROVADO!")
        else:
            print("REPROVADO")

# ===========

for a in alunos:
    if a["nome"] == nome:
        print("A" if sum(a["notas"])/len(a["notas"]) >= 7 else "R")
