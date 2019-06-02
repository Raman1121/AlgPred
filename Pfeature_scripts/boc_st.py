import os
import sys
import pandas as pd
import math
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
def boc_st(file,output,n) :
    tota = []
    hy = []
    Si = []
    Du = []
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    bb = pd.DataFrame()
    filename, file_extension = os.path.splitext(file)
    #df = pd.read_csv(file, header = None)
    df = split(file,n)	
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
                    D = D + bonds.iloc[:,4][k]
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
    header = []
    header1 = ('total','hydrogen','single','double')
    for i in range(1,n+1):
        for j in header1:
            header.append(j+"_s"+str(i))
    qq = []
    for i in range(0,len(bb),n):
        aa = []
        for j in range(n):
            aa.extend(bb.loc[i+j])
        qq.append(aa)
    zz = pd.DataFrame(qq)
    zz.columns = header
    zz.to_csv(output, index=None)
def main(argv):
    global inputfile
    global outputfile
    inputfile = ''
    outputfile = ''
    number = 1
    if len(argv[1:]) == 0:
        print ("\nUsage: boc_st.py -i inputfile -o outputfile  -n number\n")
        print("-i: Input file in single line format\n-o: Output file\n-n: Number of splits")
        sys.exit()

    if len(argv[1:])<5:
        print ("\nUsage: boc_st.py -i inputfile -o outputfile  -n number\n")
        print("-i: Input file in single line format\n-o: Output file\n-n: Number of splits")
        print("\nInputError: You have provided lesser number of arguments. \n")
        sys.exit()
    try:
      opts, args = getopt.getopt(argv,"i:o:n:",["ifile=","ofile=","n="])
    except getopt.GetoptError:
        print ("\nUsage: boc_st.py -i inputfile -o outputfile -n number\n")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ('\nboc_st.py -i inputfile -o outputfile -m number1 -n number\n')
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

    boc_st(sys.argv[2],sys.argv[4],int(sys.argv[6]))

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])
