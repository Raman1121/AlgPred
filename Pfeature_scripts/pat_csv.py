import pandas as pd
import os
import sys
import getopt
def pat_csv(file,n,out):
    filename,file_ext = os.path.splitext(file)
    df3 = pd.read_csv(file, header=None)
    ss = []
    f = open(out, 'w')
    sys.stdout = f
    for i in range(0,len(df3)):
        ss.append([i])
        for j in range(0,(len(df3.loc[i])-n+1)):
            ss[i].append(df3.loc[i][j:j+n].values)
    for i in range(0,len(ss)) :
        for j in range(1,len(ss[i])) :
            for each in ss[i][j][0:len(ss[i][j])] :
                print(each, end=",")
        print("")
    f.truncate()
def main(argv):
    global inputfile
    global outputfile
    inputfile = ''
    outputfile = ''
    window_size=1
    #option = 1
    if len(argv[1:]) == 0:
        print ("\nUsage: pat_csv.py -i inputfile -w window_size -o outputfile\n")
        print('inputfile : file in the .csv format\n')
        print('window_size : size of the window\n')
        print('outputfile : is the file of feature vectors\n')
        sys.exit()

    try:
      opts, args = getopt.getopt(argv,"i:w:o:",["ifile=","wsize=","ofile="])
    except getopt.GetoptError:
        print ("\nUsage: pat_csv.py -i inputfile -w window_size -o outputfile\n")
        print('inputfile : file in the .csv format\n')
        print('window_size : size of the window\n')
        print('outputfile : is the file of feature vectors\n')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ('\npat_csv.py -i inputfile -w window_size -o outputfile\n')
            print('inputfile : file in the .csv format\n')
            print('window_size : size of the window\n')
            print('outputfile : is the file of feature vectors\n')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-w", "--wsize"):
            window_size = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    pat_csv(sys.argv[2],int(sys.argv[4]),sys.argv[6])

if __name__ == '__main__':
    #print(sys.argv)
    main(sys.argv[1:])
