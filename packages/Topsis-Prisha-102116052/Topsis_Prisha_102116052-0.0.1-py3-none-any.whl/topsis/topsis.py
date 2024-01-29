import pandas as pd 
import numpy as np
import sys
import os

def normalize(df):
    divisor = df.apply(lambda x: x**2).apply(sum).apply(lambda x: x**0.5)
    df = df.div(divisor)
    return df

def weight_normalized(df, weights):
    df = df.mul(weights)
    return df

def best_worst(df, impacts):
    best=[]
    worst=[]
    for i in range(len(impacts)):
        if impacts[i]=='+':
            best.append(max(df.iloc[:,i]))
            worst.append(min(df.iloc[:,i]))
        else:
            best.append(min(df.iloc[:,i]))
            worst.append(max(df.iloc[:,i]))
    return (best,worst)

def calc_performance(df, best, worst):
    s_best=[]
    s_worst=[]
    for i in range(len(df)):
        s_best.append((sum((df.loc[i] - best)**2))**0.5)
        s_worst.append((sum((df.loc[i] - worst)**2))**0.5)
    s_total = [i+j for i,j in zip(s_worst,s_best)]
    performance = [i/j for i,j in zip(s_worst,s_total)]
    df.loc[:,'Topsis Score'] = performance

def rank(df):
    sorted_array = df.loc[:,'Topsis Score'].argsort()
    ranks = np.empty_like(sorted_array)
    ranks[sorted_array] = np.arange(len(sorted_array))
    n=len(sorted_array)
    ranks = [n-i for i in ranks]
    df.loc[:,'Rank'] = ranks

def topsis(input,weights, impacts):
    df=input.iloc[:,1:]

    df = normalize(df)
    df = weight_normalized(df,weights)

    (best,worst) = best_worst(df,impacts)
    calc_performance(df,best,worst)
    rank(df)
    return df

if __name__=="__main__":
    n= len(sys.argv)
    if (n!=5):
        print(n)
        print("Number of Arguments did not match!")
        sys.exit(1)

    arg1 = sys.argv[1]
    
    if (os.path.isfile(r"{}".format(arg1))==False):
        print("File Not Found Error!")
        sys.exit(1)
    
    arg2 = [float(i) for i in sys.argv[2].split(",")]
    arg3 = sys.argv[3].split(",")
    arg4 = sys.argv[4]
    
    df = pd.read_csv(r"{}".format(arg1))
    cols = len(df.axes[1])
    if (cols<3):
        print("Insufficient Data to perform TOPSIS!")
        sys.exit(1)
    if (len(df.select_dtypes(include='number').axes[1])<cols-1):
        print("Non numeric data found!")
        sys.exit(1)
    if (len(arg2)!=cols-1 or len(arg3)!=cols-1):
        print("Weights or Impacts are not in specified format!")
        sys.exit(1)
    for i in arg3:
        if i not in ['+','-']:
            print("Impacts need to be + or -!")
            sys.exit(1)

    res = topsis(df, arg2, arg3)
    res.to_csv(r"{}".format(arg4), index=False)