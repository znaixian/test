# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:27:34 2019

@author: ncarucci
"""

def Capping(df, threshold):
    while (df.weight > threshold).any():
        print('Greater than %s? Cap it  ') %(threshold)
        largest = float(df.weight.nlargest(1))        
        df['weight_1'] = 0
        df['weight_1'][df.weight == threshold] = threshold
        num = len(df[df.weight == largest])  
        df['weight_1'][df.weight == largest] = threshold
        dist = (largest - threshold)*num
        total = df.weight[(df.weight_1 == 0)].sum()
        df['weight_1'][df.weight_1 == 0] = df.weight + dist*(df.weight/total)
        #file.weight_1.sum()
        del df['weight']
        df.rename(columns={'weight_1': 'weight'}, inplace=True) 
        return Capping(df, threshold) 