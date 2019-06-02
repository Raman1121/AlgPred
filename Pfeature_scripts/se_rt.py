

import math
from collections import Counter
import pandas as pd
import numpy as np
import os
import sys
import csv
import getopt

def splitstring_res(filename,Nlength,Clength):
    data=list((pd.read_csv(filename,sep=',',header=None)).iloc[:,0])
    s=[]
    s1=[]
    for i in range(len(data)):
        s=data[i][Nlength:]
        s1=s1+[s[:-Clength]] 
    return (s1)

def entropy_single(seq):
    seq=seq.upper()
    num, length = Counter(seq), len(seq)
    return -sum( freq/length * math.log(freq/length, 2) for freq in num.values())

def se_rt(filename,outt,nt,ct):
    data=splitstring_res(filename,nt,ct)
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
    number1 = 1
    number2 = 1	
    if len(argv[1:]) == 0:
        print ("\nUsage: se_rt.py -i inputfile -o outputfile -m number1 -n number2\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')
        print('number1 : number of N-Terminal residues\n')
        print('number2 : number of C-Terminal residues\n') 			
        sys.exit()	
		
    try:
      opts, args = getopt.getopt(argv,"i:o:m:n:",["ifile=","ofile=","m=","n="])
    except getopt.GetoptError:
        print ("\nUsage: se_rt.py -i inputfile -o outputfile -m number1 -n number2\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')
        print('number1 : number of N-Terminal residues\n')
        print('number2 : number of C-Terminal residues\n') 			
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ('\nse_rt.py -i inputfile -o outputfile -m number1 -n number2\n')
            print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
            print('outputfile : is the file of feature vectors\n')
            print('number1 : number of N-Terminal residues\n')
            print('number2 : number of C-Terminal residues\n') 			
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-m", "--m"):
            m = int(sys.argv[6])
        elif opt in ("-n", "--n"):
            n = int(sys.argv[8])			
			
    se_rt(sys.argv[2],sys.argv[4],int(sys.argv[6]),int(sys.argv[8]))

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])	

