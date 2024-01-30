#libpyles
========================================================

###Atraves desse pacote, o usuário poderá fazer a manipulação de arquivos de maneira mais simples e otimizada, além de poder criar, mover, excluir e copiar diretórios. E mais algumas funções extras de conversão de arquivos de texto.

##Instalação
Para instalar o pacote, basta executar o comando abaixo:
<pre><code>pip install libpyles</code></pre>

##Funções da biblioteca

=======================================================

def criar_arquivo_txt(nome)
def abrir_arquivo_txt(nome)
def escrever_arquivo_txt(nome)
def criar_arquivo_bin(nome)
def abrir_arquivo_bin(nome)
def escrever_arquivo_bin(nome)
def listar_diretorio(diretorio, extensao)
def diretorio_atual()
def criar_diretorio(nome_dir)
def copiar_diretorio_completo(src, dst)
def mover_diretorio_completo(src, dst)
def deletar_arquivo(nome_arquivo)
def deletar_diretorio(nome_diretorio):
def tamanho_diretorio_kb(caminho)
def tamanho_arquivo_kb(caminho, nome_arq)
def palavra_chave(arquivo, palavra)
def contar_palavras_mais_frequentes(nome_arquivo)
def contar_caracteres(arquivo)
def txt_pdf(arquivo, nome_arquivo)
def pdf_to_txt(arquivo, arquivo_txt)
def txt_bin(arquivo, nome_arquivo_bin)
def bin_to_txt(nome_arquivo_bin, nome_arquivo_txt)

=======================================================

##Importação

<pre><code>import libpyles</code></pre>

=======================================================

##Uso de cada função

=======================================================

>Será utilizado uma abreviação para fácil entendimento. Nesse sentido, será utilizado o __lp__ (import libpyles as lp).

<pre><code>

lp.criar_arquivo_txt(nome) 

""" 
    A variável 'nome' é apenas o nome do arquivo sem a extensão(.txt) e entre aspas simples, por exemplo 'teste'. 
    Saída: É criado um arquivo .txt se ele não existir no diretório atual, caso contrário, ela apenas lê e exibe o arquivo .txt. Além disso é retornado True ou False para ser utilizado dependendo da ocasião do uso. 
    Exemplo:
        if lp.criar_arquivo_txt(nome) is True:
            print('Arquivo criado!!')
        else:
            print('Arquivo já existente!!')
"""

lp.abrir_arquivo_txt(nome)

"""
    A variável 'nome' é apenas o nome do arquivo sem a extensão(.txt) e entre aspas simples, por exemplo 'teste'.
    Saída: Abrir um arquivo .txt, se ele existir no diretório. Além disso é retornado True ou False para ser utilizado dependendo da ocasião do uso.
    Exemplo:
        if lp.criar_arquivo_txt(nome) is True:
            print('Arquivo lido!!')
        else:
            print('Arquivo não existe!!')
"""

</code></pre>

