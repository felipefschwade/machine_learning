#importa do arquivo dados a funcao acessos pode ser classe
from dados import carregarAcessos
#assimila X e Y ao resultaado da funcao
X, Y = carregarAcessos()
treino_X = X[:90]
treino_Y = Y[:90]
teste_X = X[-9:]
teste_Y = Y[-9:]
from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(treino_X, treino_Y)
print modelo.predict(teste_X)
taxa_de_acerto = 100.0 * modelo.score(teste_X, teste_Y)
print taxa_de_acerto