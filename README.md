# TP1 — Conversor de Sistemas de Numeração

GCC241 — Introdução à Computação — 2026/1

## Integrantes

- Gabriel Santos Carvalho
- Teverson Gualberto Benfica

---

## Linguagem utilizada

Python 3

Bibliotecas utilizadas:

- math
- random
- csv
- sys

Somente bibliotecas padrão da linguagem.

---

## Objetivo do projeto

Implementar algoritmos de conversão entre sistemas numéricos sem utilizar funções prontas da linguagem para conversão de bases.

Bases suportadas:

- Binário (2)
- Octal (8)
- Decimal (10)
- Hexadecimal (16)

O programa também suporta:

- números inteiros
- números fracionários
- modo passo-a-passo
- modo batch via CSV
- quiz
- cálculo de máximos representáveis

---

## Estrutura do projeto

```text
TP1/

src/
│
├── main.py
├── parser.py
├── conversor.py
└── formatador.py

tests/
│
└── test_conversor.py

entrada_exemplo.csv

README.md
```

### Arquivos

### main.py

Arquivo principal.

Responsável por:

- menu do programa
- seleção do modo
- integração entre módulos

---

### parser.py

Responsável por:

- validar entradas
- validar bases
- validar caracteres permitidos

Exemplos:

- impedir "8" em octal
- impedir "G" em hexadecimal

---

### conversor.py

Contém os algoritmos de conversão.

Implementações principais:

- decimal → binário
- decimal → octal
- decimal → hexadecimal
- bases → decimal
- binário ↔ octal
- binário ↔ hexadecimal
- octal ↔ hexadecimal
- tratamento de parte fracionária

---

### formatador.py

Responsável pela saída do programa.

Implementa:

- exibição comum
- exibição passo-a-passo
- mensagens de erro

---

### tests/

Contém testes automatizados.

Cobertura:

- conversões válidas
- conversões inválidas
- fracionários
- validações
- casos de borda

---

## Como executar

Entre na pasta do projeto.

### Execução normal

```bash
cd TP1/src
python3 main.py
```

---

### Executar testes

```bash
cd TP1
python3 tests/test_conversor.py
```

---

## Modos disponíveis

### 1 — Conversão simples

Converte entre:

- decimal
- binário
- octal
- hexadecimal

Exemplo:

Entrada:

```text
valor: 25
origem: 10
destino: 2
```

Saída:

```text
11001
```

---

### 2 — Modo passo-a-passo

Mostra o algoritmo funcionando.

Exemplo:

Decimal → Binário.

```text
25 ÷ 2 = 12 resto 1
12 ÷ 2 = 6 resto 0
6 ÷ 2 = 3 resto 0
3 ÷ 2 = 1 resto 1
1 ÷ 2 = 0 resto 1

Resultado: 11001
```

---

### 3 — Modo batch (CSV)

Lê arquivo CSV.

Formato:

```csv
valor;base_origem;base_destino
25;10;2
1111;2;10
FF;16;10
```

Gera:

```csv
valor;base_origem;resultado;base_destino
25;10;11001;2
1111;2;15;10
FF;16;255;10
```

---

### 4 — Quiz

Gera desafios aleatórios.

Possui 5 níveis de dificuldade.

O usuário responde.

O programa:

- verifica resposta
- informa acerto/erro
- mantém pontuação

---

### 5 — Máximos representáveis

Dado k bits:

calcula:

```text
2^k − 1
```

Mostra simultaneamente em:

- binário
- octal
- decimal
- hexadecimal

Exemplo:

Entrada:

```text
8
```

Saída:

```text
Binário: 11111111
Octal: 377
Decimal: 255
Hexadecimal: FF
```

---

## Restrições respeitadas

O projeto NÃO utiliza funções proibidas.

Não foram usados:

### Python vetados

- bin()
- oct()
- hex()
- int(valor, base)
- format()
- f"{n:b}"

Todas as conversões foram implementadas manualmente usando:

- loops
- aritmética básica
- manipulação de strings

---

## Exemplos

### Decimal → Hexadecimal

Entrada:

```text
255
10
16
```

Saída:

```text
FF
```

---

### Binário → Decimal

Entrada:

```text
101101
2
10
```

Saída:

```text
45
```

---

### Fracionário

Entrada:

```text
10.625
10
2
```

Saída:

```text
1010.101
```

---

## Limitações conhecidas

- resultado fracionário limitado a 16 casas
- truncamento informado explicitamente
- aceita "." e "," como separador decimal

---

## Testes realizados

Cobertura mínima:

- decimal ↔ binário
- decimal ↔ octal
- decimal ↔ hexadecimal
- binário ↔ octal
- binário ↔ hexadecimal
- octal ↔ hexadecimal
- validação de entrada
- fracionários
- batch CSV
- quiz

Total:

35 testes automatizados.

---

## Vídeo de demonstração

Link:

INSERIR LINK AQUI

---

## Observações finais

Este projeto foi desenvolvido para fins didáticos na disciplina GCC241 — Introdução à Computação.

Todos os algoritmos de conversão foram implementados manualmente conforme exigido no enunciado.# pequeno ajuste
