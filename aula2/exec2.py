maior = 0
######
num = int(input("Digite o primeiro número: "))

maior = num if int(input("Digite o primeiro número: ")) > maior else maior

######

num2 = int(input("Digite o segundo número: "))

maior = num2 if num2 > maior else maior

######

num3 = int(input("Digite o terceiro número: "))

maior = num3 if num3 > maior else maior
######
print("O maior número é: %s" % maior)