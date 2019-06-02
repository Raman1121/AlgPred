#!/usr/bin/python

import sys, getopt
import numpy as np
import pandas as pd
import os
def pssm_n1(file,output):
   filename,file_ext=os.path.splitext(file)
   df=pd.read_csv(file,header=None)
   df1 = df.iloc[:,0:21]
   def pssm(x):
       # that, if x is a string,
       if type(x) is str:
           # just returns it untouched
           return x
       # but, if not, return it multiplied by 100
       elif x:
           return (1/(1+(2.7182)**(-x)))
        # and leave everything else
       else:
           return
   df2 = df1.applymap(pssm)
   df2.to_csv(output, encoding='utf-8', index=False, header=False)		 
def main(argv):
    global inputfile
    global outputfile
    inputfile = ''
    outputfile = ''
    #option = 1
    if len(argv[1:]) == 0:
        print ("\nUsage: pssm_n1.py -i inputfile -o outputfile\n")
        print('inputfile : PSSM file of peptide/protein sequences\n')
        print('outputfile : is the file of feature vectors\n')
        sys.exit()

    try:
      opts, args = getopt.getopt(argv,"i:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ("\nUsage: pssm_n1.py -i inputfile -o outputfile\n")
        print('inputfile : PSSM file of peptide/protein sequences\n')
        print('outputfile : is the file of feature vectors\n')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ('\npssm_n1.py -i inputfile -o outputfile\n')
            print('inputfile : PSSM file of peptide/protein sequences\n')
            print('outputfile : is the file of feature vectors\n')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    pssm_n1(sys.argv[2],sys.argv[4])

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])
