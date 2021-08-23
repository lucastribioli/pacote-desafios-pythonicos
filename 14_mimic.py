"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""

import random
import sys


def get_dict(filename):
    arquivo = open(filename, "r")
    listona = []
    dicionario = dict()

    for linha in arquivo:
        for word in linha.lower().replace("\n", " ").split(" "):
                listona.append(word)

    for i in range(len(listona)):
        if i < len(listona) - 1:
            if listona[i] in dicionario:
                dicionario[listona[i]].append(listona[i + 1])
            else:
                dicionario[listona[i]] = [listona[i + 1]]
    arquivo.close()

    return dicionario


def mimic_dict(filename):
    return get_dict(filename)


def print_mimic(mimic_dict, word):
    letter = word
    count = 0
    stringona = ""
    while True:
        if letter is not "":
            stringona += f" {letter}"
            count += 1
        letter = random.choice(mimic_dict[letter])
        if count == 200:
            break
    print(f" {stringona}. ")


# Chama mimic_dict() e print_mimic()
def main():
    if len(sys.argv) != 2:
        print('Utilização: ./14_mimic.py file-to-read')
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])
    print_mimic(dict, '')


if __name__ == '__main__':
    main()
