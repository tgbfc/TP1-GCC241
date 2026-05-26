# ============================================================
# parser.py
#
# Responsável por:
# - leitura de entrada
# - validação de bases
# - modo batch CSV
# - leitura segura de parâmetros
# ============================================================

import csv
from conversor import validar_numero


BASES_VALIDAS = [2, 8, 10, 16]


# ------------------------------------------------------------
# Verifica se a base existe
# ------------------------------------------------------------
def validar_base(base):

    return base in BASES_VALIDAS


# ------------------------------------------------------------
# Valida conjunto completo da conversão
# ------------------------------------------------------------
def validar_entrada(numero, origem, destino):

    if not validar_base(origem):
        raise ValueError(
            f"Base origem inválida: {origem}"
        )

    if not validar_base(destino):
        raise ValueError(
            f"Base destino inválida: {destino}"
        )

    if not validar_numero(numero, origem):
        raise ValueError(
            f"Número inválido para base {origem}"
        )

    return True


# ------------------------------------------------------------
# Leitura CLI simples
# ------------------------------------------------------------
def ler_conversao():

    numero = input(
        "Valor: "
    ).strip()

    origem = int(
        input("Base origem (2/8/10/16): ")
    )

    destino = int(
        input("Base destino (2/8/10/16): ")
    )

    validar_entrada(
        numero,
        origem,
        destino
    )

    return numero, origem, destino


# ------------------------------------------------------------
# Pergunta Sim/Não
# ------------------------------------------------------------
def perguntar_sn(msg):

    while True:

        resposta = input(
            msg
        ).strip().lower()

        if resposta in ['s', 'sim']:
            return True

        if resposta in ['n', 'nao', 'não']:
            return False

        print(
            "Digite S ou N."
        )


# ------------------------------------------------------------
# Lê inteiro positivo
# ------------------------------------------------------------
def ler_inteiro_positivo(msg):

    while True:

        try:

            valor = int(
                input(msg)
            )

            if valor > 0:
                return valor

            print(
                "Digite valor > 0."
            )

        except:

            print(
                "Entrada inválida."
            )


# ------------------------------------------------------------
# Lê modo do programa
# ------------------------------------------------------------
def ler_modo():

    print("\n======== MENU ========")
    print("1 - Conversão")
    print("2 - Passo-a-passo")
    print("3 - Batch CSV")
    print("4 - Quiz")
    print("5 - Máximos")
    print("0 - Sair")

    return input(
        "\nEscolha: "
    ).strip()


# ------------------------------------------------------------
# Lê nome de arquivo CSV
# ------------------------------------------------------------
def ler_arquivo_csv():

    nome = input(
        "Arquivo CSV: "
    ).strip()

    if nome == "":
        raise ValueError(
            "Nome vazio."
        )

    return nome


# ------------------------------------------------------------
# Carrega CSV
#
# formato:
# valor;base_origem;base_destino
# ------------------------------------------------------------
def carregar_csv(nome_arquivo):

    registros = []

    with open(
        nome_arquivo,
        'r',
        encoding='utf-8'
    ) as arq:

        leitor = csv.reader(
            arq,
            delimiter=';'
        )

        next(leitor, None)

        for linha in leitor:

            if len(linha) != 3:

                print(
                    "Linha ignorada:",
                    linha
                )

                continue

            numero = linha[0].strip()

            origem = int(
                linha[1]
            )

            destino = int(
                linha[2]
            )

            try:

                validar_entrada(
                    numero,
                    origem,
                    destino
                )

                registros.append(
                    (
                        numero,
                        origem,
                        destino
                    )
                )

            except Exception as erro:

                print(
                    f"Erro CSV: {erro}"
                )

    return registros


# ------------------------------------------------------------
# Salva CSV
#
# valor;base_origem;resultado;base_destino
# ------------------------------------------------------------
def salvar_csv(
        nome_arquivo,
        resultados
):

    with open(
        nome_arquivo,
        'w',
        newline='',
        encoding='utf-8'
    ) as arq:

        escritor = csv.writer(
            arq,
            delimiter=';'
        )

         # adiciona cabeçalho
        escritor.writerow([
            "valor",
            "base_origem",
            "resultado",
            "base_destino"
        ])

        for linha in resultados:

            escritor.writerow(
                linha
            )


# ------------------------------------------------------------
# Lê parâmetros do quiz
# ------------------------------------------------------------
def ler_quiz():

    print("\n==== QUIZ ====")

    nivel = int(
        input(
            "Nível (1-5): "
        )
    )

    qtd = int(
        input(
            "Quantidade perguntas: "
        )
    )

    if nivel < 1 or nivel > 5:
        raise ValueError(
            "Nível inválido."
        )

    if qtd <= 0:
        raise ValueError(
            "Quantidade inválida."
        )

    return nivel, qtd


# ------------------------------------------------------------
# Lê k bits
# ------------------------------------------------------------
def ler_bits():

    k = ler_inteiro_positivo(
        "Quantidade de bits: "
    )

    return k