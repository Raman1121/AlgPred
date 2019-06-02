import os
import sys
import numpy as np
import pandas as pd
import getopt
def bin_di_wp(file,outt,q):
    filename, file_extension = os.path.splitext(file)
    df2=pd.read_csv(file,header=None)
    df = pd.DataFrame(df2[0].str.upper())
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
        print ("\nUsage: bin_di_wp.py -i inputfile -o outputfile -q order\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')
        print('order : is order of dipeptide\n')		
        sys.exit()	
		
    try:
      opts, args = getopt.getopt(argv,"i:o:q:",["ifile=","ofile=","q="])
    except getopt.GetoptError:
        print ("\nUsage: bin_di_wp.py -i inputfile -o outputfile -q order\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')
        print('order : is order of dipeptide\n')		
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ('\nbin_di_wp.py -i inputfile -o outputfile -q order\n')
            print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
            print('outputfile : is the file of feature vectors\n')	
            print('order : is order of dipeptide\n')			
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-q", "--q"):
            q = int(sys.argv[6])	
			
			
    bin_di_wp(sys.argv[2],sys.argv[4],int(sys.argv[6]))

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])	
