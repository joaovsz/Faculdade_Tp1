import time
import matplotlib.pyplot as plt

def ler_arquivos(arquivo):
    with open(arquivo, 'r') as f:
        return [linha.strip() for linha in f.readlines()]

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

def medir_tempo(algoritmo, lista):
    inicio = time.time()
    algoritmo(lista)
    fim = time.time()
    return fim - inicio

if __name__ == "__main__":
    arquivo_listagem = './tp1_files/saida.txt'
    lista_arquivos = ler_arquivos(arquivo_listagem)

    lista_para_bubble = lista_arquivos[:]
    tempo_bubble = medir_tempo(bubble_sort, lista_para_bubble)

    lista_para_selection = lista_arquivos[:]
    tempo_selection = medir_tempo(selection_sort, lista_para_selection)

    lista_para_insertion = lista_arquivos[:]
    tempo_insertion = medir_tempo(insertion_sort, lista_para_insertion)

    algoritmos = ['Bubble Sort', 'Selection Sort', 'Insertion Sort']
    tempos = [tempo_bubble, tempo_selection, tempo_insertion]

    plt.figure(figsize=(10, 6))
    plt.bar(algoritmos, tempos, color='skyblue')
    plt.xlabel('Algoritmo de Ordenação')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title('Comparação dos Tempos de Execução dos Algoritmos de Ordenação')
    plt.savefig('graficos_algoritmos.png')
