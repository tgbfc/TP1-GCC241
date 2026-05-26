# ============================================================
# conversor.py
#
# Núcleo do sistema de conversão entre bases.
#
# IMPORTANTE:
# NÃO usa:
# - bin()
# - oct()
# - hex()
# - int(valor, base)
# - format()
#
# Todas as conversões são implementadas manualmente.
# ============================================================

DIGITOS = "0123456789ABCDEF"


# ------------------------------------------------------------
# Converte caractere para valor numérico
# Ex:
# 'A' -> 10
# 'F' -> 15
# '7' -> 7
# ------------------------------------------------------------
def char_para_valor(c):

    c = c.upper()

    for i in range(len(DIGITOS)):
        if DIGITOS[i] == c:
            return i

    return -1


# ------------------------------------------------------------
# Converte valor numérico para caractere
# Ex:
# 10 -> 'A'
# 15 -> 'F'
# ------------------------------------------------------------
def valor_para_char(v):
    return DIGITOS[v]


# ------------------------------------------------------------
# Verifica se um número pertence à base
# ------------------------------------------------------------
def validar_numero(numero, base):

    numero = numero.upper().replace(",", ".")

    pontos = 0

    for c in numero:

        if c == '.':
            pontos += 1

            if pontos > 1:
                return False

            continue

        valor = char_para_valor(c)

        if valor < 0 or valor >= base:
            return False

    return True


# ------------------------------------------------------------
# Converte parte inteira de qualquer base para decimal
# ------------------------------------------------------------
def inteiro_para_decimal(numero, base):

    decimal = 0
    potencia = 0

    for i in range(len(numero) - 1, -1, -1):

        valor = char_para_valor(numero[i])

        decimal += valor * (base ** potencia)

        potencia += 1

    return decimal


# ------------------------------------------------------------
# Converte parte fracionária para decimal
# ------------------------------------------------------------
def fracao_para_decimal(fracao, base):

    decimal = 0.0
    potencia = -1

    for c in fracao:

        valor = char_para_valor(c)

        decimal += valor * (base ** potencia)

        potencia -= 1

    return decimal


# ------------------------------------------------------------
# Converte número completo para decimal
# ------------------------------------------------------------
def base_para_decimal(numero, base):

    numero = numero.upper().replace(",", ".")

    if not validar_numero(numero, base):
        raise ValueError("Número inválido para a base informada.")

    if '.' in numero:

        parte_int, parte_frac = numero.split('.')

    else:

        parte_int = numero
        parte_frac = ""

    inteiro = inteiro_para_decimal(parte_int, base)

    fracao = fracao_para_decimal(parte_frac, base)

    return inteiro + fracao


# ------------------------------------------------------------
# Decimal inteiro -> qualquer base
# Método das divisões sucessivas
# ------------------------------------------------------------
def decimal_inteiro_para_base(numero, base, trace=False):

    if numero == 0:
        return "0"

    restos = []

    while numero > 0:

        resto = numero % base

        if trace:
            print(f"{numero} / {base} = {numero // base} resto {resto}")

        restos.append(valor_para_char(resto))

        numero //= base

    restos.reverse()

    return ''.join(restos)


# ------------------------------------------------------------
# Decimal fracionário -> qualquer base
# Método das multiplicações sucessivas
# ------------------------------------------------------------
def decimal_fracao_para_base(fracao, base, limite=16, trace=False):

    resultado = ""

    contador = 0

    while fracao > 0 and contador < limite:

        fracao *= base

        parte_inteira = int(fracao)

        resultado += valor_para_char(parte_inteira)

        if trace:
            print(f"{fracao} -> {parte_inteira}")

        fracao -= parte_inteira

        contador += 1

    return resultado


# ------------------------------------------------------------
# Decimal -> qualquer base
# ------------------------------------------------------------
def decimal_para_base(numero, base, trace=False):

    inteiro = int(numero)

    fracao = numero - inteiro

    parte_int = decimal_inteiro_para_base(inteiro, base, trace)

    if fracao == 0:
        return parte_int

    parte_frac = decimal_fracao_para_base(fracao, base, 16, trace)

    return parte_int + "." + parte_frac


# ------------------------------------------------------------
# Conversão genérica
# ------------------------------------------------------------
def converter(numero, base_origem, base_destino, trace=False):

    decimal = base_para_decimal(numero, base_origem)

    return decimal_para_base(decimal, base_destino, trace)


# ============================================================
# CONVERSÕES DIRETAS VIA BINÁRIO
# (sem passar pelo decimal)
# ============================================================

BINARIO_3 = {
    "000": "0",
    "001": "1",
    "010": "2",
    "011": "3",
    "100": "4",
    "101": "5",
    "110": "6",
    "111": "7"
}

BINARIO_4 = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F"
}


# ------------------------------------------------------------
# Octal -> Binário
# ------------------------------------------------------------
def octal_para_binario(octal):

    resultado = ""

    for c in octal:

        valor = char_para_valor(c)

        bin3 = ""

        for _ in range(3):

            bin3 = str(valor % 2) + bin3

            valor //= 2

        resultado += bin3

    return resultado.lstrip("0") or "0"


# ------------------------------------------------------------
# Hexadecimal -> Binário
# ------------------------------------------------------------
def hexadecimal_para_binario(hexadecimal):

    resultado = ""

    for c in hexadecimal:

        valor = char_para_valor(c)

        bin4 = ""

        for _ in range(4):

            bin4 = str(valor % 2) + bin4

            valor //= 2

        resultado += bin4

    return resultado.lstrip("0") or "0"


# ------------------------------------------------------------
# Binário -> Octal
# ------------------------------------------------------------
def binario_para_octal(binario):

    while len(binario) % 3 != 0:
        binario = "0" + binario

    resultado = ""

    for i in range(0, len(binario), 3):

        grupo = binario[i:i+3]

        resultado += BINARIO_3[grupo]

    return resultado.lstrip("0") or "0"


# ------------------------------------------------------------
# Binário -> Hexadecimal
# ------------------------------------------------------------
def binario_para_hexadecimal(binario):

    while len(binario) % 4 != 0:
        binario = "0" + binario

    resultado = ""

    for i in range(0, len(binario), 4):

        grupo = binario[i:i+4]

        resultado += BINARIO_4[grupo]

    return resultado.lstrip("0") or "0"


# ------------------------------------------------------------
# Octal -> Hexadecimal
# via binário
# ------------------------------------------------------------
def octal_para_hexadecimal(octal):

    binario = octal_para_binario(octal)

    return binario_para_hexadecimal(binario)


# ------------------------------------------------------------
# Hexadecimal -> Octal
# via binário
# ------------------------------------------------------------
def hexadecimal_para_octal(hexadecimal):

    binario = hexadecimal_para_binario(hexadecimal)

    return binario_para_octal(binario)


# ------------------------------------------------------------
# Calculadora de máximos
# ------------------------------------------------------------
def maximo_bits(k):

    valor = (2 ** k) - 1

    return {
        "decimal": str(valor),
        "binario": decimal_para_base(valor, 2),
        "octal": decimal_para_base(valor, 8),
        "hexadecimal": decimal_para_base(valor, 16)
    }