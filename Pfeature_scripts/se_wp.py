
# coding: utf-8

# In[141]:


import math
from collections import Counter
import pandas as pd
import numpy as np
import os
import sys
import getopt
import csv


def entropy_single(seq):
    seq=seq.upper()
    num, length = Counter(seq), len(seq)
    return -sum( freq/length * math.log(freq/length, 2) for freq in num.values())

def se(filename,outt):
    data=list((pd.read_csv(filename,sep=',',header=None)).iloc[:,0])
#     print(data)
    Val=[]
    header=["Shannon-Entropy"]
    for i in range(len(data)):
        data1=''
        data1=str(data[i])
        data1=data1.upper()
        allowed = set(('A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y'))
        is_data_invalid = set(data1).issubset(allowed)   
        if is_data_invalid==False:
            print("Error: Please check for invalid inputs in the sequence.","\nError in: ","Sequence number=",i+1,",","Sequence = ",data[i],",","\nNOTE: Spaces, Special characters('[@_!#$%^&*()<>?/\|}{~:]') and Extra characters(BJOUXZ) should not be there.")
            return
        Val.append(round((entropy_single(str(data[i]))),3))
        #print(Val[i])
        file= open(outt,'w', newline='\n')#output file
        with file:
            writer=csv.writer(file,delimiter='\n');
            writer.writerow(header)
            writer.writerow(Val);
    return Val

def main(argv):
    global inputfile
    global outputfile	
    inputfile = ''
    outputfile = ''	
    #option = 1	
    if len(argv[1:]) == 0:
        print ("\nUsage: se.py -i inputfile -o outputfile\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')		
        sys.exit()	
		
    try:
      opts, args = getopt.getopt(argv,"i:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ("\nUsage: se.py -i inputfile -o outputfile\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')		
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ('\nse.py -i inputfile -o outputfile\n')
            print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
            print('outputfile : is the file of feature vectors\n')			
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
			
    se(sys.argv[2],sys.argv[4])

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])	

