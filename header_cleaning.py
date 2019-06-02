## Python Script to separate and clean the header file generated in required format.

import sys
import getopt
import csv
import numpy as np
import pandas as pd

def clean(filename):
    file = open(filename, "r")
    label_number = []
    csv_filename = filename.split('.')[0]+'.csv'
    print(csv_filename)
    path = 'header_files/'

    for line in file:
        #print(line)
        label = line.split('_')[0]
        label_final = label.split('>')[1]
        #print(label_final)
        if label_final == 'N':
            label_number.append(0)
        elif label_final == 'P':
            label_number.append(1)

        #print(label_final)
        
        '''with open(csv_filename, 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(label_number)

        csvfile.close()'''
    print(len(label_number))
    pd.DataFrame(np.array(label_number)).to_csv(path+csv_filename, header=None, index=False)

    


def main(argv):

    global inputfile
    inputfile = ''

    if len(argv[1:]) == 0:
        print ("\nUsage: header_cleaning.py -i inputfile \n")
        print('inputfile : is the file of headers\n')
        sys.exit()

    try:
        opts, args = getopt.getopt(argv, "i")
    except getopt.GetoptError:
        print ("\nUsage: header_cleaning.py -i inputfile \n")
        print('inputfile : is the file of headers\n')	
        sys.exit(2)

    for opt, arg in opts:
        if opt == '--help' or opt == '--h':
            print ("\nUsage: header_cleaning.py -i inputfile \n")
            print('inputfile : is the file of headers\n')	
            sys.exit()
        elif opt in ("-i", "--infile"):
            inputfile = arg

    clean(sys.argv[2])

if __name__ == "__main__":
    main(sys.argv[1])

    

