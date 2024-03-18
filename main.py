import numpy as np
from buscas import *

#Nome para salvar os arquivos csv do valor e da resposta de tempo
nome_sequencial ="Busca_Sequencial"
nome_sequencial_otimizada ="Busca_Sequencial_Otimizada"
nome_busca_binaria = "Busca_Binária"

#Valores que n e q podem assumir
valores = [10000,100000,10000000,1000000]

#Para escolher qual função quer rodar para facilitar.
busca_sequencial_linear_compila = False
busca_sequencial_linear_otimizada_compila = True
busca_sequencial_binaria_compila = True

#Função principal
def main():
     for valor in valores:
       #passando os valores para gerar os numeros aletorios
        n = criar_lista_n(valor)
        q = criar_lista_q(valor)
        n = n.tolist()
        q = q.tolist()
        print(f'Vetor aleatório n gerado para números: {valor}')
        print(f'Vetor aleatório q gerado para números: {valor}')
        #Chamando as funções que estão com True para compilar
        if busca_sequencial_linear_compila == True:
             print(len(busca_sequencial_linear(n,q,valor,nome_sequencial)))
             criar_grafico(nome_sequencial)
        if busca_sequencial_linear_otimizada_compila == True:
             print(len(busca_sequencial_otimizada(n,q,valor,nome_sequencial_otimizada)))
             criar_grafico(nome_sequencial_otimizada)
        if busca_sequencial_binaria_compila == True:
             print(len(busca_binaria(n,q,valor,nome_busca_binaria)))
             criar_grafico(nome_busca_binaria)
        elif busca_sequencial_linear_compila == False and busca_sequencial_linear_otimizada_compila == False and busca_sequencial_binaria_compila == False:
          print("Nenhuma função escolhida para ser processada")
          break


if __name__ == "__main__":
    main()
    