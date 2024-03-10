import time
import numpy as np
import pandas as pd 
import seaborn as sns
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt 


def criar_lista_n(valor):
    valor_tam = list(str(valor))
    valor_tam = len(valor_tam )
    valor_tam = valor_tam - 1
    n = np.random.randint(0,valor,10**valor_tam)
    return n

def criar_lista_q(valor):
    valor_tam = list(str(valor))
    valor_tam = len(valor_tam )
    valor_tam = valor_tam - 1
    q = np.random.randint(0,valor,10**valor_tam)
    return q

def busca_sequencial_linear(n,q,valor, nome):
     inicio = time.time()
     ocorrencia_na_lista = [i for i in q if i in n]
     fim = time.time()
     tempo_total = (round(float(fim - inicio), 3))
     return ocorrencia_na_lista
     salvar_dados(valor,tempo_total, nome)

def busca_sequencial_otimizada(n,q,valor, nome):
    ocorrencia_na_lista_automatizada = []
    inicio = time.time()
    n.sort()
    for i in q:
        if isinstance(n, list):
           for n_item in n:
             if i < n_item:
                 break
             elif i == n_item: 
                 ocorrencia_na_lista_automatizada.append(i)
    fim = time.time()
    tempo_total = fim - inicio
    tempo_total = (round(float(fim - inicio), 3))
    return ocorrencia_na_lista_automatizada
    salvar_dados(valor,tempo_total,nome)
   
def salvar_dados(valor,tempo,nome):
  try:
    df = pd.read_csv("dados.csv")
  except FileNotFoundError:
    df = pd.DataFrame(columns=['Valor', 'Tempo'])

  df_novo = pd.DataFrame({'Valor': [valor], 'Tempo': [tempo], 'Função': [nome]})
  df = pd.concat([df, df_novo], ignore_index=True)
  df.to_csv("dados.csv", index=False)
  print("arquivo salvo")

if __name__ == '__main__':
     nome_sequencial ="busca_seq"
     nome_sequencial_automatizada ="busca_seq_automatizada"
     nome_busca_binaria = "busca binaria"
     valores = [10000]
     for valor in valores:
        n = criar_lista_n(valor)
        q = criar_lista_q(valor)
        n = n.tolist()
        q = q.tolist()
        # print(f'Vetor aleatório lista: {n} gerado')
        # print(f'Vetor aleatório chave: {q} gerado')
        # print(busca_sequencial_linear(n,q,valor,nome_sequencial))
        # print(busca_sequencial_otimizada(n,q,valor,nome_sequencial_automatizada))
        print(busca_binaria(n,q,valor,nome_busca_binaria))
        
    #  criar_grafico()
        
    