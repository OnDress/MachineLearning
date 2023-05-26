import numpy as np
import pandas as pd
import search

def main():

    df = pd.read_csv("small-test-dataset.txt", sep= "  ", header= None)

    search.feature_search(df)

if __name__ == "__main__": main()

