import time
import numpy as np
import pandas as pd 
import seaborn as sns
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt 

def criar_lista_n(valor):
    valor_tam = list(str(valor))
    tam = len(valor_tam)
    valor_tam = tam - 1
    tam = 10**valor_tam
    n = np.random.randint(0,tam,tam)
    return n

def criar_lista_q(valor):
    valor_tam = list(str(valor))
    tam = len(valor_tam)
    valor_tam = tam - 1
    tam = 10**valor_tam
    q = np.random.randint(0,tam,tam)
    return q

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
    df = pd.read_csv("dados.csv")
  except FileNotFoundError:
    df = pd.DataFrame(columns=['Valor', 'Tempo'])

  df_novo = pd.DataFrame({'Valor': [valor], 'Tempo': [tempo], 'Função': [nome]})
  df = pd.concat([df, df_novo], ignore_index=True)
  df.to_csv("dados.csv", index=False)
  print("arquivo salvo")

def criar_grafico():
    df = pd.read_csv("dados_10^4.csv")
  
    sns.lineplot(data=df, x='Valor', y='Tempo', hue='Função',palette=['magenta', 'deepskyblue', 'yellowgreen'])

    plt.xlabel('Quantidade de números buscado')
    plt.ylabel('Tempo em segundos')
   
    x = df['Valor']
    y = df['Tempo']
    plt.yticks(y)
    plt.scatter(x, y, marker="*", color='red')

    plt.xlabel('Quantidade de Números Buscado')
    plt.ylabel('Tempo em Segundos')

    plt.savefig("dados_linha.png", format='png')
    print("gráfico criado")

if __name__ == '__main__':
     nome_sequencial ="Busca Sequencial"
     nome_sequencial_automatizada ="Busca Sequencial Otimizada"
     nome_busca_binaria = "Busca Binária"
     valores = [10000000]
     for valor in valores:
        n = criar_lista_n(valor)
        q = criar_lista_q(valor)
        n = n.tolist()
        q = q.tolist()
        print(f'Vetor aleatório lista gerado')
        print(f'Vetor aleatório chave gerado')
        print(len(busca_binaria(n,q,valor,nome_busca_binaria)))
        print(len(busca_sequencial_otimizada(n,q,valor,nome_sequencial_automatizada)))
        print(len(busca_sequencial_linear(n,q,valor,nome_sequencial)))
        
     criar_grafico()
        
    