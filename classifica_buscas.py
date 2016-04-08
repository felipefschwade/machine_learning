import pandas as pd #Utiliza a biblioteca pandas de Data Analysis
df = pd.read_csv('buscas.csv') #Df = data_frame
Y_df = df['comprou'] #O pandas torna o cabecaalho como referencia ao dado, nao necessitando referencia numerica
X_df = df[['home', 'busca', 'logado']] #Para utilizar mais de uma coluna devemos passar um array como argumento
Xdummies_df= pd.get_dummies(X_df)
X = Xdummies_df.values
Y = Y_df.values
print Y
print X