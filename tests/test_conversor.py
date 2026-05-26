# ============================================================
# test_conversor.py
#
# Suíte de testes automáticos
#
# Executar:
#
# python -m unittest tests.test_conversor
#
# Cobertura:
# F1–F10
# + validações
# + fracionários
# + conversões diretas
# ============================================================

import unittest

from src.conversor import *


class TestConversor(unittest.TestCase):

    # -------------------------
    # VALIDAÇÃO
    # -------------------------

    def test_valid_binario(self):
        self.assertTrue(
            validar_numero("10101",2)
        )

    def test_invalid_binario(self):
        self.assertFalse(
            validar_numero("10201",2)
        )

    def test_valid_octal(self):
        self.assertTrue(
            validar_numero("765",8)
        )

    def test_invalid_octal(self):
        self.assertFalse(
            validar_numero("789",8)
        )

    def test_valid_hex(self):
        self.assertTrue(
            validar_numero("AF2",16)
        )

    def test_invalid_hex(self):
        self.assertFalse(
            validar_numero("AFG",16)
        )

    # -------------------------
    # BASE -> DECIMAL
    # -------------------------

    def test_bin_decimal(self):
        self.assertEqual(
            base_para_decimal("1010",2),
            10
        )

    def test_octal_decimal(self):
        self.assertEqual(
            base_para_decimal("17",8),
            15
        )

    def test_hex_decimal(self):
        self.assertEqual(
            base_para_decimal("FF",16),
            255
        )

    # -------------------------
    # DECIMAL -> BASE
    # -------------------------

    def test_decimal_binario(self):
        self.assertEqual(
            decimal_para_base(10,2),
            "1010"
        )

    def test_decimal_octal(self):
        self.assertEqual(
            decimal_para_base(64,8),
            "100"
        )

    def test_decimal_hex(self):
        self.assertEqual(
            decimal_para_base(255,16),
            "FF"
        )

    # -------------------------
    # CONVERSÃO GENÉRICA
    # -------------------------

    def test_converter_2_16(self):
        self.assertEqual(
            converter("11111111",2,16),
            "FF"
        )

    def test_converter_16_2(self):
        self.assertEqual(
            converter("FF",16,2),
            "11111111"
        )

    def test_converter_8_10(self):
        self.assertEqual(
            converter("17",8,10),
            "15"
        )

    def test_converter_10_8(self):
        self.assertEqual(
            converter("64",10,8),
            "100"
        )

    # -------------------------
    # FRACIONÁRIOS
    # -------------------------

    def test_fracao_bin_decimal(self):

        valor = base_para_decimal(
            "1010.1",
            2
        )

        self.assertAlmostEqual(
            valor,
            10.5,
            places=4
        )

    def test_fracao_decimal_bin(self):

        resultado = decimal_para_base(
            10.625,
            2
        )

        self.assertTrue(
            resultado.startswith(
                "1010.101"
            )
        )

    def test_fracao_hex_decimal(self):

        valor = base_para_decimal(
            "A.8",
            16
        )

        self.assertAlmostEqual(
            valor,
            10.5,
            places=4
        )

    # -------------------------
    # BIN ↔ OCTAL
    # -------------------------

    def test_bin_octal(self):
        self.assertEqual(
            binario_para_octal(
                "111111"
            ),
            "77"
        )

    def test_octal_bin(self):
        self.assertEqual(
            octal_para_binario(
                "77"
            ),
            "111111"
        )

    # -------------------------
    # BIN ↔ HEX
    # -------------------------

    def test_bin_hex(self):
        self.assertEqual(
            binario_para_hexadecimal(
                "11111111"
            ),
            "FF"
        )

    def test_hex_bin(self):
        self.assertEqual(
            hexadecimal_para_binario(
                "FF"
            ),
            "11111111"
        )

    # -------------------------
    # OCT ↔ HEX
    # -------------------------

    def test_octal_hex(self):
        self.assertEqual(
            octal_para_hexadecimal(
                "377"
            ),
            "FF"
        )

    def test_hex_octal(self):
        self.assertEqual(
            hexadecimal_para_octal(
                "FF"
            ),
            "377"
        )

    # -------------------------
    # MÁXIMOS
    # -------------------------

    def test_maximo_8bits(self):

        dados = maximo_bits(8)

        self.assertEqual(
            dados["decimal"],
            "255"
        )

    def test_maximo_binario(self):

        dados = maximo_bits(4)

        self.assertEqual(
            dados["binario"],
            "1111"
        )

    # -------------------------
    # CHAR ↔ VALOR
    # -------------------------

    def test_char_valor(self):

        self.assertEqual(
            char_para_valor("A"),
            10
        )

    def test_valor_char(self):

        self.assertEqual(
            valor_para_char(15),
            "F"
        )

    # -------------------------
    # EDGE CASES
    # -------------------------

    def test_zero_bin(self):
        self.assertEqual(
            decimal_para_base(0,2),
            "0"
        )

    def test_zero_hex(self):
        self.assertEqual(
            decimal_para_base(0,16),
            "0"
        )

    def test_unidade(self):
        self.assertEqual(
            converter(
                "1",
                10,
                2
            ),
            "1"
        )

    def test_maior_hex(self):
        self.assertEqual(
            converter(
                "FFFF",
                16,
                10
            ),
            "65535"
        )

    def test_decimal_grande(self):
        self.assertEqual(
            decimal_para_base(
                1024,
                2
            ),
            "10000000000"
        )

    def test_binario_longo(self):
        self.assertEqual(
            base_para_decimal(
                "10000000000",
                2
            ),
            1024
        )


if __name__ == "__main__":

    unittest.main()