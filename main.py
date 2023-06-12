import numpy as np
import pandas as pd
import math
import search

def main():
    print("Welcome to 862173656's Feature Selection Algorithm")
    file = input("Enter the name of the file to test: ")

    df = pd.read_csv(file, sep= "\s+", header= None)
    print("Type the number of the Algorithm you wish to run: ")
    print("1 - Forward Selection")
    algorithm = input("2 - Backward Elimination\n")
    if algorithm == '1':
        all_features = set()
        for i in range(1,len(df.columns)):
            all_features.add(i)
        print("This data has " + str(len(df.columns) - 1) + " features, with " + str(df.shape[0]) + " instances" )
        print("Running nearest neighbor with no features (default rate), using \'leave-one-out\' evaluation, I get an accuracy of: " + str(search.leave_one_out_cross_validation(df,all_features, None, "none")))
        print("Beginning Search: ")
        search.forward_search(df)
    elif algorithm == '2':
        all_features = set()
        for i in range(1,len(df.columns)):
            all_features.add(i)
        print("This data has " + str(len(df.columns) - 1) + " features, with " + str(df.shape[0]) + " instances" )
        print("Running nearest neighbor with no features (default rate), using \'leave-one-out\' evaluation, I get an accuracy of: " + str(search.leave_one_out_cross_validation(df,all_features, None, "none")))
        print("Beginning Search: ")
        search.backward_elimination(df)




if __name__ == "__main__": main()

