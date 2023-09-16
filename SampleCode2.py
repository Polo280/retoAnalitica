import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# LIBRERIAS A USAR
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

path_csv = "peso_estatura_genero.csv"

def main():
    df = pd.read_csv(path_csv)
    modelo = linear_model.LinearRegression()
    x = df["Estatura"].to_numpy(dtype="float").reshape(-1, 1)
    y = df["Peso"].to_numpy(dtype="float")
    modelo.fit(x, y)
    modelo.score(x, y)

    b0 = modelo.intercept()
    print(b0)
    c = modelo.coef_
    print(c)

    yp = modelo.predict(x)
    print(yp)

    fig = plt.figure()
    plt.scatter(df["Estatura"], df["Peso"], marker="o")
    plt.plot(x, yp)
    plt.show()

    df.Peso = df.Peso * 2
    transform = PolynomialFeatures()
    transform.fit(x)
if __name__ == "__main__":
    main()
    print("Program terminated correctly")
