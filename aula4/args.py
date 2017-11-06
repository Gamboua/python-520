def exemplo(*args):
    print(args)

exemplo('a', 'b', 'c')

def dicionario(**kwargs):
    print(kwargs)

dicionario(nome='gabriel', email='gabriel@4linux.com')

def juntos(*args, **kwargs):
    args[1]
    kwargs['nome']

juntos('a','b','c')