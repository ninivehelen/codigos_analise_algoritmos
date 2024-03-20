from buscas import *

#Nome para salvar os arquivos csv do valor e da resposta de tempo
nome_sequencial ="Busca_Sequencial"
nome_sequencial_otimizada ="Busca_Sequencial_Otimizada"
nome_busca_binaria = "Busca_Binária"

#cores de cada gráfico
#Valores que n e q podem assumir
valores = [10000,100000,1000000,10000000]

#cores dos gráficos
cor_sequencial = "#044026"
cor_sequencial_otimizada = "#14c478"
cor_busca_binaria = "#4af7ac"

#Para escolher qual função quer rodar para facilitar.
busca_sequencial_linear_compila = True
busca_sequencial_linear_otimizada_compila = True
busca_binaria_compila = True

#Função principal
def main():
     for valor_n in valores:
       #passando os valores para gerar os numeros aletorios
        n = criar_lista_n(valor_n)
        q = criar_lista_q()
        n = n.tolist()
        q = q.tolist()
        tam_q = len(q)
        print(f'Vetor aleatório n gerado para: {valor_n}')
        print(f'Vetor aleatório q gerado para: {tam_q}')
        #Chamando as funções que estão com True para compilar
        if busca_sequencial_linear_compila == True:
             print(len(busca_sequencial_linear(n,q,valor_n,tam_q,nome_sequencial)))
             criar_grafico(nome_sequencial,cor_sequencial)
         
        if busca_sequencial_linear_otimizada_compila == True:
             print(len(busca_sequencial_otimizada(n,q,valor_n, tam_q,nome_sequencial_otimizada)))
             criar_grafico(nome_sequencial_otimizada,cor_sequencial_otimizada)

        if busca_binaria_compila == True:
             print(len(busca_binaria(n,q,valor_n,tam_q,nome_busca_binaria)))
             criar_grafico(nome_busca_binaria ,cor_busca_binaria)

        elif busca_sequencial_linear_compila == False and busca_sequencial_linear_otimizada_compila == False and busca_sequencial_binaria_compila == False:
          print("Nenhuma função escolhida para ser processada")

#função principal que compila o código          
if __name__ == "__main__":
    main()
    