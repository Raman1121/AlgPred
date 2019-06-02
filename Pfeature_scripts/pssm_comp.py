import sys, getopt
import numpy as np
import pandas as pd
import os
def pssm_comp(file,out):
   filename, file_ext = os.path.splitext(file)
   aa = list("ACDEFGHIKLMNPQRSTVWY")
   df=pd.read_csv(file, header=None)
   df.set_index(0,inplace=True)
   Matrix = [[0 for x in range(0,20)] for y in range(0,20)]
   j = 0
   df2 = []
   for i in aa:
      if i in df.index[:]:
         df1 = df.loc[i]
         df2 = (df1.sum(axis=0)/len(df))
         Matrix[j] =np.asarray(df2)
         j = j+1
      else:
         j = j+1
   f = open(out, 'w')
   sys.stdout = f
   for each in Matrix:
       for j in each:
           print("%.4f"%j,end=",")
   f.close()
def main(argv):
    global inputfile
    global outputfile
    inputfile = ''
    outputfile = ''
    #option = 1
    if len(argv[1:]) == 0:
        print ("\nUsage: pssm_comp.py -i inputfile -o outputfile\n")
        print('inputfile : PSSM file of peptide/protein sequences\n')
        print('outputfile : is the file of feature vectors\n')
        sys.exit()

    try:
      opts, args = getopt.getopt(argv,"i:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ("\nUsage: pssm_comp.py -i inputfile -o outputfile\n")
        print('inputfile : PSSM file of peptide/protein sequences\n')
        print('outputfile : is the file of feature vectors\n')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ('\npssm_comp.py -i inputfile -o outputfile\n')
            print('inputfile : PSSM file of peptide/protein sequences\n')
            print('outputfile : is the file of feature vectors\n')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    pssm_comp(sys.argv[2],sys.argv[4])

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])
