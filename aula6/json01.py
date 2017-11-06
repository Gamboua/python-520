import json
# from json import dumps

aluno = {
    "nome": "gabriel",
    "curso": "python"
}

string = json.dumps(aluno)

print(type(json.loads(string)))
