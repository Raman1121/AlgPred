

import math
from collections import Counter
import pandas as pd
import numpy as np
import os
import sys
import csv
import getopt

def splitstring_C(filename, Clength):
    data=list((pd.read_csv(filename,sep=',',header=None)).iloc[:,0])
    s=[]
    for i in range(len(data)):
        s=s+[data[i][-Clength:]]        
    return (s)

def ser_ct(filename,outt,ct):
    data=splitstring_C(filename,ct)
    GH=[]
    for i in range(len(data)):
        my_list={'A':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'K':0,'L':0,'M':0,'N':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'V':0,'W':0,'Y':0}
        data1=''
        data1=str(data[i])
        data1=data1.upper()
        allowed = set(('A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y'))
        is_data_invalid = set(data1).issubset(allowed)   
        if is_data_invalid==False:
            print("Error: Please check for invalid inputs in the sequence.","\nError in: ","Sequence number=",i+1,",","Sequence = ",data[i],",","\nNOTE: Spaces, Special characters('[@_!#$%^&*()<>?/\|}{~:]') and Extra characters(BJOUXZ) should not be there.")
            return
        seq=data[i]
        seq=seq.upper()
        num, length = Counter(seq), len(seq)
        num=dict(sorted(num.items()))
        C=list(num.keys())
        F=list(num.values())
        for key, value in my_list.items():
             for j in range(len(C)):
                if key == C[j]:
                    my_list[key] = round(((F[j]/length)* math.log(F[j]/length, 2)),3)
        GH.append(list(my_list.values()))
    file= open(outt,'w', newline='')#output file
    with file:
        writer=csv.writer(file);
        writer.writerow(('A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y'));		
        writer.writerows(GH);
    
    return GH
	
def main(argv):
    global inputfile
    global outputfile	
    inputfile = ''
    outputfile = ''	
    number = 1	
    if len(argv[1:]) == 0:
        print ("\nUsage: ser_ct.py -i inputfile -o outputfile -n number\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')
        print('number : number of C-Terminal residues\n') 			
        sys.exit()	
		
    try:
      opts, args = getopt.getopt(argv,"i:o:n:",["ifile=","ofile=","n="])
    except getopt.GetoptError:
        print ("\nUsage: ser_ct.py -i inputfile -o outputfile -n number\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')
        print('number : number of C-Terminal residues\n') 		
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ('\nser_ct.py -i inputfile -o outputfile -n number\n')
            print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
            print('outputfile : is the file of feature vectors\n')
            print('number : number of C-Terminal residues\n') 			
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-n", "--n"):
            n = int(sys.argv[6])			
			
    ser_ct(sys.argv[2],sys.argv[4],int(sys.argv[6]))

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])		



