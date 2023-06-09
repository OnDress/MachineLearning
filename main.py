import numpy as np
import pandas as pd
import math
import search

def main():

    df = pd.read_csv("CS170_Spring_2023_Large_data__73.txt", sep= "\s+", header= None)
    search.feature_search(df)

if __name__ == "__main__": main()

