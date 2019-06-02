import os
import sys
import numpy as np
import pandas as pd
import getopt

def nt(file,n):
    filename, file_extension = os.path.splitext(file)
    df1 = pd.read_csv(file, header = None)
    df2 = pd.DataFrame(df1[0].str.upper())
    df3 = []
    for i in range(0,len(df2)):
        df3.append(df2[0][i][0:n])
        df4 = pd.DataFrame(df3)
        #df4.to_csv(filename+".nt", index = None, header = False, encoding = 'utf-8')
    return df4
	
def bin_di_nt(file,outt,n,q):
    file1 = nt(file,n)
    filename, file_extension = os.path.splitext(file)
    #df2=pd.read_csv(file,header=None)
    #df = pd.DataFrame(df2[0].str.upper())
    df = file1
    mat3 = pd.read_csv("Data/bin_di.csv", header = None)
    mat3.set_index(0, inplace = True)
    mat3.index = pd.Series(mat3.index).replace(np.nan,'NA')
    f = open(outt+"_"+str(q), 'w')
    sys.stdout = f
    for i in range(0,len(df)):
        for j in range(0,(len(df[0][i])-(q+1))):
            temp1 = df[0][i][j:j+q+2:q+1]
            for each in (mat3.loc[temp1].values.ravel()):
                print("%.0f"%each, end = ",", flush = True)
        print("")
    f.truncate()
	
def main(argv):
    global inputfile
    global outputfile	
    inputfile = ''
    outputfile = ''	
    number = 1	
    if len(argv[1:]) == 0:
        print ("\nUsage: bin_di_nt.py -i inputfile -o outputfile -n number -q order\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')
        print('number1 : number of N-Terminal residues\n')	
        print('order : is order of dipeptide\n')			
        sys.exit()	
		
    try:
      opts, args = getopt.getopt(argv,"i:o:n:q:",["ifile=","ofile=","n=","q="])
    except getopt.GetoptError:
        print ("\nUsage: bin_di_nt.py -i inputfile -o outputfile -n number -q order\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')
        print('number1 : number of N-Terminal residues\n')	
        print('order : is order of dipeptide\n')		
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ('\nbin_di_nt.py -i inputfile -o outputfile -n number -q order\n')
            print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
            print('outputfile : is the file of feature vectors\n')
            print('number1 : number of N-Terminal residues\n')	
            print('order : is order of dipeptide\n')			
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-n", "--ofile"):
            n = int(sys.argv[6])	
        elif opt in ("-q", "--ofile"):
            q = int(sys.argv[8])			
			
    bin_di_nt(sys.argv[2],sys.argv[4],int(sys.argv[6]),int(sys.argv[8]))

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])	
