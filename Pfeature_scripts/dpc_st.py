import pandas as pd
import sys
import os
import numpy as np
import math
import getopt
from itertools import repeat
std = list("ACDEFGHIKLMNPQRSTVWY")
def dpc_st(file,output,n):
    filename,file_ext = os.path.splitext(file)
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
            k2.append((int(len(df2[0][w])/n)+r))
        for j in k2:
            df3 = df2[0][w][s:j+s]
            k1.append(df3)
            s = j+s
    f = open(output, 'w')
    sys.stdout = f
    for h in range(1,n+1):
        for e in std:
            for r in std:
                print(e+r+'s'+str(h), end=",")
    print("")
    for i in range(0,len(k1),n):
        k4 = k1[i:i+n]
        for j in k4:
            for k in std:
                for l in std:
                    count = 0
                    temp = k+l
                    for m3 in range(0,(len(j)-1)):
                        b = j[m3:m3+2]
                        if b == temp:
                            count += 1
                        composition = (count/(len(j)-1))*100
                    print("%.2f" %composition, end = ',')
        print("")
    f.truncate()
def main(argv):
    global inputfile
    global outputfile
    inputfile = ''
    outputfile = ''
    number = 1
    if len(argv[1:]) == 0:
        print ("\nUsage: dpc_st.py -i inputfile -o outputfile  -n number\n")
        print("-i: Input file in single line format\n-o: Output file\n-n: Number of splits")
        sys.exit()

    if len(argv[1:])<5:
        print ("\nUsage: dpc_st.py -i inputfile -o outputfile  -n number\n")
        print("-i: Input file in single line format\n-o: Output file\n-n: Number of splits")
        print("\nInputError: You have provided lesser number of arguments. \n")
        sys.exit()
    try:
      opts, args = getopt.getopt(argv,"i:o:n:",["ifile=","ofile=","n="])
    except getopt.GetoptError:
        print ("\nUsage: dpc_st.py -i inputfile -o outputfile -n number\n")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ('\ndpc_st.py -i inputfile -o outputfile -m number1 -n number\n')
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

    dpc_st(sys.argv[2],sys.argv[4],int(sys.argv[6]))

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])
