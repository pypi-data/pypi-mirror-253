import os
import shutil
from fpdf import FPDF
import PyPDF2
from collections import Counter
import re
import pickle


def criar_arquivo_txt(nome):
    """Função responsável por criar arquivos .txt se eles não existirem, caso contrário, ela apenas lê e exibe o arquivo .txt

    Parameters
    ----------
    nome : str
        Nome que será atribuido para o arquivo .txt se ele não existir

    Returns
    -------
    bool
        True se o arquivo .txt já existe (lê e exibe o arquivo), False se o arquivo .txt não existe (escreve em um arquivo .txt)
    """
    if os.path.exists(nome + '.txt'):
        with open(nome + '.txt', "r", encoding="utf-8") as arq:
            arquivo = arq.read()
            print(arquivo)
        return True
    else:
        with open(nome + '.txt', "w", encoding="utf-8") as arq:
            conteudo = input('-> ')
            arq.write(conteudo + " ")
        return False


def abrir_arquivo_txt(nome):
    """Função responsável por abrir um arquivo .txt, se ele existir

    Parameters
    ----------
    nome : str
        Nome do arquivo .txt que será aberto, se ele existir

    Returns
    -------
    bool
        True se o arquivo .txt já existe (lê e exibe o arquivo .txt), False se o arquivo .txt não existe
    """
    if os.path.exists(nome + '.txt'):
        with open(nome + '.txt', "r", encoding="utf-8") as arq:
            arquivo = arq.read()
            print(arquivo)
        return True
    else:
        return False   


def escrever_arquivo_txt(nome):
    """Função responsável por escrever em um arquivo .txt, se ele existir.

    Parameters
    ----------
    nome : str
        Nome do arquivo .txt que será escrito, se ele existir

    Returns
    -------
    bool
        True se o arquivo .txt já existe (escreve no arquivo .txt), False se o arquivo .txt não existe
    """
    if os.path.exists(nome + '.txt'):
        with open(nome + '.txt', "a", encoding="utf-8") as arq:
            conteudo = input('-> ')
            arq.write(conteudo + " ")
        return True
    else:
        return False


def criar_arquivo_bin(nome):
    """Função responsável por criar arquivos .bin se eles não existirem, caso contrário, ela apenas lê e exibe o arquivo .bin

    Parameters
    ----------
    nome : str
        Nome que será atribuido para o arquivo .bin se ele não existir

    Returns
    -------
    bool
        True se o arquivo .bin já existe (lê e exibe o arquivo), False se o arquivo .bin não existe (escreve em um arquivo .bin)
    """
    if os.path.exists(nome + '.bin'):
        with open(nome + '.bin', 'rb') as arq:
            arquivo = arq.read()
            print(arquivo)
        return True
    else:
        with open(nome + '.bin', 'wb') as arq:
            conteudo = input('-> ')
            arq.write(pickle.dumps(conteudo))
        return False


def abrir_arquivo_bin(nome):
    """Função responsável por abrir um arquivo .bin, se ele existir

    Parameters
    ----------
    nome : str
        Nome do arquivo .bin que será aberto, se ele existir

    Returns
    -------
    bool
        True se o arquivo .bin já existe (lê e exibe o arquivo .bin), False se o arquivo .bin não existe
    """
    if os.path.exists(nome + '.bin'):    
        with open(nome + '.bin', "rb") as arq:
            arquivo = arq.read()
            print(pickle.loads(arquivo))
        return True
    else:
        return False


def escrever_arquivo_bin(nome):
    """Função responsável por escrever em um arquivo .bin, se ele existir.

    Parameters
    ----------
    nome : str
        Nome do arquivo .bin que será escrito, se ele existir

    Returns
    -------
    bool
        True se o arquivo .bin já existe (escreve no arquivo .bin), False se o arquivo .bin não existe
    """
    if os.path.exists(nome + '.bin'):
        with open(nome + '.bin', "ab") as arq:
            conteudo = input('-> ')
            arq.write(pickle.dumps(conteudo))
        return True
    else:
        return False


def listar_diretorio(diretorio, extensao):
    """
    Função responsável por listas tudo que esta dentro do diretorio, dependendo da extensão

    Parameters
    ----------
    diretorio : str
        Caminho do diretorio a qual deseja-se fazer a listagem
    extensao : str
        Extensão dos arquivos a qual deseja-se fazer a listagem
    """
    for raiz, dirs, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if arquivo.endswith(extensao):
                for dir in dirs:
                    caminho_completo = os.path.join(raiz, dir, arquivo)
                    print(caminho_completo)


def diretorio_atual():
    """
    Função responsável por listas o diretorio atual
    Returns
    -------
    str
        retorna o diretório de trabalho atual do programa em execução
    """
    return os.getcwd()


def criar_diretorio(nome_dir):
    """Função responsável por criar um novo diretório.

    Parameters
    ----------
    nome_dir : str
        O nome do novo diretório a ser criado.

    Returns
    -------
    None
        A função não retorna um valor específico, mas cria um novo diretório no diretório atual.
    """
    os.mkdir(diretorio_atual()+'./'+nome_dir)


def copiar_diretorio_completo(src, dst):
    """Função responsável por copiar todo o conteúdo (arquivos) de um diretório de origem para um diretório de destino.

    Parameters
    ----------
    src : str
        Caminho do diretório de origem que será copiado.
    dst : str
        Caminho do diretório de destino onde os arquivos serão copiados.

    Returns
    -------
    bool
        True se a operação for bem-sucedida, False se ocorrer algum erro durante a cópia.
    """
    try:
        for raiz, _, arquivos in os.walk(src):
            for arquivo in arquivos:
                src_arquivo = os.path.join(raiz, arquivo)
                dst_arquivo = os.path.join(dst, arquivo)
                shutil.copy2(src_arquivo, dst_arquivo)
        return True
    except Exception as e:
        print(f"Error during file copy: {e}")
        return False


def mover_diretorio_completo(src, dst):
    """Função responsável por mover todo o conteúdo (arquivos) de um diretório de origem para um diretório de destino.

    Parameters
    ----------
    src : str
        Caminho do diretório de origem que será movido.
    dst : str
        Caminho do diretório de destino para onde os arquivos serão movidos.

    Returns
    -------
    bool
        True se a operação for bem-sucedida, False se ocorrer algum erro durante o movimento.
    """
    lista = os.listdir(src)
    qtnd_arq = len(lista)
    aux = 0
    try:
        if os.path.isdir(dst):
            while aux < qtnd_arq:
                antigo = os.path.join(src, lista[aux])
                novo = os.path.join(dst, lista[aux])
                if os.path.exists(antigo):  
                    shutil.move(antigo, novo)
                else:
                    print(f"Arquivo nao existe: {antigo}")
                aux += 1
            return True
        else:
            return False
    except Exception as e:
        print(f"Erro ao mover arquivo: {e}")
        return False


def deletar_arquivo(nome_arquivo):
    """Função responsável por deletar um arquivo especificado.

    Parameters
    ----------
    nome_arquivo : str
        O nome do arquivo a ser removido.

    Returns
    -------
    bool
        True se o arquivo for removido com sucesso, False se o arquivo não for encontrado ou ocorrer um erro durante a remoção.
    """
    try:
        os.remove(nome_arquivo)
        print(f"O arquivo '{nome_arquivo}' foi removido com sucesso.")
        return True
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return False
    except Exception as e:
        print(f"Erro ao tentar remover o arquivo '{nome_arquivo}': {e}")
        return False


def deletar_diretorio(nome_diretorio):
    """Função responsável por deletar um diretório especificado, incluindo todos os seus arquivos e subdiretórios.

    Parameters
    ----------
    nome_diretorio : str
        O nome do diretório a ser removido.

    Returns
    -------
    bool
        True se o diretório for removido com sucesso, False se o diretório não for encontrado ou ocorrer um erro durante a remoção.
    """
    try:
        shutil.rmtree(nome_diretorio)
        print(f"O diretório '{nome_diretorio}' foi removido com sucesso.")
        return True
    except FileNotFoundError:
        print(f"O diretório '{nome_diretorio}' não foi encontrado.")
        return False
    except Exception as e:
        print(f"Erro ao tentar remover o diretório '{nome_diretorio}': {e}")
        return False


def tamanho_diretorio_kb(caminho):
    """Função responsável por calcular o tamanho total (em kilobytes) de um diretório, incluindo todos os seus arquivos e subdiretórios.

    Parameters
    ----------
    caminho : str
        O caminho do diretório a ser analisado.

    Returns
    -------
    tuple
        Uma tupla contendo três valores:
        - O tamanho total do diretório em kilobytes.
        - O número total de arquivos no diretório.
        - O número total de subdiretórios no diretório.
    """
    total = 0
    total_arq = 0
    total_dir = 0
    for caminho_atual, sub_dir, arquivos in os.walk(caminho):
        for a in arquivos:
            aux = os.path.join(caminho_atual, a)
            total += os.path.getsize(aux)
            total_arq += 1

        for sub in sub_dir:
            aux_2 = os.path.join(caminho_atual, sub)
            subdir_size, subdir_arq, subdir_dir = tamanho_diretorio_kb(aux_2)
            total_dir += 1 + subdir_dir
            total_arq += subdir_arq
            total += subdir_size
    return total/1024, total_arq, total_dir



def tamanho_arquivo_kb(caminho, nome_arq):
    """Função responsável por obter o tamanho de um arquivo em kilobytes.

    Parameters
    ----------
    caminho : str
        O caminho do diretório que contém o arquivo.
    nome_arq : str
        O nome do arquivo para o qual o tamanho será obtido.

    Returns
    -------
    float
        O tamanho do arquivo em kilobytes.
    """
    return os.path.getsize(caminho + '\\' + nome_arq)/1024


def palavra_chave(arquivo, palavra):
    """Função responsável por buscar a ocorrência de uma palavra-chave em um arquivo de texto.

    Parameters
    ----------
    arquivo : str
        O caminho do arquivo de texto a ser analisado.
    palavra : str
        A palavra-chave a ser procurada no arquivo.

    Returns
    -------
    tuple
        Uma tupla contendo duas informações:
        - Uma lista de tuplas, onde cada tupla contém o número da linha e o conteúdo da linha onde a palavra-chave foi encontrada.
        - O número total de ocorrências da palavra-chave no arquivo.
    """
    ocorrencias = []
    count = 0

    with open(arquivo, 'r', encoding='utf-8') as file:
        for numero_linha, linha in enumerate(file, 1):
            if palavra in linha:
                count += 1
                ocorrencias.append((numero_linha, linha.strip()))

    return ocorrencias, count


def contar_palavras_mais_frequentes(nome_arquivo):
    """Função responsável por contar as 10 palavras mais frequentes em um arquivo de texto, excluindo stopwords comuns.

    Parameters
    ----------
    nome_arquivo : str
        O caminho do arquivo de texto a ser analisado.

    Returns
    -------
    list
        Uma lista contendo tuplas representando as 10 palavras mais frequentes no arquivo, juntamente com suas contagens.
    """
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()

    palavras = re.findall(r'\b\w+\b', conteudo.lower())

    stopwords = ["a", "e", "em", "este", "estes", "esta", "estas", "é", "no", "na", "tem", "as", "o", "os", "um", "uns", "uma", "umas", "para", "de", "da", "do", "das", "dos", "se", "então", "ele", "ela", "eles", "elas", "à", "ou", "por", "que", "com", "também", "the", "a", "an", "at", "by", "from", "how", "of", "on", "that", "to", "for", "in", "out", "I", "he", "she", "it", "they", "our", "them", "him", "her", "do", "will", "or", "with", "also", "and", "is", "are", "this", "can", "we", "ao", "são", "pelo", "seus","seu", "lhe"]
    palavras_filtradas = [palavra for palavra in palavras if palavra not in stopwords]

    contagem_palavras = Counter(palavras_filtradas)

    palavras_mais_frequentes = contagem_palavras.most_common(10)

    return palavras_mais_frequentes


def contar_caracteres(arquivo):
    """Função responsável por contar o número total de caracteres em um arquivo de texto.

    Parameters
    ----------
    arquivo : str
        O caminho do arquivo de texto a ser analisado.

    Returns
    -------
    int
        O número total de caracteres no arquivo.
    """
    with open(arquivo, 'r', encoding='utf-8') as file:
        conteudo = file.read()
        quantidade_caracteres = len(conteudo)

    return quantidade_caracteres


def txt_pdf(arquivo, nome_arquivo):
    """Função responsável por converter um arquivo de texto para um arquivo PDF.

    Parameters
    ----------
    arquivo : str
        O caminho do arquivo de texto a ser convertido.
    nome_arquivo : str
        O nome que será atribuído ao arquivo PDF resultante.

    Returns
    -------
    None
        A função não retorna um valor específico, mas cria um arquivo PDF a partir do arquivo de texto fornecido.
    """
    pdf = FPDF()
    pdf.add_page()
    file = open(arquivo, 'r')
    for texto in file:
        if len(texto) <= 20:
            pdf.set_font("Arial", "B", size=18)
            pdf.cell(w=200,h=10,txt=texto,ln=1,align='C')
        else:
            pdf.set_font("Arial", size=15)
            pdf.cell(w=0,h=10,txt=texto,align='L')
    pdf.output(nome_arquivo + '.pdf')


def pdf_to_txt(arquivo, arquivo_txt):
    """Função responsável por converter um arquivo PDF para um arquivo de texto.

    Parameters
    ----------
    arquivo : str
        O caminho do arquivo PDF a ser convertido.
    arquivo_txt : str
        O nome que será atribuído ao arquivo de texto resultante.

    Returns
    -------
    None
        A função não retorna um valor específico, mas cria um arquivo de texto contendo o texto extraído do arquivo PDF.
    """
    with open(arquivo, 'rb') as pdf:
        aux = PyPDF2.PdfReader(pdf)

        text = ""
        for page in aux.pages:
            text += page.extract_text()
    with open(arquivo_txt + '.txt', 'w', encoding='utf-8') as txt:
        txt.write(text)


def txt_bin(arquivo, nome_arquivo_bin):
    """Função responsável por converter um arquivo de texto para um arquivo binário (.bin).

    Parameters
    ----------
    arquivo : str
        O caminho do arquivo de texto a ser convertido.
    nome_arquivo_bin : str
        O nome que será atribuído ao arquivo binário resultante.

    Returns
    -------
    bool
        True se o arquivo de texto existe e a conversão foi bem-sucedida, False caso contrário.
    """
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as arq:
            conteudo_texto = arq.read()
        with open(nome_arquivo_bin + '.bin', 'wb') as arq_bin:
            arq_bin.write(pickle.dumps(conteudo_texto))
        return True
    else:
        return False


def bin_to_txt(nome_arquivo_bin, nome_arquivo_txt):
    """Função responsável por converter um arquivo binário (.bin) para um arquivo de texto.

    Parameters
    ----------
    nome_arquivo_bin : str
        O caminho do arquivo binário a ser convertido.
    nome_arquivo_txt : str
        O nome que será atribuído ao arquivo de texto resultante.

    Returns
    -------
    bool
        True se o arquivo binário existe e a conversão foi bem-sucedida, False caso contrário.
    """
    if os.path.exists(nome_arquivo_bin):
        with open(nome_arquivo_bin, 'rb') as arq_bin:
            conteudo_bin = pickle.load(arq_bin)
        with open(nome_arquivo_txt + '.txt', 'w', encoding='utf-8') as arq_txt:
            arq_txt.write(conteudo_bin)
        return True
    else:
        return False

