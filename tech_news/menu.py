import sys


def analyzer_menu():
    opt = [
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    ]
    msg = {
        0: "Digite quantas notícias serão buscadas:",
        1: "Digite o título:",
        2: "Digite a data no formato aaaa-mm-dd:",
        3: "Digite a fonte:",
        4: "Digite a categoria:",
    }

    for x in opt:
        print(x)

    try:
        result = int(input('Digite a opção:'))
        print(msg[result])
    except (KeyError, ValueError):
        sys.stderr.write("Opção inválida")

# Agradecimentos especiais ao meu colega Joao Pistorio da turma 10-B que me
# ajudou a realizar esse projeto dando dicas e permitindo consultas em seu PR.
# PR Joao: https://github.com/tryber/sd-010-b-tech-news/pull/98
