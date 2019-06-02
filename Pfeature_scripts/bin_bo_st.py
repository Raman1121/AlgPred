import sys
import os
import pandas as pd
from itertools import repeat
import getopt
def split(file,n):
    filename, file_extension = os.path.splitext(file)
    df1 = pd.read_csv(file, header = None)
    df2 = pd.DataFrame(df1[0].str.upper())
    k1 = []
    for w in range(0,len(df2)):
        s = 0
        k2 = []
        r = 0
        if len(df2[0][w])%n == 0:
            k2.extend(repeat(int(len(df2[0][w])/n),n))
        else:
            r = int(len(df2[0][w])%n)
            k2.extend(repeat(int(len(df2[0][w])/n),n-1))
            k2.append((int(len(df2[0][w])/n))+r)
        for j in k2:
            df3 = df2[0][w][s:j+s]
            k1.append(df3)
            s = j+s
    df4 = pd.DataFrame(k1)
    #df4.to_csv(filename+".split", index = None, header = False, encoding = 'utf-8')
    return df4
	
def bin_bo_st(file,output,n) :
    df = split(file,n)
    filename, file_extension = os.path.splitext(file)
    #df=pd.read_csv(file,header=None)
    ############binary matrix for atoms
    f = open('matrix_can_pat.out', 'w')
    sys.stdout = f
    print("-,=,c,b,")
    x = []
    for i in range(0,4) :
        x.append([])
        for j in range(0,4) :
            if i == j :
                x[i].append(1)
            else :
                x[i].append(0)
            
            print(x[i][j], end=",") 
        print("") 
    f.truncate() 

##############associate binary values to bonds   
    mat = pd.read_csv("matrix_can_pat.out")
    mat1 = mat.iloc[:,:-1]
    mat2 = mat1.transpose()
    df1 = pd.read_csv("Data/can_pat.csv")
    zz = []
    kk = pd.DataFrame()
    
    for i in range(0,len(df1)) :
        zz.append([])
        for j in range(0,len(df1.iloc[:,1][i])) :
            temp = str(df1.iloc[:,1][i][j])
            zz[i].append(mat2.loc[temp])

    f1 = open('bin_bond', 'w')
    sys.stdout = f1
    for i in range(0,len(zz)) :
        for row in zz[i]:
            print(",".join(map(str,row)), end=",")
        print("")
    
    f1.truncate() 

    with open('bin_bond', 'r') as f:
        g = list(f)
        
    for i in range(0,len(g)) :
        g[i] = g[i].replace(",\n","")
        
    df1["bin"] = g    

    xx=[]
    jj = 0
    for i in range(0,len(df)) :
        xx.append([])
        while jj < len(df[0][i]) :
            temp=df[0][i][jj]
            for k in range(0,len(df1)) :
                if temp == df1.iloc[k,0][0] :
                    xx[i].append(df1.iloc[k,2])
            jj += 1
        jj = 0 

    f2 = open(output, 'w')
    sys.stdout = f2
    for i in range(0,len(xx),n) :
        for row in xx[i:i+n]:
            print(",".join(map(str,row)), end=",")
        print("")
    f2.truncate()  
    os.remove("matrix_can_pat.out")
    os.remove('bin_bond')
def main(argv):
    global inputfile
    global outputfile
    inputfile = ''
    outputfile = ''
    number = 1
    if len(argv[1:]) == 0:
        print ("\nUsage: bin_bo_st.py -i inputfile -o outputfile  -n number\n")
        print("-i: Input file in single line format\n-o: Output file\n-n: Number of splits")
        sys.exit()

    if len(argv[1:])<5:
        print ("\nUsage: bin_bo_st.py -i inputfile -o outputfile  -n number\n")
        print("-i: Input file in single line format\n-o: Output file\n-n: Number of splits")
        print("\nInputError: You have provided lesser number of arguments. \n")
        sys.exit()
    try:
      opts, args = getopt.getopt(argv,"i:o:n:",["ifile=","ofile=","n="])
    except getopt.GetoptError:
        print ("\nUsage: bin_bo_st.py -i inputfile -o outputfile -n number\n")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ('\nbin_bo_st.py -i inputfile -o outputfile -m number1 -n number\n')
            print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n')
            print('outputfile : is the file of feature vectors\n')
            print('number1 : Number of splits\n')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-n", "-n"):
            n = int(sys.argv[6])

    bin_bo_st(sys.argv[2],sys.argv[4],int(sys.argv[6]))

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])
