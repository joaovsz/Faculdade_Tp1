import time
import psutil
from collections import deque
import matplotlib.pyplot as plt  

def ler_arquivos(arquivo):
    with open(arquivo, 'r') as f:
        return [linha.strip() for linha in f.readlines()]

def medir_tempo_e_memoria(funcao, *args):
    inicio_tempo = time.time()
    inicio_memoria = psutil.Process().memory_info().rss
    resultado = funcao(*args)
    fim_tempo = time.time()
    fim_memoria = psutil.Process().memory_info().rss
    tempo_execucao = fim_tempo - inicio_tempo
    memoria_usada = (fim_memoria - inicio_memoria) / 1024 
    return resultado, tempo_execucao, memoria_usada

if __name__ == "__main__":
    arquivo_listagem = './tp1_files/saida.txt'
    lista_arquivos = ler_arquivos(arquivo_listagem)

    _, tempo_hashtable, memoria_hashtable = medir_tempo_e_memoria(lambda x: {i: x[i] for i in range(len(x))}, lista_arquivos)
    pilha, tempo_pilha, memoria_pilha = medir_tempo_e_memoria(lambda x: list(reversed(x)), lista_arquivos)
    fila, tempo_fila, memoria_fila = medir_tempo_e_memoria(lambda x: deque(x), lista_arquivos)

    estruturas = ['Hashtable', 'Pilha', 'Fila']
    tempos = [tempo_hashtable, tempo_pilha, tempo_fila]
    memorias = [memoria_hashtable, memoria_pilha, memoria_fila]

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.bar(estruturas, tempos, color='lightgreen')
    plt.xlabel('Estrutura de Dados')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title('Comparação dos Tempos de Execução')

    plt.subplot(1, 2, 2)
    plt.bar(estruturas, memorias, color='salmon')
    plt.xlabel('Estrutura de Dados')
    plt.ylabel('Memória Usada (KB)')
    plt.title('Comparação da Memória Usada')

    plt.tight_layout()
    plt.savefig('graficos_algoritmos2.png')

