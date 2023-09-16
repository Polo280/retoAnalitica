import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path_csv = "credit_risk.csv"
path_out = "OutputAct2"

def main():
    # Abrir archivos
    output = open(path_out, 'w')
    df = pd.read_csv(path_csv)      # Convertir csv a Dataframe

    # Agregar estadisticos describe() a output file
    output.write("DESCRIBE\n")
    output.write(df.describe().to_string())

    # Encontrar variables maximas y minimas
    output.write("\n\nEdad max: " + str(df['Age'].max()) + "\n")
    output.write("Edad min: " + str(df['Age'].min()) + "\n")
    output.write("Rango: " + str(df['Age'].max() - df['Age'].min())+ "\n\n")

    output.write("Ingreso maximo: " + str(df['Income'].max()) + "\n")
    output.write("Ingreso minimo: " + str(df['Income'].min()) + "\n")
    output.write("Rango: " + str(df['Income'].max() - df['Income'].min()) + "\n\n")

    output.write("Prestamo maximo: " + str(df['Amount'].max()) + "\n")
    output.write("Prestamo minimo: " + str(df['Amount'].min()) + "\n")
    output.write("Rango: " + str(df['Amount'].max() - df['Amount'].min()) + "\n\n")

    output.write("Tasa maxima: " + str(df['Rate'].max()) + "\n")
    output.write("Tasa minima: " + str(df['Rate'].min()) + "\n")
    output.write("Rango: " + str(df['Rate'].max() - df['Rate'].min()) + "\n\n")

    output.write("Percentil ingreso max: " + str(df['Percent_income'].max()) + "\n")
    output.write("Percentil ingreso min: " + str(df['Percent_income'].min()) + "\n")
    output.write("Rango: " + str(df['Percent_income'].max() - df['Percent_income'].min()) + "\n\n")

    output.write("Longitud historial cred max: " + str(df['Cred_length'].max()) + "\n")
    output.write("Longitud historial cred min: " + str(df['Cred_length'].min()) + "\n")
    output.write("Rango: " + str(df['Cred_length'].max() - df['Cred_length'].min()) + "\n\n")

    # Ver los tipos de las variables en el dataframe
    output.write("\n" + "TIPOS DE DATOS" + "\n" + str(df.dtypes) + "\n")  # El tipo object se refiere a strings

    # Algunos otros estadisticos
    output.write("\nESTADISTICOS ADICIONALES\nEdad\n")
    output.write("Media: " + str(df['Age'].mean()) + "\n")
    output.write("Mediana: " + str(df['Age'].median()) + "\n")
    output.write("Desviacion estandar: " + str(df['Age'].std()) + "\n\n")

    output.write("Ingreso\nMedia: " + str(df['Income'].mean()) + "\n")
    output.write("Mediana: " + str(df['Income'].median()) + "\n")
    output.write("Desviacion estandar: " + str(df['Income'].std()) + "\n")

    output.write("Prestamo cantidad\nMedia: " + str(df['Amount'].mean()) + "\n")
    output.write("Mediana: " + str(df['Amount'].median()) + "\n")
    output.write("Desviacion estandar: " + str(df['Amount'].std()) + "\n")

    output.write("Tasa de interes\nMedia: " + str(df['Rate'].mean()) + "\n")
    output.write("Mediana: " + str(df['Rate'].median()) + "\n")
    output.write("Desviacion estandar: " + str(df['Rate'].std()) + "\n")

    output.write("Percentil Ingreso\nMedia: " + str(df['Percent_income'].mean()) + "\n")
    output.write("Mediana: " + str(df['Percent_income'].median()) + "\n")
    output.write("Desviacion estandar: " + str(df['Percent_income'].std()) + "\n")

    output.write("Longitud historial\nMedia: " + str(df['Cred_length'].mean()) + "\n")
    output.write("Mediana: " + str(df['Cred_length'].median()) + "\n")
    output.write("Desviacion estandar: " + str(df['Cred_length'].std()) + "\n")

    output.close()

if __name__ == "__main__":
    main()
    print("Program terminated correctly")