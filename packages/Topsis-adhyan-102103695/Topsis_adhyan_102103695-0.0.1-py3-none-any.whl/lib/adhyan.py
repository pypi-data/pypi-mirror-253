import pandas as pd
import numpy as np
import ast
import sys
import logging

# def fun(filepath,weights,impact,output):
def topsis():
    filepath="102103474-data.csv"

    weights=[1,1,1,1,1]
    # weights=ast.literal_eval(weights)

    impact=[1,-1,1,-1,1]
    # impact=ast.literal_eval(impact)

    output=submit.csv

    data=pd.read_csv(filepath,index_col='Fund Name')
    # print(data)
    # data.info()
    
    n = data.shape[1]
    if (n<3):
        logging.warning('Error')
        return
    if (len(weights)!=len(impact)!=len(data)):
        logging.warning('Error')
        return



    # weights=[1,1,1,1,1]
    # impact=[1,-1,1,-1,1]

    norm_data=data/np.sqrt((data ** 2).sum(axis=0))
    norm_data=norm_data*weights

    # impact=[1,-1,1,-1,1]
    rough=norm_data*impact
    

    best=rough.max().abs()
    
    worst=rough.min().abs()
    
    dist_best=np.sqrt(((norm_data-best)**2).sum(axis=1))
  
    dist_worst=np.sqrt(((norm_data-worst)**2).sum(axis=1))
  

    total_dist=dist_best+dist_worst
    performance=dist_worst/total_dist
    rank = pd.Series(performance, name='Performance').rank(ascending=False).astype(int)

    norm_data['Topsis Score']=performance
    norm_data['Rank']=rank
   
    norm_data.to_csv(output, index=False)


# if __name__ == "__main__":
#     topsis()
#     # Check if the correct number of command-line arguments is provided
#     if len(sys.argv) != 5:
#         logging.warning('Invalid no. of arguements')
#         sys.exit(1)


# filepath=sys.argv[1]

# weights=sys.argv[2]
# weights=ast.literal_eval(weights)

# impact=sys.argv[3]
# impact=ast.literal_eval(impact)
# output=sys.argv[4]
# fun(filepath,weights,impact,output)