import pandas as pd
import os
import math
import sys
import getopt
import glob
import time
import numpy as np
from time import sleep
data1 = pd.read_csv("Data/data", sep = "\t")
def ct(file,n):
    filename, file_extension = os.path.splitext(file)
    df1 = pd.read_csv(file, header = None)
    df2 = pd.DataFrame(df1[0].str.upper())
    df3 = []
    for i in range(0,len(df2)):
        df3.append(df2[0][i][-n:])
        df4 = pd.DataFrame(df3)
        #df4.to_csv(filename+".ct", index = None, header = False, encoding = 'utf-8')
    return df4

std = list('ACDEFGHIKLMNPQRSTVWY')
def apaac_1_ct(file,lambdaval,v,w):
    df1 = ct(file,v)
    filename, file_extension = os.path.splitext(file)
    #df = pd.read_csv(file, header = None)
    #df1 = pd.DataFrame(df[0].str.upper())
    dd = []
    cc = []
    pseudo = []
    aa = {}
    for i in range(len(std)):
        aa[std[i]] = i
    for i in range(0,3):
        mean = sum(data1.iloc[i][1:])/20
        rr = math.sqrt(sum([(p-mean)**2 for p in data1.iloc[i][1:]])/20)
        dd.append([(p-mean)/rr for p in data1.iloc[i][1:]])
        zz = pd.DataFrame(dd)
        #print(zz)
    head = []
    for n in range(1, lambdaval + 1):
        for e in ('hydrphobicity','hydrophilicity','sidechainmass'):
            head.append('lam_' + str(n)+"_"+str(e))
    pp = pd.DataFrame()
    ee = []
    tt = []
    for k in range(0,len(df1)):
        cc = []
        for n in range(1,lambdaval+1):
            for b in range(0,len(zz)):
                cc.append(sum([zz.loc[b][aa[df1[0][k][p]]] * zz.loc[b][aa[df1[0][k][p + n]]] for p in range(len(df1[0][k]) - n)]) / (len(df1[0][k]) - n))
                qq = pd.DataFrame(cc)
        tt.append(cc)
        np.savetxt(filename+".more", tt, delimiter=",")
        pseudo = [(w * p) / (1 + w * sum(cc)) for p in cc]
        ee.append(pseudo)
        ii = round(pd.DataFrame(ee, columns = head),4)
        ii.to_csv(filename+".plam",index = None)
def aac_comp(file,v,w):
    df = ct(file,v)
    filename, file_extension = os.path.splitext(file)
    df31 = pd.read_csv(filename+".more", header=None)
    df31["sum"] = df31.sum(axis=1)
    f = open(filename+".aac", 'w')
    sys.stdout = f
    zz = df.iloc[:,0]
    print("A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y,")
    c = 0
    for j in zz:
        for i in std:
            count = 0
            for k in j:
                temp1 = k
                if temp1 == i:
                    count += 1
                composition = (count/(1+(w*df31['sum'][c])))
            print("%.4f"%composition, end = ",")
        print("")
        c = c+1
    f.truncate()
def apaac_ct(file,outt,lambdaval,v,w):
    filename, file_extension = os.path.splitext(file)
    apaac_1_ct(file,lambdaval,v,w)
    aac_comp(file,v,w)
    data1 = pd.read_csv(filename+".aac")
    data2 = pd.read_csv(filename+".plam")
    data3 = pd.concat([data1.iloc[:,:-1],data2], axis = 1).reset_index(drop=True)
    data3.to_csv(outt, index = None)
    os.remove(filename+".aac")
    os.remove(filename+".plam")
    os.remove(filename+".more")
def main(argv):
    global inputfile
    global outputfile	
    inputfile = ''
    outputfile = ''	
    number = 1	
    if len(argv[1:]) == 0:
        print ("\nUsage: apaac_ct.py -i inputfile -o outputfile -l lamda -n number -w weight\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')
        print('lamda : lamda value (gap)\n')	
        print('number : number of C-Terminal residues\n')		
        print('weight : assign weight to the sequence\n')		
			
        sys.exit()	
		
    try:
      opts, args = getopt.getopt(argv,"i:o:l:n:w:",["ifile=","ofile=","l=","n=","w="])
    except getopt.GetoptError:
        print ("\nUsage: apaac_ct.py -i inputfile -o outputfile -l lamda -n number -w weight\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')
        print('lamda : lamda value (gap)\n')	
        print('number : number of C-Terminal residues\n')		
        print('weight : assign weight to the sequence\n')		
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ('\napaac_ct.py -i inputfile -o outputfile -l lamda -n number -w weight\n')
            print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
            print('outputfile : is the file of feature vectors\n')
            print('lamda : lamda value (gap)\n')	
            print('number : number of C-Terminal residues\n')		
            print('weight : assign weight to the sequence\n')
			
            sys.exit()
			
			
    apaac_ct(sys.argv[2],sys.argv[4],int(sys.argv[6]),int(sys.argv[8]),float(sys.argv[10]))
    #filename, file_extension = os.path.splitext(sys.argv[2])	


if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])					
				

