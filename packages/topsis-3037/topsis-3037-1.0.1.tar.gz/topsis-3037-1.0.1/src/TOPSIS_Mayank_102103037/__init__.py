from .main import topsis
import numpy as np 
from scipy.stats import rankdata
import sys
import pandas as pd 
def main():      
    if len(sys.argv) != 5:         
        print("ERROR! WRONG NUMBER OF PARAMETERS")         
        print("USAGES: $python <programName> <dataset> <weights array> <impacts array>")         
        print("EXAMPLE: $python programName.py data.csv 1,1,1,1 +,+,-,+ ")         
        exit(1)      
    dataset = pd.read_csv(sys.argv[1]).values     
    datasetwithheaing = pd.read_csv(sys.argv[1],index_col=False)     
    decisionMatrix = dataset[:, 1:]
    weights = [int(i) for i in sys.argv[2].split(',')]  
    impacts = sys.argv[3].split(',')
    name = sys.argv[4]     
    topsis(datasetwithheaing,dataset,decisionMatrix, weights, impacts,name)   

if __name__ == "__main__":
    main()