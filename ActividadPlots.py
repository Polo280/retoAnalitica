import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import seaborn as sns
import numpy as np

path_csv = "credit_risk.csv"
path_out = "OutputAct3"

def main():
    # Abrir archivos
    output = open(path_out, 'w')
    df = pd.read_csv(path_csv)  # Convertir csv a Dataframe

if __name__ == '__main__':
    main()
    print("Program terminated correctly")
    exit()