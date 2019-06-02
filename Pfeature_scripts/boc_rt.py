import os
import sys
import pandas as pd
import math
import getopt
#from  more_itertools import unique_everseen
def rest(file,n,c):
    filename, file_extension = os.path.splitext(file)
    df1 = pd.read_csv(file, header = None)
    df2 = pd.DataFrame(df1[0].str.upper())
    df3 = []
    for i in range(0,len(df2)):
        df3.append(df2[0][i][n:-c])
        df4 = pd.DataFrame(df3)
        #df4.to_csv(filename+".rest", index = None, header = False, encoding = 'utf-8') 
    return df4
def boc_rt(file,outt,n,c) :
    tota = []
    hy = []
    Si = []
    Du = []
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    bb = pd.DataFrame()
    df = rest(file,n,c)
    #filename, file_extension = os.path.splitext(file)
    #df = pd.read_csv(file, header = None)
    	
    bonds=pd.read_csv("Data/bonds.csv")
    for i in range(0,len(df)) :
        tot = 0
        h = 0
        S = 0
        D = 0
        tota.append([i])
        hy.append([i])
        Si.append([i])
        Du.append([i])
        for j in range(0,len(df[0][i])) :
            temp = df[0][i][j]
            for k in range(0,len(bonds)) :
                if bonds.iloc[:,0][k] == temp :
                    tot = tot + bonds.iloc[:,1][k]
                    h = h + bonds.iloc[:,2][k]
                    S = S + bonds.iloc[:,3][k]
                    D = D + bonds.iloc[:,3][k]
        tota[i].append(tot)
        hy[i].append(h)
        Si[i].append(S)
        Du[i].append(D)
    for m in range(0,len(df)) :
        b1.append(tota[m][1])
        b2.append(hy[m][1])
        b3.append(Si[m][1])
        b4.append(Du[m][1])
    
    bb["total"] = b1 
    bb["hydrogen"] = b2
    bb["single"] = b3
    bb["double"] = b4 
    
    bb.to_csv(outt,index=None)
	
def main(argv):
    global inputfile
    global outputfile	
    inputfile = ''
    outputfile = ''	
    number1 = 1
    number2 = 1	
    if len(argv[1:]) == 0:
        print ("\nUsage: boc_rt.py -i inputfile -o outputfile -m number1 -n number2\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')
        print('number1 : number of N-Terminal residues\n')
        print('number2 : number of C-Terminal residues\n') 			
        sys.exit()	
		
    try:
      opts, args = getopt.getopt(argv,"i:o:m:n:",["ifile=","ofile=","m=","n="])
    except getopt.GetoptError:
        print ("\nUsage: boc_rt.py -i inputfile -o outputfile -m number1 -n number2\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')
        print('number1 : number of N-Terminal residues\n')
        print('number2 : number of C-Terminal residues\n') 			
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ('\nboc_rt.py -i inputfile -o outputfile -m number1 -n number2\n')
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
			
    boc_rt(sys.argv[2],sys.argv[4],int(sys.argv[6]),int(sys.argv[8]))

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])		

	
