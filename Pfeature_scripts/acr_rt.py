
# coding: utf-8

# In[3]:


# autocorr('filepath','aaindex',d)
#input: csv of sequences, aaindex of property for which autocorrelation descriptors are to be estimated, d is the lag (<=30)
#output: for every sequence (with aaindex and d fixed) three autocorrelation values - NMB,Moran and Geary

import math
import pandas as pd
import numpy as np
import os
import csv
import sys
import getopt
import warnings
warnings.filterwarnings("ignore") 
def splitstring_NC(filename,Nlength,Clength):
    data=list((pd.read_csv(filename,sep=',',header=None)).iloc[:,0])
    s=[]
    s1=[]
    for i in range(len(data)):
        s=data[i][Nlength:]
        s1=s1+[s[:-Clength]] 
    return (s1)
def p_aa(prop,a):
    if ((a.upper()=='A') or (a.upper()=='C') or (a.upper()=='D') or (a.upper()=='E') or (a.upper()=='F') or (a.upper()=='G') or (a.upper()=='H') or (a.upper()=='I') or (a.upper()=='K') or (a.upper()=='L') or (a.upper()=='M') or (a.upper()=='N') or (a.upper()=='P') or (a.upper()=='Q') or (a.upper()=='R') or (a.upper()=='S') or (a.upper()=='T') or (a.upper()=='V') or (a.upper()=='W') or (a.upper()=='Y')):
        data=pd.read_table('Data/z_aaindex.csv',sep=',',index_col='INDEX' )
        p=data.loc[prop][a.upper()]
        return p
    else:
        print("Error!: Invalid sequence. Special character(s)/invalid amino acid letter(s) present in input.")
        return  
def NMB(prop,seq,d):
    if (d<=30):
        sum=0
        for i in range(len(seq)-d):
            sum=sum+p_aa(prop,seq[i])*p_aa(prop,seq[i+d])
        ats=sum/(len(seq)-d)
        return ats
    else:
        print("Error!: d should be less than equal to 30")
        return
def pav(prop,seq):
    av=0
    for i in range(len(seq)):
        av=av+p_aa(prop,seq[i])
    av=av/len(seq)
    return av
def moran(prop,seq,d):
    if (d<=30):
        s1=0
        s2=0
        p_bar=pav(prop,seq)
        for i in range(len(seq)-d):
            s1=s1+(p_aa(prop,seq[i])-p_bar)*(p_aa(prop,seq[i+d])-p_bar)
        for i in range(len(seq)):
            s2=s2+(p_aa(prop,seq[i])-p_bar)*(p_aa(prop,seq[i])-p_bar)
        return (s1/(len(seq)-d))/(s2/len(seq))
    else:
        print("Error!: d should be less than equal to 30")
        return
def geary(prop,seq,d):
    if (d<=30):
        s1=0
        s2=0
        p_bar=pav(prop,seq)
        for i in range(len(seq)-d):
            s1=s1+(p_aa(prop,seq[i])-p_aa(prop,seq[i+d]))*(p_aa(prop,seq[i])-p_aa(prop,seq[i+d]))
        for i in range(len(seq)):
            s2=s2+(p_aa(prop,seq[i])-p_bar)*(p_aa(prop,seq[i])-p_bar)
        return (s1/(2*(len(seq)-d)))/(s2/(len(seq)-1))
    else:
        print("Error!: d should be less than equal to 30")
        return
def acr_rt(filename,outt,m,n,d):
    if (d<=30):
        seq_data=splitstring_NC(filename,m,n)
        prop=list((pd.read_csv('Data/aaindices.csv',sep=',',header=None)).iloc[0,:])
        output=[[]]
        for k in range(len(prop)):
            output[0]=output[0]+['NMB_ac','Moran_ac','Geary_ac']
        temp=[]
        #header=['Sequence','aaindex','Normalized Moreau-Broto','Moran','Geary']
        #output.append(header)
        for i in range(len(seq_data)):
            for j in range(len(prop)):
                temp=temp+[round(NMB(prop[j],seq_data[i],d),3),round(moran(prop[j],seq_data[i],d),3),round(geary(prop[j],seq_data[i],d),3)]
            output.append(temp)
            temp=[]
        file = open(outt,'w')
        with file:
            writer = csv.writer(file);
            writer.writerows(output);
        return output
    else:
        print("Error!: d should be less than equal to 30")
        return
		
def main(argv):
    global inputfile
    global outputfile	
    inputfile = ''
    outputfile = ''	
    number1 = 1
    number2 = 1	
    if len(argv[1:]) == 0:
        print ("\nUsage: acr_rt.py -i inputfile -o outputfile -m number1 -n number2 -d lag\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')
        print('number : number of N-Terminal residues\n')
        print('d : lag(<=30)\n') 			
        sys.exit()	
		
    try:
      opts, args = getopt.getopt(argv,"i:o:m:n:d:",["ifile=","ofile=","m=","n=","d="])
    except getopt.GetoptError:
        print ("\nUsage: acr_rt.py -i inputfile -o outputfile -m number1 -n number2 -d lag\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')
        print('number : number of N-Terminal residues\n')
        print('d : lag(<=30)\n') 
        #print('error\n')		
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ('\nacr_rt.py -i inputfile -o outputfile -m number1 -n number2 -d lag\n')
            print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
            print('outputfile : is the file of feature vectors\n')
            print('number : number of N-Terminal residues\n')
            print('d : lag(<=30)\n') 			
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-m", "m"):
            n = int(sys.argv[6])			
        elif opt in ("-n", "n"):
            n = int(sys.argv[8])
        elif opt in ("-d", "d"):
            d = int(sys.argv[10])			
			
    acr_rt(sys.argv[2],sys.argv[4],int(sys.argv[6]),int(sys.argv[8]),int(sys.argv[10]))

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])		

