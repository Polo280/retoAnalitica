import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path_csv = "peso_estatura_genero.csv"
path_out = "OutputSample.txt"

def main():
    # Abrir archivos
    output = open(path_out, 'w')
    df = pd.read_csv(path_csv)      # Convertir csv a Dataframe

    # Agregar estadisticos describe() a output file
    output.write("DESCRIBE\n")
    output.write(df.describe().to_string())
    output.write("\n\n")

    # Encontrar variables maximas y minimas
    output.write("Peso maximo: " + str(df['Peso'].max()) + "\n")
    output.write("Peso minimo: " + str(df['Peso'].min()) + "\n\n")
    output.write("Estatura maxima: " + str(df['Estatura'].max()) + "\n")
    output.write("Estatura minima: " + str(df['Estatura'].min()) + "\n\n")

    # Rangos
    output.write("Rango de peso: " + str(df['Peso'].max() - df['Peso'].min()) + "\n")
    output.write("Rango de estatura: " + str(df['Estatura'].max() - df['Estatura'].min()) + "\n")

    # Ver los tipos de las variables en el dataframe
    output.write("\n" + "TIPOS DE DATOS" + "\n" + str(df.dtypes) + "\n") # El tipo object se refiere a strings

    # Algunos otros estadisticos
    output.write("\nESTADISTICOS ADICIONALES\nPeso\n")
    output.write("Media: " + str(df['Peso'].mean()) + "\n")
    output.write("Mediana: " + str(df['Peso'].median()) + "\n")
    output.write("Desviacion estandar: " + str(df['Peso'].std()) + "\n\n")

    output.write("Estatura\nMedia: " + str(df['Estatura'].mean()) + "\n")
    output.write("Mediana: " + str(df['Estatura'].median()) + "\n")
    output.write("Desviacion estandar: " + str(df['Estatura'].std()) + "\n")
    output.close()

if __name__ == "__main__":
    main()
    print("Program terminated correctly")