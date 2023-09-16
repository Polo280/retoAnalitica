import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path_csv = "peso_estatura_genero.csv"
path_out = "OutputSample.txt"

def main():
    # Abrir archivos
    output = open(path_out, 'w')
    df = pd.read_csv(path_csv)      # Convertir csv a Dataframe

    output.write("DESCRIBE\n")
    output.write(df.describe().to_string())

    df.Estatura = df.Estatura * 2.54
    df.Peso = df.Peso / 2.2
    print(df['Peso'].var())

    # PLOTTING
    x = np.linspace(0, 10, num=100)
    m = 2
    b = 5
    y = m * x + b
    fig = plt.figure(figsize=(5, 5))

    plt.plot(x, y)
    plt.title("Sample Graph")
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    plt.grid(True)
    plt.show()

    output.close()

if __name__ == "__main__":
    main()
    print("Program terminated correctly")