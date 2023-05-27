import numpy as np
import pandas as pd
import math
import search

def main():

    df = pd.read_csv("large-test-dataset-1.txt", sep= "  ", header= None)
    #df2 = df.iloc[0:len(df.index),[1,4,6]]
    search.feature_search(df)
    """test = set()
    test.add(1)
    test.add(4)
    test.add(6)
    #slam = []
    #for num in test:
        #slam.append(num)
    #df2 = df.iloc[0:len(df.index),slam]
    slam = df.iloc[0,1:len(df.columns)]
    bam = df.iloc[29,1:len(df.columns)]
    sum = 0
    for i in range(0,len(slam.index)):
        sum += (float(slam.iloc[i]) - float(bam.iloc[i]))**2
    distance = math.sqrt(sum)
    print(distance)
    #print(df.iloc[5,0])
    print(bam)"""
    #for i in range (0,len(df.index)):
     #   print(str(i) + ": " + str(df.iloc[i,40]))
    #print(df)

if __name__ == "__main__": main()

