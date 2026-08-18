#  Central de Análise de Texto e Listas | Python CLI

> **Status do Projeto:** Em andamento | **Foco:** Algoritmos, Modularização e Estrutura de Dados

Uma aplicação interativa desenvolvida em Python executada via linha de comando (CLI). O objetivo principal do projeto foi aplicar **conceitos avançados de modularização (funções/subalgoritmos)**, **manipulação de strings**, **fatiamento de listas (slicing)** e **tratamento de entradas**.

---

## Funcionalidades e Casos de Uso

| Opção | Funcionalidade | Conceito Técnico Aplicado |
| :--- | :--- | :--- |
| **01** | **Obter Extremos de Lista** | Indexação positiva/negativa (`lista[0]`, `lista[-1]`) |
| **02** | **Inverter Texto** | Fatiamento inverso de strings (`string[::-1]`) |
| **03** | **Análise e Tratamento de Frase** | Métodos de string (`.strip()`, `.upper()`), manipulação de Dicionários e contagem |
| **04** | **Substituir Palavras** | Método de substituição imutável (`.replace()`) |
| **05** | **Recortar Lista por Intervalo** | *Slicing* parametrizado (`lista[inicio:fim]`) |

---

## Tecnologias e Boas Práticas

* **Linguagem:** Python 3.x
* **Arquitetura:** Separação clara entre Interface (CLI) e Regra de Negócio (Módulo de Funções)
* **Boas Práticas:**
  * **Type Hinting:** Anotação explícita de tipos nos parâmetros e retornos de funções.
  * **Clean Code:** Nomes de variáveis expressivos e funções com responsabilidade única.
  * **Controle de Versão:** Commits semânticos no Git (`feat:`, `refactor:`, `docs:`).

---

## Estrutura da Aplicação

```text
├── programa.py         # Interface principal do menu e captura de inputs (CLI)
├── subalgoritmos.py    # Módulo de funções com a lógica pura dos dados
└── README.md           # Documentação técnica do projeto
