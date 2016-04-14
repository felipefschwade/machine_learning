from collections import Counter
import pandas as pd #Utiliza a biblioteca pandas de Data Analysis
df = pd.read_csv('buscas.csv') #Df = data_frame
Y_df = df['comprou'] #O pandas torna o cabecaalho como referencia ao dado, nao necessitando referencia numerica
X_df = df[['home', 'busca', 'logado']] #Para utilizar mais de uma coluna devemos passar um array como argumento
Xdummies_df= pd.get_dummies(X_df)
X = Xdummies_df.values
Y = Y_df.values
tamanho_de_treino = int(0.9 * len(X)) #define que o treino do algoritmo sera de 90 dos dados
tamanho_de_teste = int(0.1 * len(X)) #define que o teste do algoritmo sera de 10 dos dados
#cria as variaveis de teste e de treino
treino_X = X[:tamanho_de_treino]
treino_Y = Y[:tamanho_de_treino]
teste_X = X[-tamanho_de_teste:]
teste_Y = Y[-tamanho_de_teste:]
#importa a biblioteca do modelo bayesiano
from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(treino_X, treino_Y) #realiza o treino #realiza o teste
taxa_de_acerto = 100.0 * modelo.score(teste_X, teste_Y) #calcula a taxa de acerto
print "Taxa de acerto do algoritmo: %f" % taxa_de_acerto
#Testando a eficacia de um algoritmo que chuta tudo 0 ou 1
acerto_base = max(Counter(teste_Y).itervalues())
taxa_de_acerto_base = 100.0 * acerto_base / len(teste_Y)
print "Taxa de acerto base: %f" % taxa_de_acerto_base