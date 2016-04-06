#importa do arquivo dados a funcao acessos pode ser classe
from dados import carregarAcessos
#assimila X e Y ao resultaado da funcao
X, Y = carregarAcessos()

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(X, Y)
print modelo.predict([[1,0,1], [0, 1, 0]])