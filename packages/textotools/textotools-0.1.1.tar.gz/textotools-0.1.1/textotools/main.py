# Objetivo Geral
# Desenvolver um pacote Python para manipulação eficiente de texto em arquivos.
# Contextualização
# Explorar funcionalidades comuns de manipulação de strings adaptadas para trabalhar diretamente com arquivos de texto.

# Capitalização:
# contar_palavras(nome_arquivo_entrada, nome_arquivo_saida)
# contar_caracteres(nome_arquivo_entrada, nome_arquivo_saida)
# converter_maiusculas(nome_arquivo_entrada, nome_arquivo_saida)
# converter_minusculas(nome_arquivo_entrada, nome_arquivo_saida)
# Descrição: Cada função realiza a operação desejada em todas as palavras ou caracteres de um arquivo de texto, salvando o resultado em um novo arquivo.

# Substituição de Substrings:
# Função: substituir_substring(nome_arquivo_entrada, nome_arquivo_saida, antiga, nova)
# Descrição: Substitui todas as ocorrências de uma substring por outra em um arquivo de texto, salvando o resultado em um novo arquivo.

# Compressão de Texto:
# Função: compress_texto(nome_arquivo_entrada, nome_arquivo_saida)
# Descrição: Comprime o conteúdo de um arquivo de texto usando o algoritmo de compressão.
# Descompressão de Texto:
# Função: decompress_texto(nome_arquivo_entrada, nome_arquivo_saida)
# Descrição: Descomprime o conteúdo do arquivo de texto usando o algoritmo de descompressão.
#lembrando que é pra ser uma biblioteca do PYPI e não um servidor ou cliente
#caso o arquivo de saida não exista, ele deve ser criado
import os
import re
import string
import sys
import zlib

import heapq
from collections import defaultdict, Counter
import pickle

    
def abrir_arquivo(nome_arquivo):
    """
    Abre um arquivo de texto.

    A função abrir_arquivo é responsável por abrir um arquivo de texto.

    Parameters
    ----------
    nome_arquivo : str
        O nome do arquivo de texto.

    Returns
    -------
    bool
        Um objeto de arquivo se o arquivo foi aberto com sucesso, ou False caso contrário.
    """
    try:
        arquivo = open(nome_arquivo, 'r')
        return arquivo
    except:
        arquivo = False 
        return arquivo

def contar_palavras(nome_arquivo_entrada, nome_arquivo_saida=None):
    """
    Conta o número de palavras em um arquivo de texto.

    A função contar_palavras é responsável por contar o número de palavras em um arquivo de texto e retornar o resultado.

    Parameters
    ----------
    nome_arquivo_entrada : str
        O nome do arquivo de texto de entrada.
    nome_arquivo_saida : str, opcional
        O nome do arquivo de texto de saída. Se não for fornecido, nenhum arquivo será criado.

    Returns
    -------
    int or False
        A quantidade de palavras se a operação foi realizada com sucesso, False caso contrário.
    """
    
    arquivo = abrir_arquivo(nome_arquivo_entrada)  
    if arquivo:
        texto = arquivo.read()
        arquivo.close()
        return len(texto.split())
    else:
        return False

    
def contar_caracteres(nome_arquivo_entrada, nome_arquivo_saida=None):
    """
    Conta o número de caracteres em um arquivo de texto.

    A função contar_caracteres é responsável por contar o número de caracteres em um arquivo de texto e retornar o resultado.

    Parameters
    ----------
    nome_arquivo_entrada : str
        O nome do arquivo de texto de entrada.
    nome_arquivo_saida : str, opcional
        O nome do arquivo de texto de saída. Se não for fornecido, nenhum arquivo será criado.

    Returns
    -------
    int or False
        A quantidade de caracteres se a operação foi realizada com sucesso, False caso contrário.
    """
    
    arquivo = abrir_arquivo(nome_arquivo_entrada)
    if arquivo:
        texto = arquivo.read()
        arquivo.close()
        return len(texto)
    else:
        return False

    
def substituir_substring(nome_arquivo_entrada, antiga='', nova='', nome_arquivo_saida=None):
    """
    Substitui todas as ocorrências de uma substring por outra em um arquivo de texto.

    A função substituir_substring é responsável por substituir todas as ocorrências de uma substring por outra em um arquivo de texto.

    Parameters
    ----------
    nome_arquivo_entrada : str
        O nome do arquivo de texto de entrada.
    nome_arquivo_saida : str, opcional
        O nome do arquivo de texto de saída. Se não for fornecido, um arquivo será criado no diretório atual.
    antiga : str, opcional
        A substring a ser substituída.
    nova : str, opcional
        A substring substituta.

    Returns
    -------
    bool
        True se a operação foi realizada com sucesso, False caso contrário.
    """

    arquivo = abrir_arquivo(nome_arquivo_entrada)
    if arquivo:
        texto = arquivo.read()
        arquivo.close()
        texto_modificado = texto.replace(antiga, nova)

        if nome_arquivo_saida is not None:
            # Se nome_arquivo_saida for fornecido, escreve o texto modificado no arquivo
            arquivo_saida = open(nome_arquivo_saida, 'w')
            arquivo_saida.write(texto_modificado)
            arquivo_saida.close()
        else:
            # Se nome_arquivo_saida não for fornecido, cria um arquivo no diretório atual
            nome_arquivo_saida = nome_arquivo_entrada.split('.')[0] + '_substituido.txt'
            arquivo_saida = open(nome_arquivo_saida, 'w')
            arquivo_saida.write(texto_modificado)
            arquivo_saida.close()

        return True
    else:
        return False


    
def compress_texto(nome_arquivo_entrada, nome_arquivo_saida=None):
    """
    Comprime o conteúdo de um arquivo de texto.

    A função compress_texto é responsável por comprimir o conteúdo de um arquivo de texto.

    Parameters
    ----------
    nome_arquivo_entrada : str
        O nome do arquivo de texto de entrada.
    nome_arquivo_saida : str, opcional
        O nome do arquivo de texto de saída. Se não for fornecido, um arquivo será criado no diretório atual.

    Returns
    -------
    bool
        True se a operação foi realizada com sucesso, False caso contrário.
    """

    arquivo = abrir_arquivo(nome_arquivo_entrada)
    if arquivo:
        texto = arquivo.read()
        arquivo.close()
        texto_compress = zlib.compress(texto.encode())

        if nome_arquivo_saida is not None:
            # Se nome_arquivo_saida for fornecido, escreve o texto comprimido no arquivo
            arquivo_saida = open(nome_arquivo_saida, 'wb')
            arquivo_saida.write(texto_compress)
            arquivo_saida.close()
        else:
            # Se nome_arquivo_saida não for fornecido, cria um arquivo no diretório atual
            nome_arquivo_saida = nome_arquivo_entrada.split('.')[0] + '_compress.txt'
            arquivo_saida = open(nome_arquivo_saida, 'wb')
            arquivo_saida.write(texto_compress)
            arquivo_saida.close()

        return True
    else:
        return False



def decompress_texto(nome_arquivo_entrada, nome_arquivo_saida=None):
    """
    Descomprime o conteúdo de um arquivo de texto.

    A função decompress_texto é responsável por descomprimir o conteúdo de um arquivo de texto.

    Parameters
    ----------
    nome_arquivo_entrada : str
        O nome do arquivo de texto de entrada.
    nome_arquivo_saida : str, opcional
        O nome do arquivo de texto de saída. Se não for fornecido, um arquivo será criado no diretório atual.

    Returns
    -------
    bool
        True se a operação foi realizada com sucesso, False caso contrário.
    """

    arquivo = open(nome_arquivo_entrada, 'rb')
    if arquivo:
        texto = arquivo.read()
        arquivo.close()
        texto_decompress = zlib.decompress(texto).decode()

        if nome_arquivo_saida is not None:
            # Se nome_arquivo_saida for fornecido, escreve o texto descomprimido no arquivo
            arquivo_saida = open(nome_arquivo_saida, 'w')
            arquivo_saida.write(texto_decompress)
            arquivo_saida.close()
        else:
            # Se nome_arquivo_saida não for fornecido, cria um arquivo no diretório atual
            nome_arquivo_saida = nome_arquivo_entrada.split('.')[0] + '_decompress.txt'
            arquivo_saida = open(nome_arquivo_saida, 'w')
            arquivo_saida.write(texto_decompress)
            arquivo_saida.close()

        return True
    else:
        return False


def contar_palavras_iguais(nome_arquivo_entrada, palavra):
    """
    Conta o número de vezes que uma palavra aparece em um arquivo de texto.

    A função contar_palavras_iguais é responsável por contar o número de vezes que uma palavra aparece em um arquivo de texto e retornar o resultado.

    Parameters
    ----------
    nome_arquivo_entrada : str
        O nome do arquivo de texto de entrada.
    palavra : str
        A palavra a ser contada.

    Returns
    -------
    int or False
        A quantidade de vezes que a palavra aparece se a operação foi realizada com sucesso, False caso contrário.
    """

    arquivo = abrir_arquivo(nome_arquivo_entrada)
    if arquivo:
        #contar todas as vezes que a palavra aparece
        texto = arquivo.read()
        arquivo.close()
        return len(re.findall(palavra, texto))
    else:
        return False
    
def remover_palavra(palavra, nome_arquivo_entrada, nome_arquivo_saida=None):
    """
    Remove uma palavra de um arquivo de texto.

    A função remover_palavra é responsável por remover uma palavra de um arquivo de texto.

    Parameters
    ----------
    nome_arquivo_entrada : str
        O nome do arquivo de texto de entrada.
    palavra : str
        A palavra a ser removida.
    nome_arquivo_saida : str, opcional
        O nome do arquivo de texto de saída. Se não for fornecido, um arquivo será criado no diretório atual.

    Returns
    -------
    bool
        True se a operação foi realizada com sucesso, False caso contrário.
    """

    arquivo = abrir_arquivo(nome_arquivo_entrada)
    if arquivo:
        # Remove a palavra do arquivo em todos os lugares
        texto = arquivo.read()
        arquivo.close()
        texto_modificado = texto.replace(palavra, '')

        if nome_arquivo_saida is not None:
            # Se nome_arquivo_saida for fornecido, escreve o texto modificado no arquivo
            arquivo_saida = open(nome_arquivo_saida, 'w')
            arquivo_saida.write(texto_modificado)
            arquivo_saida.close()
        else:
            # Se nome_arquivo_saida não for fornecido, cria um arquivo no diretório atual
            nome_arquivo_saida = nome_arquivo_entrada.split('.')[0] + '_removido.txt'
            arquivo_saida = open(nome_arquivo_saida, 'w')
            arquivo_saida.write(texto_modificado)
            arquivo_saida.close()

        return True
    else:
        return False

        
    


