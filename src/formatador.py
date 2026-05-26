# ============================================================
# formatador.py
#
# Responsável por:
# - impressão organizada
# - modo trace / passo-a-passo
# - menus amigáveis
# - exibição dos máximos
# ============================================================


# ------------------------------------------------------------
# Cabeçalhos
# ------------------------------------------------------------
def titulo(texto):

    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


# ------------------------------------------------------------
# Resultado simples
# ------------------------------------------------------------
def mostrar_resultado(
        numero,
        origem,
        destino,
        resultado
):

    titulo("RESULTADO")

    print(
        f"{numero} (base {origem})"
    )

    print("↓")

    print(
        f"{resultado} (base {destino})"
    )


# ------------------------------------------------------------
# Resultado batch
# ------------------------------------------------------------
def mostrar_batch(
        registros,
        resultados
):

    titulo("MODO BATCH")

    print(
        f"Entradas processadas: "
        f"{len(registros)}"
    )

    print(
        f"Resultados gravados."
    )


# ------------------------------------------------------------
# Impressão do trace
# ------------------------------------------------------------
def mostrar_trace_inicio():

    titulo(
        "PASSO-A-PASSO DA CONVERSÃO"
    )

    print(
        "\nAcompanhe o algoritmo:"
    )


# ------------------------------------------------------------
# Quiz
# ------------------------------------------------------------
def mostrar_quiz_inicio():

    titulo("QUIZ DE BASES")

    print(
        "Responda as conversões."
    )

    print()


def mostrar_pergunta(
        indice,
        total,
        numero,
        origem,
        destino
):

    print(
        f"\n[{indice}/{total}]"
    )

    print(
        f"Converter:"
    )

    print(
        f"{numero} "
        f"(base {origem}) "
        f"→ base {destino}"
    )


def mostrar_correto():

    print(
        "✓ Correto!"
    )


def mostrar_errado(
        resposta,
        correto
):

    print(
        f"✗ Errado."
    )

    print(
        f"Sua resposta: {resposta}"
    )

    print(
        f"Correto: {correto}"
    )


def mostrar_placar(
        pontos,
        total
):

    titulo("PLACAR FINAL")

    print(
        f"Acertos: {pontos}/{total}"
    )

    porcentagem = (
        pontos / total
    ) * 100

    print(
        f"Aproveitamento: "
        f"{porcentagem:.1f}%"
    )


# ------------------------------------------------------------
# Máximos
# ------------------------------------------------------------
def mostrar_maximos(
        k,
        dados
):

    titulo(
        f"MAIOR VALOR "
        f"REPRESENTÁVEL "
        f"COM {k} BITS"
    )

    print()

    print(
        "Decimal:"
    )

    print(
        dados["decimal"]
    )

    print()

    print(
        "Binário:"
    )

    print(
        dados["binario"]
    )

    print()

    print(
        "Octal:"
    )

    print(
        dados["octal"]
    )

    print()

    print(
        "Hexadecimal:"
    )

    print(
        dados["hexadecimal"]
    )


# ------------------------------------------------------------
# Erros
# ------------------------------------------------------------
def mostrar_erro(erro):

    titulo("ERRO")

    print(
        str(erro)
    )


# ------------------------------------------------------------
# Encerramento
# ------------------------------------------------------------
def mostrar_saida():

    titulo(
        "Programa encerrado."
    )


# ------------------------------------------------------------
# Menu rápido
# ------------------------------------------------------------


# ------------------------------------------------------------
# Linha divisória
# ------------------------------------------------------------
def linha():

    print(
        "-" * 60
    )