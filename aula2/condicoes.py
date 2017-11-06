idade = 18
habilitacao = True
bebado = True

if idade == 18:
    if habilitacao:
        if not bebado:
            print("Voce pode dirigir")
        else:
            print("Voce nao pode dirigir!")
    else:
        print("Voce nao pode dirigir!")
else:
    print("Voce nao pode dirigir!")

if idade >= 18 and habilitacao or not bebado:
    print("Voce pode dirigir")
else:
    print("Voce nao pode dirigir!")

if idade >= 18:
    print("Voce pode dirigir")
elif habilitacao:
    print("Voce pode dirigir")
elif not bebado:
    print("Voce pode dirigir")
else:
    print("Voce nao pode dirigir!")

if bebado is None:
    print(10)
else:
    print(20)

print( 10 if bebado is None else 20 )