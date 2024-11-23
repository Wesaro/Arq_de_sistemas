import json

def bancoFunc():
    """Lê o conteúdo do arquivo dados.txt e retorna como objeto JSON."""

    with open('dados.txt', 'r') as file:
            conteudo = file.read()
            conteudoJson = json.loads(conteudo)
    return conteudoJson

def calcMedia(conteudoJson):
    if not conteudoJson:
        return 0.0

    soma = 0.0
    for item in conteudoJson:
        soma += item.get('salario', 0.0)
    
    media = soma / len(conteudoJson)
    return media

def imprimeLista(conteudoJson):
    if not conteudoJson:
        print("Nenhum dado disponível para exibir.")
        return

    for item in conteudoJson:
        print(item)

conteudoJson = bancoFunc()
if conteudoJson:
    media = calcMedia(conteudoJson)
    print(f"Média dos salários: {media:.2f}")
    imprimeLista(conteudoJson)
