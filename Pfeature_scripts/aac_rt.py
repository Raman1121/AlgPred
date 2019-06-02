import pandas as pd
import sys
import os
import numpy as np
import getopt
std = list("ACDEFGHIKLMNPQRSTVWY")
def aac_rt(file,out,m,n):
    filename, file_extension = os.path.splitext(file)
    f = open(out, 'w')
    sys.stdout = f
    df = pd.read_csv(file, header = None)
    zz = df.iloc[:,0]
    print("A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y,")
    for j in range(0,len(zz)):
        str = zz[j][m:-n]
        q = str.upper()
        if len(q)>=1:
            for i in std:
                count = 0
                for k in q:
                    temp1 = k
                    if temp1 == i:
                        count += 1
                    composition = (count/len(q))*100
                print("%.2f"%composition, end = ",")
            print("")
            f.truncate()
        else:
            print("Warning: Peptide length is small")
            
def main(argv):
    global inputfile
    global outputfile	
    inputfile = ''
    outputfile = ''	
    number1 = 1
    number2 = 1	
    if len(argv[1:]) == 0:
        print ("\nUsage: aac_rt.py -i inputfile -o outputfile -m number1 -n number2\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')
        print('number1 : number of N-Terminal residues\n')
        print('number2 : number of C-Terminal residues\n') 			
        sys.exit()	
		
    try:
      opts, args = getopt.getopt(argv,"i:o:m:n:",["ifile=","ofile=","m=","n="])
    except getopt.GetoptError:
        print ("\nUsage: aac_rt.py -i inputfile -o outputfile -m number1 -n number2\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')
        print('number1 : number of N-Terminal residues\n')
        print('number2 : number of C-Terminal residues\n') 			
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ('\naac_rt.py -i inputfile -o outputfile -m number1 -n number2\n')
            print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
            print('outputfile : is the file of feature vectors\n')
            print('number1 : number of N-Terminal residues\n')
            print('number2 : number of C-Terminal residues\n') 			
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-m", "--ofile"):
            m = int(sys.argv[6])
        elif opt in ("-n", "--ofile"):
            n = int(sys.argv[8])			
			
    aac_rt(sys.argv[2],sys.argv[4],int(sys.argv[6]),int(sys.argv[8]))

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])				
