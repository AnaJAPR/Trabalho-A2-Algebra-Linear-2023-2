import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

# Doing a linear regresion with a random data set
# x,y = make_regression(n_samples=200, n_features=1, noise=30)

# plt.scatter(x,y)

df = pd.read_csv("Sleep_Efficiency.csv").dropna()

x = df["Sleep duration"].values.reshape(-1,1)
y = df["Caffeine consumption"].values

# creating a linear regression model and fitting the model to the data
modelo = LinearRegression()
modelo.fit(x,y)

# defining coefficients
a_coeff = modelo.coef_
l_coeff = modelo.intercept_

print(a_coeff)
print(l_coeff)

# y = a + b*x
# y = l_coeff + a_coeff * x
# print(y)

# defining some characteristics of the graph
plt.scatter(x,y)
plt.plot(x, l_coeff + a_coeff*x, color='orange') # line representing linear regression
plt.scatter(0, l_coeff + a_coeff*2.5, color='lightgreen', s = 20) 

# This shows the graph
# plt.show()








'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_excel("spotify-2023.xlsx").dropna()

coluna_1 = df["streams"].values
coluna_2 = df["in_deezer_playlists"].values

plt.figure()
plt.scatter(coluna_1, coluna_2)
plt.xlabel("coluna_1")
plt.ylabel("coluna_2")

plt.figure()
plt.scatter(np.log(coluna_1), np.log(coluna_2))
plt.xlabel("log(coluna_1)")
plt.ylabel("log(coluna_2)")

t = np.log(coluna_1)
ones = np.ones(len(t))
b = np.log(coluna_2)

A = np.column_stack([ones, t])

AtA = A.T @ A
Atb = A.T @ b

x_hat = np.linalg.solve(AtA, Atb)

t_linspace = np.linspace(np.min(t), np.max(t), 101)

least_square = x_hat[0] + x_hat[1] * t
least_square_plot = x_hat[0] + x_hat[1] * t_linspace

MSE = np.mean((least_square - b)**2)

print('MSE: ', MSE)

regr = linear_model.LinearRegression()
regr.fit(t.reshape(-1, 1), b)

least_square_sklearn_plot = regr.predict(t_linspace.reshape(-1, 1))
least_square_sklearn = regr.predict(t.reshape(-1, 1))

fig, ax = plt.subplots()
plt.scatter(t, b, label="df")
plt.plot(t_linspace, least_square_plot, color='k', label='numpy')
plt.plot(t_linspace, least_square_sklearn_plot, 'k--', label='sklearn', linewidth=5)
plt.xlabel('log(coluna_1')
plt.ylabel('log(coluna_2)')
plt.legend()

# plt.show()
'''