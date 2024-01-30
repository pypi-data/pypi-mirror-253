import os
import shutil
from fpdf import FPDF
import  PyPDF2
from collections import Counter
import re 
# import chardet
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas

# extensao = ".txt"
        
def criar_arquivo_txt(nome): 
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
    if os.path.exists(nome + '.txt'):
        with open(nome + '.txt', "r", encoding="utf-8") as arq:
            arquivo = arq.read()
            print(arquivo)
        return True
    else:
        return False
        

def escrever_arquivo_txt(nome):
    if os.path.exists(nome + '.txt'):
        with open(nome + '.txt', "a", encoding="utf-8") as arq:
            conteudo = input('-> ')
            arq.write(conteudo + " ")
        return True
    else:
        return False
  
  
def criar_arquivo_bin(nome):
    if os.path.exists(nome + '.bin'):
        with open(nome + '.bin', 'rb') as arq:
            arquivo = arq.read()
            print(arquivo)
    else:
        with open(nome + '.bin', 'wb') as arq:
            arq.write()
            
def abrir_arquivo_bin(nome):
    if os.path.exists(nome + '.bin'):    
        with open(nome + '.bin', "rb") as arq:
            arquivo = arq.read()
            print(arquivo)
        return True
    else:
        return False

def escrever_arquivo_bin(nome):
    if os.path.exists(nome + '.bin'):
        with open(nome + '.bin', "ab") as arq:
            conteudo = input('-> ')
            arq.write(conteudo + " ")
        return True
    else:
        return False

def listar_diretorio(diretorio, extensao):
    #raiz - dirs - arquivos
    for raiz, dirs, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if arquivo.endswith(extensao):
                for dir in dirs:
                    caminho_completo = os.path.join(raiz, dir, arquivo)
                    print(caminho_completo)

def diretorio_atual():
    return os.getcwd()

def criar_diretorio(nome_dir):
    os.mkdir(diretorio_atual()+'./'+nome_dir)

def copiar_diretorio_completo(src, dst):
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
    total = 0
    total_arq = 0
    total_dir = 0
    for caminho_atual, sub_dir, arquivos in os.walk(caminho):
        for a in arquivos:
            aux = os.path.join(caminho_atual, a)
            total += os.path.getsize(aux)
            total_arq = total_arq + 1
        for sub in sub_dir:
            aux_2 = os.path.join(caminho_atual, sub)
            total_dir = 1 + total_dir 
            total += tamanho_diretorio_kb(aux_2)
            
    return total/1024, total_arq, total_dir

def tamanho_arquivo_kb(caminho, nome_arq):
    return os.path.getsize(caminho + '\\' + nome_arq)

def palavra_chave(arquivo, palavra):
    ocorrencias = []
    count = 0

    with open(arquivo, 'r', encoding='utf-8') as file:
        for numero_linha, linha in enumerate(file, 1):
            if palavra in linha:
                count += 1
                ocorrencias.append((numero_linha, linha.strip()))

    return ocorrencias, count

def contar_palavras_mais_frequentes(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        
    palavras = re.findall(r'\b\w+\b', conteudo.lower())

    stopwords = ["a", "e", "em", "este", "estes", "esta", "estas", "é", "no", "na", "tem", "as", "o", "os", "um", "uns", "uma", "umas", "para", "de", "da", "do", "das", "dos", "se", "então", "ele", "ela", "eles", "elas", "à", "ou", "por", "que", "com", "também", "the", "a", "an", "at", "by", "from", "how", "of", "on", "that", "to", "for", "in", "out", "I", "he", "she", "it", "they", "our", "them", "him", "her", "do", "will", "or", "with", "also", "and", "is", "are", "this", "can", "we", "ao", "são", "pelo", "seus","seu", "lhe"]
    palavras_filtradas = [palavra for palavra in palavras if palavra not in stopwords]
    
    contagem_palavras = Counter(palavras_filtradas)
    
    palavras_mais_frequentes = contagem_palavras.most_common(10)

    return palavras_mais_frequentes


def contar_caracteres(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        conteudo = file.read()
        quantidade_caracteres = len(conteudo)
    
    return quantidade_caracteres


def txt_pdf(arquivo, nome_arquivo):
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
    with open(arquivo, 'rb') as pdf:
        aux = PyPDF2.PdfReader(pdf)

        text = ""
        for page in aux.pages:
            text += page.extract_text()

    with open(arquivo_txt + '.txt', 'w', encoding='utf-8') as txt:
        txt.write(text)

def txt_bin(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as arq:
            conteudo_texto = arq.read()
        with open('output.bin', 'wb') as arq_bin:
            arq_bin.write(conteudo_texto.encode('utf-8'))
        return True
    else:
        return False

# bin_txt nao esquecer-----------------------

# palavras_mais_frequentes = contar_palavras_mais_frequentes(diretorio_atual()+'\\teste.txt')

# Mostra as 10 palavras mais frequentes
# print("As 10 palavras mais frequentes:")
# for palavra, frequencia in palavras_mais_frequentes:
#     print(f"{palavra}: {frequencia}")
# txt_bin('pedro.txt')

# txt_pdf('teste2.txt')
# pdf_to_txt('saida.pdf','saida2')

# diretorio = diretorio_atual()
# print(contar_caracteres('teste3.txt'))
# print(tamanho_diretorio_kb(diretorio_atual()))
# print(tamanho_arquivo_kb(diretorio_atual(), 'teste2.txt'))
# deletar_diretorio('teste')
# deletar_arquivo('teste.txt')
# palavra = palavra_chave('teste2.txt', 'amor')
# palavra = palavra_chave('teste2.txt', 'amor')
# print(palavra)

# if copiar_diretorio_completo(diretorio, r'C:\Users\nyddo\OneDrive\Área de Trabalho\Faculdade\POOII\teste') is True:
#     print('Arquivos copiados com sucesso!')
# else:
#     print('Arquivos nao copiados!')


# if mover_diretorio_completo(diretorio, r'C:\Users\nyddo\OneDrive\Área de Trabalho\Faculdade\POOII\teste') is True:
#     print('Arquivos movidos com sucesso!')
# else:
#     print('Arquivos nao movidos!')
    
# print(os.listdir(diretorio_atual()))

#listar_diretorio(diretorio, extensao)


# nome_arquivo = "teste" 


# if abrir_arquivo_txt(nome_arquivo) is True:
#     escrever_arquivo_txt(nome_arquivo)
#     abrir_arquivo_txt(nome_arquivo) 
# else:
#     criar_arquivo_txt(nome_arquivo)
#     abrir_arquivo_txt(nome_arquivo)



