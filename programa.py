import os 
os.system("cls")

opcao = " "

while opcao != "0" :
    print ("""
        === Central de Análise de Texto e Listas ===
        1 - Exibir o primeiro itens de uma lista 
        2 - Inverter um texto
        3 - Analisar e tratar uma frase 
        4 - Substituir palavra em uma frase 
        5 - Recortar uma lista por intervalos 
        0 - Sair 
    """)
    opcao = (input("Escolha uma opção para dar continuidade: " )) 