# ============================================================
# main.py
#
# Programa principal.
#
# Responsável por:
# - menu
# - dispatch dos modos
# - integração completa do TP
# ============================================================

from parser import *
from conversor import *
from formatador import *

import random


# ------------------------------------------------------------
# MODO 1 — Conversão normal
# ------------------------------------------------------------
def modo_conversao():

    try:

        numero, origem, destino = ler_conversao()

        resultado = converter(
            numero,
            origem,
            destino
        )

        mostrar_resultado(
            numero,
            origem,
            destino,
            resultado
        )

    except Exception as erro:

        mostrar_erro(erro)


# ------------------------------------------------------------
# MODO 2 — Passo-a-passo
# F7
# ------------------------------------------------------------
def modo_trace():

    try:

        numero, origem, destino = ler_conversao()

        mostrar_trace_inicio()

        resultado = converter(
            numero,
            origem,
            destino,
            trace=True
        )

        mostrar_resultado(
            numero,
            origem,
            destino,
            resultado
        )

    except Exception as erro:

        mostrar_erro(erro)


# ------------------------------------------------------------
# MODO 3 — Batch CSV
# F8
# ------------------------------------------------------------
def modo_batch():

    try:

        entrada = ler_arquivo_csv()

        registros = carregar_csv(
            entrada
        )

        saida = []

        for numero, origem, destino in registros:

            resultado = converter(
                numero,
                origem,
                destino
            )

            saida.append(
                [
                    numero,
                    origem,
                    resultado,
                    destino
                ]
            )

        salvar_csv(
            "saida.csv",
            saida
        )

        mostrar_batch(
            registros,
            saida
        )

    except Exception as erro:

        mostrar_erro(erro)


# ------------------------------------------------------------
# Geração aleatória do quiz
# F9
# ------------------------------------------------------------
def gerar_exercicio(nivel):

    limites = {

        1: (1,15),
        2: (16,255),
        3: (256,1023),
        4: (1024,65535),
        5: (65536,999999)

    }

    minimo,maximo = limites[nivel]

    decimal = random.randint(
        minimo,
        maximo
    )

    bases = [2,8,10,16]

    origem = random.choice(
        bases
    )

    destino = random.choice(
        bases
    )

    while destino == origem:

        destino = random.choice(
            bases
        )

    numero = decimal_para_base(
        decimal,
        origem
    )

    resposta = decimal_para_base(
        decimal,
        destino
    )

    return (
        numero,
        origem,
        destino,
        resposta
    )


# ------------------------------------------------------------
# MODO QUIZ
# ------------------------------------------------------------
def modo_quiz():

    try:

        nivel,total = ler_quiz()

        mostrar_quiz_inicio()

        pontos = 0

        for i in range(1,total+1):

            (
                numero,
                origem,
                destino,
                correto
            ) = gerar_exercicio(
                nivel
            )

            mostrar_pergunta(
                i,
                total,
                numero,
                origem,
                destino
            )

            resposta = input(
                "Resposta: "
            ).strip().upper()

            if resposta == correto:

                mostrar_correto()

                pontos += 1

            else:

                mostrar_errado(
                    resposta,
                    correto
                )

        mostrar_placar(
            pontos,
            total
        )

    except Exception as erro:

        mostrar_erro(erro)


# ------------------------------------------------------------
# MODO MÁXIMOS
# F10
# ------------------------------------------------------------
def modo_maximos():

    try:

        k = ler_bits()

        dados = maximo_bits(
            k
        )

        mostrar_maximos(
            k,
            dados
        )

    except Exception as erro:

        mostrar_erro(erro)


# ------------------------------------------------------------
# Loop principal
# ------------------------------------------------------------
def main():

    while True:

        try:

            opcao = ler_modo()

            if opcao == '1':

                modo_conversao()

            elif opcao == '2':

                modo_trace()

            elif opcao == '3':

                modo_batch()

            elif opcao == '4':

                modo_quiz()

            elif opcao == '5':

                modo_maximos()

            elif opcao == '0':

                mostrar_saida()

                break

            else:

                print(
                    "Opção inválida."
                )

        except KeyboardInterrupt:

            print(
                "\nEncerrado pelo usuário."
            )

            break


# ------------------------------------------------------------
# Entrada do programa
# ------------------------------------------------------------
if __name__ == "__main__":

    main()