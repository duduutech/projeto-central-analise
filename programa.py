import os 
os.system("cls")
import subalgoritmos


opcao = " "

while opcao != "0" :
    print ("""
        === Central de Análise de Texto e Listas ===
        1 - Exibir o primeiro e itens de uma lista 
        2 - Inverter um texto
        3 - Analisar e tratar uma frase 
        4 - Substituir palavra em uma frase 
        5 - Recortar uma lista por intervalos 
        0 - Sair 
    """)
    opcao = (input("Escolha uma opção para dar continuidade: " )) 
    if opcao == "1" :
        entrada = input("Digite os itens separados por virgulas: ")
        lista_itens = [item.strip() for item in entrada.split(",")]
        extremos = subalgoritmos.obter_extremos(lista_itens)
        print(f"""
        Primeiro item: {extremos[0]}
        Segundo item: {extremos[1]}
       """ )
        input("\n Presione Enter para voltar ao menu ")

    elif opcao == "2":
        entrada_text = input("Digite um texto: ")
        text_invert = subalgoritmos.inverter_texto(entrada_text)
        print(f"\nTexto Invertido: {text_invert}")
        input("\nPrecione enter para voltar ao menu")

