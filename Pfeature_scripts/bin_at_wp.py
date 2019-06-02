import sys
import os
import pandas as pd
import getopt
def bin_at_wp(file,outt) :
    filename, file_extension = os.path.splitext(file)
    df=pd.read_csv(file,header=None)
    ############binary matrix for atoms
    f = open('matrix_atom.out', 'w')
    sys.stdout = f
    print("C,H,N,O,S,")
    x = []
    for i in range(0,5) :
        x.append([])
        for j in range(0,5) :
            if i == j :
                x[i].append(1)
            else :
                x[i].append(0)
            
            print(x[i][j], end=",") 
        print("") 
    f.close() 
##############associate binary values to atoms    
    mat = pd.read_csv("matrix_atom.out")
    mat1 = mat.iloc[:,:-1]
    mat2 = mat1.transpose()
    df1 = pd.read_csv("Data/atom.csv",header=None)
    zz = []
    kk = pd.DataFrame()
    df1 = pd.read_csv("Data/atom.csv",header=None)
    for i in range(0,len(df1)) :
        zz.append([])
        for j in range(0,len(df1[1][i])) :
            temp = df1[1][i][j]
            zz[i].append(mat2.loc[temp])
            
    f1 = open('bin_atom', 'w')
    sys.stdout = f1
    for i in range(0,len(zz)) :
        for row in zz[i]:
            print(",".join(map(str,row)), end=",")
        print("")
    
    f1.close()    
    
    with open('bin_atom', 'r') as f:
        g = list(f)
        
    for i in range(0,len(g)) :
        g[i] = g[i].replace(",\n","")    
        
    df1["bin"]=g
    
    #########binary atom values for given file
    xx=[]
    jj = 0
    for i in range(0,len(df)) :
        xx.append([])
        while jj < len(df[0][i]) :
            temp=df[0][i][jj]
            for k in range(0,len(df1)) :
                if temp == df1[0][k][0] :
                    xx[i].append(df1.iloc[k,2])
            jj += 1
        jj = 0 
        
        
    f2 = open(outt, 'w')
    sys.stdout = f2
    for i in range(0,len(xx)) :
        for row in xx[i]:
            print("".join(map(str,row)), end=",")
        print("")
    f2.truncate()   
	
    os.remove("matrix_atom.out")
    os.remove("bin_atom") 	
	
def main(argv):
    global inputfile
    global outputfile	
    inputfile = ''
    outputfile = ''	
    #option = 1	
    if len(argv[1:]) == 0:
        print ("\nUsage: bin_at_wp.py -i inputfile -o outputfile\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')		
        sys.exit()	
		
    try:
      opts, args = getopt.getopt(argv,"i:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ("\nUsage: bin_at_wp.py -i inputfile -o outputfile\n")
        print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
        print('outputfile : is the file of feature vectors\n')		
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ('\nbin_at_wp.py -i inputfile -o outputfile\n')
            print('inputfile : file of peptide/protein sequences for which descriptors need to be generated\n') 
            print('outputfile : is the file of feature vectors\n')			
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
			
    bin_at_wp(sys.argv[2],sys.argv[4])

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])		
