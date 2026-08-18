
def obter_extremos(lista: list) -> list:
    return [lista[0], lista[-1]]

def inverter_texto(texto:str) -> str:
    return texto[::-1]

def analisar_frase(frase: str) -> dict:
    frase_tratada = frase.strip()
    qtd_palavras = len(frase.strip().split())
    qnt_caracteres = len(frase)
    return {
        "sem_espaços": frase_tratada,
        "quantidade_palavras": qtd_palavras,
        "quantidade_caracteres": qnt_caracteres
    }