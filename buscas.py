import time
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

#Função para gerar os valores aletorios de n 
def criar_lista_n(valor_n):
    #capturando o valor e trasformando em lista
    valor_tam_n = list(str(valor_n))
    #Quantidade do tamanho de valor
    tam_n = len(valor_tam_n)
    #diminuido um valor para ficar a quantidade correta, pois o numero 1 não entra na contagem do valor 1000, 10000 etc..
    valor_tam_n = tam_n - 1
    tam_n = 10**valor_tam_n
    #gerando o vetor de numeros aleatorios
    n = np.random.randint(0,tam_n,tam_n)
    return n
#Função para gerar os valores aletorios de q
def criar_lista_q(valor_q):
    #capturando o valor e trasformando em lista
    valor_tam_q = list(str(valor_q))
    #Quantidade do tamanho de valor
    tam_q = len(valor_tam_q)
    #diminuido um valor para ficar a quantidade correta, pois o numero 1 não entra na contagem do valor 1000, 10000 etc..
    valor_tam_q = tam_q - 1
    tam_q = 10**valor_tam_q
    #gerando o vetor de numeros aleatorios
    q = np.random.randint(0,tam_q,tam_q)
    return q

#Função busca sequencial 
def busca_sequencial_linear(n,q,valor_n,tam_q, nome):
    #está função pecorre  n e verificando se o q estã contido em n
     print(f'Processando a função busca sequencial. Quantidade de números em n: {valor_n}')
     ocorrencia_na_lista = []
     inicio = time.time()
     for i in q:
           for n_item in n:
             if i == n_item: 
                ocorrencia_na_lista.append(i)
                break
     fim = time.time()
     tempo_total = (round(float(fim - inicio), 3))
     print("Função busca sequencial finalizada")
     salvar_dados(valor_n,tam_q,tempo_total,nome)
     return ocorrencia_na_lista

#Função busca sequencial otimizada  
def busca_sequencial_otimizada(n,q,valor_n,tam_q, nome):
    #está função ordena n de forma crescente e veririca se n for maior que q para volta pro inicio da lista e verifica o proximo q
    #está função pecorre  n e verificando se o q estã contido em n
    print(f'Processando a função busca sequencial otimizada. Quantidade de números em n: {valor_n}')
    ocorrencia_na_lista_automatizada = []
    inicio = time.time()
    n.sort()
    for i in q:
           for n_item in n:
             if i == n_item: 
                 ocorrencia_na_lista_automatizada.append(i)
                 break
             elif n_item > i:
                 break
    fim = time.time()
    tempo_total = fim - inicio
    tempo_total = (round(float(fim - inicio), 3))
    print("Função busca sequencial otimizada finalizada")
    salvar_dados(valor_n,tam_q,tempo_total,nome)
    return  ocorrencia_na_lista_automatizada

#Função busca binária
def busca_binaria(n,q,valor_n, tam_q, nome, inicio_lista=0, fim_lista=None):
     #essa  comparar q o primeiro elemento o elemento buscado com o n central
     #forma que uma das metades possa ser desprezada.
    print(f'Processando a função busca binária. Quantidade de números em n: {valor_n}')
    encontrados = []
    if fim_lista is None:
       fim_lista = len(n) - 1
    inicio = time.time()
    n.sort()
    for i in q:
        inicio_lista = 0
        fim_lista = len(n) - 1
        while inicio_lista <= fim_lista:
            meio = (inicio_lista + fim_lista) // 2
            if n[meio] == i:
                encontrados.append(i)
                break
            elif i < n[meio]:
                fim_lista = meio - 1
            else:
                inicio_lista = meio + 1
    fim = time.time()
    tempo_total = fim - inicio
    tempo_total = (round(float(fim - inicio), 3))
    print("Função busca binária finalizada")
    salvar_dados(valor_n,tam_q,tempo_total,nome)
    return encontrados
    
def salvar_dados(valor_n,tam_q, tempo,nome):
  #verificando se o arquivo já existe e se não criando o data frame para salvar os dados de valor n e tempo da função
  try:
    df = pd.read_csv(f'{nome}.csv')
  except FileNotFoundError:
    df = pd.DataFrame(columns=['Valor_n','Valor_q','Tempo'])

  #salvando os arquivos de cada valor e tempo de função processada
  df_novo = pd.DataFrame({'Valor_n': [valor_n], 'Valor_q':[tam_q],'Tempo': [tempo], 'Função': [nome]})
  df = pd.concat([df, df_novo], ignore_index=True)
  df.to_csv(f'{nome}.csv', index=False)
  print(f'arquivo salvo {nome}')

#Função de criar o gráfico
def criar_grafico(nome, cor):
    df = pd.read_csv(f'{nome}.csv')
    #convertendo os valores 100000 etc para 10^ para ajustar no gráfico
    troca_valores_n = {10000: '10^4', 100000: '10^5', 1000000: '10^6', 10000000: '10^7'}
    troca_valores_q = {100: '10^2', 1000: '10^3', 10000: '10^4', 100000: '10^5'}
    df['Valor_n'] = df['Valor_n'].map(troca_valores_n)
    df['Valor_q'] = df['Valor_q'].map(troca_valores_q)

    #criando o gráfico de linha
    sns.set()
    plt.figure()
    df = df.sort_values(by='Valor_n')
    df = df.rename(columns={'Valor_q': 'Quantidade de Números q'})
    sns.lineplot(data=df, x='Valor_n', y='Tempo', hue='Quantidade de Números q',palette=[cor], style='Quantidade de Números q',markers=True,lw=0,markeredgewidth=1.25,markeredgecolor='black',markersize=7,errorbar=None,markerfacecolor='white',dashes=False)
    plt.plot(df['Valor_n'], df['Tempo'], marker='', color=cor, linewidth=2, linestyle='None')
    
    # Ajustando a legenda
    plt.legend(title='Quantidade de Números q', loc='best')
    
    #colocando titulo e x e y
    plt.xlabel('Quantidade de Números n')
    plt.ylabel('Tempo em Segundos')
    #titulo do gráfico
    plt.title(f'Gráfico de Linha de Tempo para {nome}')
    #Salvndo
    plt.savefig(f'{nome}.png', format='png')
    plt.close() 
    print("gráfico criado")