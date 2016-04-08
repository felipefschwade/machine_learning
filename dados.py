#Importa a biblioteca para trabalhar com CSV
import csv

def carregarAcessos():
	X = []
	Y = []

	#Abre o arquivo no modo "r"ead "b"inarie
	arquivo = open('acesso_pagina.csv', 'rb')
	#utiliza a funcao reader para assimilar o arquivo ao que for lido
	lido = csv.reader(arquivo)
	lido.next() #devolve o proximo item partindo do objeto
	for linha in lido:
		 #seleciona apenas os valores de acessou_home, como_funciona e acessou_contato
		dado = [int(linha[0]), int(linha[1]), int(linha[2])]
		X.append(dado)
		#seleciona apenas o referente a comprou
		Y.append(int(linha[3])) 
	return X, Y

def carregarBuscas():
	X = []
	Y = []

	#Abre o arquivo no modo "r"ead "b"inarie
	arquivo = open('buscas.csv', 'rb')
	lido = csv.reader(arquivo)
	lido.next() #devolve o proximo item partindo do objeto
	for linha in lido:
		 #seleciona apenas os valores de nome, busca e logado
		dado = [int(linha[0]), linha[1], int(linha[2])]
		X.append(dado)
		#seleciona apenas o referente a comprou
		Y.append(int(linha[3])) 
	return X, Y