import time
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

#Função para gerar os valores aletorios de n 
def criar_lista_n(valor):
    valor_tam = list(str(valor))
    tam = len(valor_tam)
    valor_tam = tam - 1
    tam = 10**valor_tam
    n = np.random.randint(0,tam,tam)
    return n
#Função para gerar os valores aletorios de q
def criar_lista_q(valor):
    valor_tam = list(str(valor))
    tam = len(valor_tam)
    valor_tam = tam - 1
    tam = 10**valor_tam
    q = np.random.randint(0,tam,tam)
    return q

#Função busca sequencial 
def busca_sequencial_linear(n,q,valor, nome):
     print(f'Processando a função busca sequencial. Quantidade de números buscados: {valor}')
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
     salvar_dados(valor,tempo_total, nome)
     return ocorrencia_na_lista

#Função busca sequencia otimizada  
def busca_sequencial_otimizada(n,q,valor, nome):
    print(f'Processando a função busca sequencial otimizada. Quantidade de números buscados: {valor}')
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
    salvar_dados(valor,tempo_total,nome)
    return  ocorrencia_na_lista_automatizada

#Função busca binária
def busca_binaria(n,q,valor, nome, inicio_lista=0, fim_lista=None):
    print(f'Processando a função busca binária. Quantidade de números buscados: {valor}')
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
    salvar_dados(valor,tempo_total,nome)
    return encontrados
    
def salvar_dados(valor,tempo,nome):
  try:
    df = pd.read_csv(f'{nome}.csv')
  except FileNotFoundError:
    df = pd.DataFrame(columns=['Valor', 'Tempo'])
  
  df_novo = pd.DataFrame({'Valor': [valor], 'Tempo': [tempo], 'Função': [nome]})
  df = pd.concat([df, df_novo], ignore_index=True)
  df.to_csv(f'{nome}.csv', index=False)
  print(f'arquivo salvo {nome}')

#Função de criar o gráfico
def criar_grafico(nome):
    df = pd.read_csv(f'{nome}.csv')
    troca_valores = {10000: '10^4', 100000: '10^5', 1000000: '10^6', 10000000: '10^7'}
    df['Valor'] = df['Valor'].map(troca_valores)
    
    #palette=['magenta', 'deepskyblue', 'yellowgreen']
    sns.set_style("whitegrid")
    sns.lineplot(data=df, x='Valor', y='Tempo', hue='Função',palette=['deepskyblue', 'yellowgreen','Margenta'])

    plt.xlabel('Quantidade de números buscado',fontsize=10, fontweight='bold')
    plt.ylabel('Tempo em segundos',fontsize=10, fontweight='bold')

    x = df['Valor']
    y = df['Tempo']
    
    plt.yticks(y)
    plt.scatter(x, y, marker="*", color='red')
    

    plt.xlabel('Quantidade de Números Buscado')
    plt.ylabel('Tempo em Segundos')

    num_ticks = 13 
    y_min = df['Tempo'].min()
    y_max = df['Tempo'].max()
    y_ticks = np.linspace(y_min, y_max, num_ticks)

    plt.yticks(y_ticks)
    plt.savefig(f'{nome}.png', format='png')
    print("gráfico criado")