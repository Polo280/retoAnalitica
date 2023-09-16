import pandas as pd
# Mean mode std dev mediana

path_csv = "../peso_estatura_genero.csv"
path_out = "Output.txt"

def main():
    # Abrir archivos
    output = open(path_out, 'w')
    df = pd.read_csv(path_csv)      # Convertir csv a Dataframe

    output.write("ALGUNOS ESTADISTICOS DEL DATAFRAME\n")  # Obtencion de estadisticos basicos del dataframe
    output.write(df.describe().to_string())

    output.close()

if __name__ == "__main__":
    main()
    print("Program terminated correctly")