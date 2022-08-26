import numpy as np     #Importando bibliotecas necessárias
import time 
import os

caminho = r'c:\Users\Particular\Desktop\PYTHON\Instancias'   #Insira aqui o caminho onde se encontra os arquivos .txt
extensao = 'txt'                                             #Deseja que o arquivo seja salvo em outra extensão? Padrão: .doc
os.chdir(caminho)

def contaMatriz (f_caminho):
    with open(f_caminho, 'rb') as f: 
        matriz = np.genfromtxt(f, dtype = 'int32')  #Usei genfromtxt da Numpy para pegar a informação dos txt e transformar em matriz
    nomeArquivo = os.path.basename(f_caminho)       #Pego o nome dos txt
    print (nomeArquivo)                             #Printando o nome
    linCol = matriz.shape                           #Shape dirá as dimensões da matriz e passará para linCol
    print (linCol)                                  #Resultados são printados
    salvaArquivos(f_caminho, nomeArquivo, linCol)   #Hora de salvar o arquivo


def salvaArquivos (f_caminho, nomeArquivo, linCol):
    t_total = time.time() - t_inicio                                                     #Timer acaba aqui
    resultado = str(nomeArquivo) + " " + str(linCol) + " ; " + str("%.4f" % t_total)     #Resultados são unidos
    arquivo = open(caminho + r'\resultados.'+ extensao, 'a+')                            #Os resultados serão armazenados no caminho selecionado anteriormente
    arquivo.writelines(resultado + '\n')
    arquivo.close()


def abreArquivos (f_caminho):               #abreArquivos recebe o caminho 
    for f in os.listdir():                  #Aqui checamos o caminho          
        if f.endswith(".txt"):              #Checa se o arquivo é um .txt
            f_caminho = f"{caminho}\{f}"    #Encontrei minha instância  
            contaMatriz(f_caminho)          #Enviando o caminho da instância 


if __name__ == "__main__":
    t_inicio = time.time() #Vou começar a medir o tempo de execução a partir daqui
    abreArquivos(caminho)  #AbreArquivos é chamado