import numpy as np
import pandas as pd


def topsis(Data,Weights,Impacts):
    df = Data
    Items_extracted = Data[Data.columns[0]]
    Data = Data.drop(Data.columns[0],axis=1)
    
    # Taking Root of Sum of Squres of each column and dividing it with individuals
    for index,col in enumerate(Data.columns):
        Root_Of_Sq_Sum = np.sqrt(sum(np.square(Data[col])))  #taking Root of Sum of Squares
        Data[col] = (Data[col]*Weights[index])/Root_Of_Sq_Sum  #Dividing with RSS and Multiplying with weight individuals
        
    #Calculating V_plus and V_neg of each column    
    V_pos = [np.max(Data[col]) if Impacts[index] == '+' else round(np.min(Data[col]), 4) for index, col in enumerate(Data.columns)]
    V_neg = [np.min(Data[col]) if Impacts[index] == '+' else round(np.max(Data[col]), 4) for index, col in enumerate(Data.columns)]
     
    #Calculating Euclidean distance 
    S_pos = [np.sqrt(sum(np.square(x - y) for x, y in zip(V_pos, Data.iloc[i]))) for i in range(Data.shape[0])]
    S_neg = [np.sqrt(sum(np.square(x - y) for x, y in zip(V_neg, Data.iloc[i]))) for i in range(Data.shape[0])]
    
    #Calculating Performance
    P = [round(y/(x+y),5) for x,y in zip(S_pos,S_neg)]
          
    #Creating Dataframe only with Performance and Ranks      
    performance_Data = pd.DataFrame(data ={'Items':Items_extracted , 'Performance':P})
    performance_Data['Rank'] = performance_Data['Performance'].rank(ascending=True)
    
    #Dataframe fith Performance and older data
    df['Performance'] = P
    df['Rank'] = df['Performance'].rank(ascending=True)

    df.to_csv('102116120-result.csv',index=False)

    return (df)
        

  