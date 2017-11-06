maior = 0

dicio = {
    1: "primeiro",
    2: "segundo",
    3: "terceiro"
}

for i in range(1,4,1):
    num = int(input("Digite o %s número: " % dicio[i]))
    if num > maior:
        maior = num

print("O maior número é: %s" % maior)
