import sys, getopt
#from Bio import SeqIO

def pat_str(inputfile,windowfile,extensionfile,outputfile):
  with open(inputfile,'r') as f:
    g = list(f)
    #temp = f.readlines()

#  print (g)

  orig_stdout = sys.stdout
  n = open(outputfile,'w')
  sys.stdout = n



  aa =('A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y')
#  print("Program to create motifs by sliding window\n")
#  print("A , C , D , E , F , G , H , I , K , L , M , N , P , Q , R , S , T , V , W , Y\n")

  k= (int(windowfile)-1)/2
  new_str = "X" * int(k)


  for i in g:
#        print("Original sequence: ",i)
#        print (new_str)
#        a = i.readlines()
#        print(a)
#        print (a[0])
#        b = a
        c = i.replace('\n','')
#        c.upper()
        if (extensionfile == 'y'):
#
                c =new_str+c+new_str
        for j in range(0,len(c)):
            d = c[j:j+int(windowfile)]
            if len(d)==int(windowfile):
#                print("sequence number: ",j+1)
                print(d.upper())
        print("")
def main(argv):
    global inputfile
    global outputfile
    inputfile = ''
    outputfile = ''
    extension = ''
    window_size = 3
    if len(argv[1:]) == 0:
        print ("Usage:python pat_str.py -i inputFile -w window size -x extension -o outputFile\n")
        print ('-i\tInputFile\n-w\tWindow size to create motifs\n-x\t[y|n] extension of X needed or not\n-o\tOutput Motif file\n') 
        sys.exit()

    if len(argv[1:])<7:
        print ("Usage:python pat_str.py -i inputFile -w window size -x extension -o outputFile\n")
        print ('-i\tInputFile\n-w\tWindow size to create motifs\n-x\t[y|n] extension of X needed or not\n-o\tOutput Motif file\n')        
        print("\nInputError: You have provided lesser number of arguments. \n")
        sys.exit()
    try:
      opts, args = getopt.getopt(argv,"i:w:x:o:",["ifile=","w=","x=","ofile="])
    except getopt.GetoptError:
        print ("\nUsage: pat_str.py -i inputfile -w window_size  -n number -o outputfile\n")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ("Usage:python pat_str.py -i inputFile -w window size -x extension -o outputFile\n")
            print ('-i\tInputFile\n-w\tWindow size to create motifs\n-x\t[y|n] extension of X needed or not\n-o\tOutput Motif file\n')            
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-w", "-w"):
            w = int(sys.argv[4])
        elif opt in ("-x", "-x"):
            x = sys.argv[6]
        elif opt in ("-o", "--ofile"):
            outputfile = sys.argv[8]

    pat_str(sys.argv[2],int(sys.argv[4]),sys.argv[6],sys.argv[8])

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])
