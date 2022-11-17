#importando as bibliotecas
import os, requests, json
#cores
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
blue = '\033[94m'
r = clear+red+bold
g = clear+green+bold
c = clear+cyan+bold
b = clear+blue+bold
y = clear+yellow+bold
#limpando a tela
os.system('clear')

#criando uma função
def consultar(cep):

    #Fazendo o requisito para obiter as informacões da Api
    req = requests.get(f'https://viacep.com.br/ws/{cep}/json')

    #convertendo o arquivo json para dic, pra pode usar as informacoes no python
    cp = req.json()

    #impriminto o resultado na tela
    print(c+"\n_______________Consulta Cep v: Beta_______________")
    print("                                     by: HIRO KAMI")
    print(b+"Cep:"+g+cp['cep'])
    print(b+"Logradouro: "+g+cp['logradouro'])
    print(b+"Complemento: "+g+cp['complemento'])
    print(b+"Bairro: "+g+cp['bairro'])
    print(b+"Cidade: "+g+cp['localidade'])
    print(b+"Estado: "+g+cp['uf'])
    print(b+"DDD: "+g+cp['ddd'])
    print(c+"__________________________________________________")

#pedindo uma entrada do usuario
entrada = input(g+"Digite o Cep: "+y)

#chamando á função
consultar(entrada)
