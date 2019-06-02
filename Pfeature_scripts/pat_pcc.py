#!/usr/bin/env python

'''

Function to calculate fraction of each physico-chemical property present in sequences (separated by comma)

This function takes 5 command line arguments:


Argv[1]: comma separated sequences (no spaces and only comma separated)

Argv[2]: Mode to be chosen
        
        Valid input is a string type belonging to 
        
        'all'    for considering the entire sequence
        'NT'     for considering first n residues of each sequence from N terminal
        'CT'     for considering last n residues of each sequence from C terminal
        'rest'   for considering a segment of each sequence from mth to nth index (both inclusive)
        
Argv[3]: m
        For 'rest'; start index
        For other; m=n

Argv[4]: n,
        For 'rest'; end index
        For other; n is the number of residues from N or C terminal as applicable
        
Argv[5]: OUTPUT file


SPECIAL NOTE FOR PASSING COMMAND LINE ARGUMENTS---


'all' mode

    file,'all',0,0,out

'NT' mode

    file,'NT',n,n,out

'CT' mode

    file,'CT',n,n,out

'rest' mode

    file,'rest',m,n,out
        

'''

# Secondary functions, move to next section

#Single function to calculate 30 physico che
import sys
import pandas as pd
import numpy as np
import csv
import getopt

# Generating patterns

def pat_str(file,w):
    if w%2==0:
        raise Exception('window size should be an odd number. The value of window size provided: {}'.format(w))
        sys.exit()
    df1 = pd.read_csv(file, header =None)
    ext = str('X')*int((w-1)/2)
    aa = []
    for i in range(0,len(df1)):
        new_str = ext+df1[0][i]+ext
        aa.append(new_str)
    df2 = pd.DataFrame(aa)
    bb = []
    for j in range(0,len(df2)):
        for k in range(0,len(df2[0][j])):
            cc = df2[0][j][k:k+w]
            if len(cc) == w:
                bb.append(cc)
#         df3 = pd.DataFrame(bb)
    return pd.DataFrame(bb)

#Finding physico-chemical property of a vector of polypeptides


PCP= pd.read_csv('Data/PhysicoChemical_X.csv', header=None) #Our reference table for properties

headers = ['Positively charged',
'Negatively charged',
'Neutral charged',
'Polarity',
'Non polarity',
'Aliphaticity',
'Cyclic',
'Aromaticity',
'Acidicity',
'Basicity',
'Neutral (ph)',
'Hydrophobicity',
'Hydrophilicity',
'Neutral',
'Hydroxylic',
'Sulphur content',
'Secondary Structure(Helix)',
'Secondary Structure(Strands)',
'Secondary Structure(Coil)',
'Solvent Accessibilty (Buried)',
'Solvent Accesibilty(Exposed)',
'Solvent Accesibilty(Intermediate)',
'Tiny',
'Small',
'Large',
'z1',
'z2',
'z3',
'z4',
'z5'];


def encode(peptide):
    #letter = {'A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y'};
    l=len(peptide);
    encoded=np.zeros(l);
    for i in range(l):
        if(peptide[i]=='A'):
            encoded[i] = 0;
        elif(peptide[i]=='C'):
            encoded[i] = 1;
        elif(peptide[i]=='D'):
            encoded[i] = 2;
        elif(peptide[i]=='E'):
            encoded[i] = 3;
        elif(peptide[i]=='F'):
            encoded[i] = 4;
        elif(peptide[i]=='G'):
            encoded[i] = 5;
        elif(peptide[i]=='H'):
            encoded[i] = 6;
        elif(peptide[i]=='I'):
            encoded[i] = 7;
        elif(peptide[i]=='K'):
            encoded[i] = 8;
        elif(peptide[i]=='L'):
            encoded[i] = 9;
        elif(peptide[i]=='M'):
            encoded[i] = 10;
        elif(peptide[i]=='N'):
            encoded[i] = 11;
        elif(peptide[i]=='P'):
            encoded[i] = 12;
        elif(peptide[i]=='Q'):
            encoded[i] = 13;
        elif(peptide[i]=='R'):
            encoded[i] = 14;
        elif(peptide[i]=='S'):
            encoded[i] = 15;
        elif(peptide[i]=='T'):
            encoded[i] = 16;
        elif(peptide[i]=='V'):
            encoded[i] = 17;
        elif(peptide[i]=='W'):
            encoded[i] = 18;
        elif(peptide[i]=='Y'):
            encoded[i] = 19;
        elif(peptide[i]=='X'):
            encoded[i] = 20;
        else:
            print('Wrong residue!');
    return encoded;


        
def lookup(peptide,featureNum):
    l=len(peptide);
    peptide = list(peptide);
    out=np.zeros(l);
    peptide_num = encode(peptide);
    
    for i in range(l):
        out[i] = PCP[peptide_num[i]][featureNum];
    return sum(out);


def pcp(file,outt):
    if(type(file) == str):
        seq = pd.read_csv(file,header=None, sep=',');
        seq=seq.T
        seq[0].values.tolist()
        seq=seq[0];
    else:
        seq  = file;
    
    l = len(seq);

    rows = PCP.shape[0]; # Number of features in our reference table
    col = 20 ; # Denotes the 20 amino acids
    
    seq=[seq[0][i].upper() for i in range(l)]
    sequenceFeature = [];
    sequenceFeature.append(headers); #To put property name in output csv
    
    for i in range(l): # Loop to iterate over each sequence
        nfeatures = rows;
        sequenceFeatureTemp = [];
        for j in range(nfeatures): #Loop to iterate over each feature
            featureVal = lookup(seq[i],j)   
            if(len(seq[i])!=0):
                sequenceFeatureTemp.append(round(featureVal/len(seq[i]),3));
            else:
                sequenceFeatureTemp.append('NaN')
            
        sequenceFeature.append(sequenceFeatureTemp);
        
    out = pd.DataFrame(sequenceFeature);
    
    file = open(outt,'w')
    with file:
        writer = csv.writer(file);
        writer.writerows(sequenceFeature);
    return sequenceFeature;


# In[68]:


'''

Function Name: pat_pcc
Description: Gives 30 physico-chemical properties of a sequence

Function prototype: pat_pcc(file,w,outt)

Input:
@file: an input csv file with multiple sequences
@mode(optional, default = 'all'):
    Values possible: 
        1) (default)'all' : to get features of entire protein
        2) 'NT' : to get the features of first n N-Terminal residues
        3) 'CT' : to get the features of last n C-Terminal residues
        4) 'rest' : to get the features of a sub-sequence from mth position to nth position(both inclusive)
@m(optional(mandatory if 'rest' is chosen, default=0): m is the start position of residue 
@n(optional, default = '0'): n is the number of residues you want from desired terminal or end point (if 'rest' is chosen)


Output: 
A matrix (csv file) of dimension (m x 30) containing sequences as rows and their 30 physico-chemical properties as columns
where m = number of sequences (each sequence separated by comma) 

'''


'''

Function Name: pat_pcc
Description: Gives 30 physico-chemical properties of a sequence

Function prototype: pat_pcc(file,w,outt)

Input:
@file: an input csv file with multiple sequences
@mode(optional, default = 'all'):
    Values possible: 
        1) (default)'all' : to get features of entire protein
        2) 'NT' : to get the features of first n N-Terminal residues
        3) 'CT' : to get the features of last n C-Terminal residues
        4) 'rest' : to get the features of a sub-sequence from mth position to nth position(both inclusive)
@m(optional(mandatory if 'rest' is chosen, default=0): m is the start position of residue 
@n(optional, default = '0'): n is the number of residues you want from desired terminal or end point (if 'rest' is chosen)


Output: 
A matrix (csv file) of dimension (m x 30) containing sequences as rows and their 30 physico-chemical properties as columns
where m = number of sequences (each sequence separated by comma) 

'''


def pat_pcc(file,w,outt):
    m = 0
    n = 0
    mode = 'all'
    file = pat_str(file,w)
    if(type(file) == str):
        seq = pd.read_csv(file,header=None);
        #seq=seq.T
        seq[0].values.tolist()
        seq=seq[0];
    #elif(type(file)==str && len(file))
    else:
        seq  = file;
    l = len(seq);

    newseq = [""]*l; # To store the trimmed sequence
    #print('Original Sequence');
    #print(seq)
    
    
    for i in range(0,l):
    
        #if(n<len(seq[i])):
        l = len(seq[0][i]);
        
        if(mode=='NT'):
            n=m;
            if(n!=0):
                newseq[i] = seq[i][0:n];

            elif(n>l):
                print('Warning! Sequence',i,"'s size is less than n. The output table would have NaN for this sequence");


            else:
                print('Value of n is mandatory, it cannot be 0')
                break;

        elif(mode=='CT'):
            n=m;
            if(n!=0):
                newseq[i] = seq[i][(len(seq[i])-n):]
                
            elif(n>l):
                print('WARNING: Sequence',i+1,"'s size is less than the value of n given. The output table would have NaN for this sequence");


            else:
                print('Value of n is mandatory, it cannot be 0')
                break;

        elif(mode=='all'):
            newseq = seq;

        elif(mode=='rest'):
            if(m==0):
                print('Kindly provide start index for rest, it cannot be 0');
                break;

            else:
                if(n<=len(seq[i])):
                    newseq[i] = seq[i][m:(len(seq[i])-n)]
                '''elif(n>len(seq[i])):
                    newseq[i] = seq[i][m-1:len(seq[i])]
                    print('WARNING: Since input value of n for sequence',i+1,'is greater than length of the protein, entire sequence starting from m has been considered')'''

        else:
            print("Wrong Mode. Enter 'NT', 'CT','all' or 'rest'");        
        
    
    output = pcp(newseq,outt);
    return output

def main(argv):
    global inputfile
    global outputfile
    inputfile = ''
    outputfile = ''
    window_size = 3
    if len(argv[1:]) == 0:
        print ("Usage:python pat_pcc.py -i inputFile -w window size -o outputFile\n")
        print ('-i\tInputFile\n-w\tWindow size to create motifs\n-o\tOutput file\n')
        sys.exit()

    if len(argv[1:])<5:
        print ("Usage:python pat_pcc.py -i inputFile -w window size -o outputFile\n")
        print ('-i\tInputFile\n-w\tWindow size to create motifs\n-o\tOutput file\n')        
        print("\nInputError: You have provided lesser number of arguments. \n")
        sys.exit()
    try:
      opts, args = getopt.getopt(argv,"i:w:o:",["ifile=","w=","ofile="])
    except getopt.GetoptError:
        print ("\nUsage: pat_pcc.py -i inputfile -w window_size  -o outputfile\n")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ("Usage:python pat_pcc.py -i inputFile -w window size -o outputFile\n")
            print ('-i\tInputFile\n-w\tWindow size to create motifs\n-o\tOutput file\n')            
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-w", "-w"):
            w = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    pat_pcc(sys.argv[2],int(sys.argv[4]),sys.argv[6])

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])