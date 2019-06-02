import sys
import pandas as pd
import os
import getopt
std = list('ACDEFGHIKLMNPQRSTVWY')
from itertools import repeat
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
    return df4
def rri_st(file,output,n):
    filename, file_extension = os.path.splitext(file)
    file1 = split(file,n)
    data = file1
    count = 0
    cc = []
    i = 0
    x = 0
    temp = pd.DataFrame()
    f = open(filename+".rri_split",'w')
    sys.stdout = f
    print("A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y,")
    for q in range(0,len(data)):
        mm = data[0][q]
        while i < len(std):
            cc = []
            for j in mm:
                if j == std[i]:
                    count += 1
                    cc.append(count)
                else:
                    count = 0
            while x < len(cc) :
                if x+1 < len(cc) :
                    if cc[x]!=cc[x+1] :
                        if cc[x] < cc[x+1] :
                            cc[x]=0
                x += 1
            cc1 = [e for e in cc if e!= 0]
            cc = [e*e for e in cc if e != 0]
            zz= sum(cc)
            zz1 = sum(cc1)
            if zz1 != 0:
                zz2 = zz/zz1
            else:
                zz2 = 0
            print("%.2f"%zz2,end=',')
            i += 1
        i = 0
        print(" ")
    f.truncate()
    df31 = pd.read_csv(filename+".rri_split")
    df3 = df31.iloc[:,:-1]
    header = []
    for h in range(1,n+1):
        for e in std:
            header.append(e+"_s"+str(h))
    bb = []
    for i in range(0,len(df3),n):
        aa = []
        for j in range(n):
            aa.extend(df3.loc[i+j])
        bb.append(aa)
    ww = pd.DataFrame(bb)
    ww.columns = header
    ww.to_csv(output, index = None)
    os.remove(filename+".rri_split")
def main(argv):
    global inputfile
    global outputfile
    inputfile = ''
    outputfile = ''
    number = 1
    if len(argv[1:]) == 0:
        print ("\nUsage: rri_st.py -i inputfile -o outputfile  -n number\n")
        print("-i: Input file in single line format\n-o: Output file\n-n: Number of splits")
        sys.exit()

    if len(argv[1:])<5:
        print ("\nUsage: rri_st.py -i inputfile -o outputfile  -n number\n")
        print("-i: Input file in single line format\n-o: Output file\n-n: Number of splits")
        print("\nInputError: You have provided lesser number of arguments. \n")
        sys.exit()
    try:
      opts, args = getopt.getopt(argv,"i:o:n:",["ifile=","ofile=","n="])
    except getopt.GetoptError:
        print ("\nUsage: rri_st.py -i inputfile -o outputfile -n number\n")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ('\nrri_st.py -i inputfile -o outputfile -m number1 -n number\n')
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

    rri_st(sys.argv[2],sys.argv[4],int(sys.argv[6]))

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])
