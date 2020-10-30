#!/anaconda3/bin/python
# -*- coding: utf-8 -*-

# Written by: Nuha Mahmood
# Description: A command line tool to count + output the number of rows per file in a given directory. 
# Last modified: 10-30-2020

import csv
import sys
import os
import argparse



# Help: Command line argument descriptions.

parser = argparse.ArgumentParser(
    description = 
    '''A simple command-line tool to count the rows of each file in a given directory.''')

# Positional arguments

parser.add_argument('filetype', type = str, choices = ['csv', 'txt', 'tsv'], help = "Specify the file type you want to evaluate.") # There are lots of hidden/unopenable files in these directories, so I'm limiting row counts to one of these specified file types for now. 

parser.add_argument('target_directory', nargs = 1, type=os.path.abspath, help = 'Specify the directory in which you want to count rows of files.')

parser.add_argument('output_directory', nargs = 1, type=os.path.abspath, help = 'Specify where to save the row count output.')



## ignore - potential feature: counting multiple file types
# parser.add_argument('--all', type = str, default = 'all', help = "Count rows in all files.") # got to filter out hidden files from this 
    

def file_len(target_directory, fname):
    
    # load each file and count rows using enumerate
    try:
        with open(str(target_directory +"/"+ fname)) as f:
            i = 0
            for i, l in enumerate(f):
                pass
            return i

    except UnicodeDecodeError:
        pass

 
        
        # skip over non utf-8 files 
        #except UnicodeDecodeError:
            #pass
        # skip over directories - returns None
        #except IsADirectoryError:
            #pass
    

def right_filetype(a_file, filetype):
    if a_file.endswith(str(filetype)):
        return True
    else:
        return False

def count_all(target_directory, filetype):
    
    # initiate storage for row_count info
    lengths = dict()
    
    print(target_directory)
    
    # run thru every file in the current directory
    for a_file in os.listdir(target_directory):
        
        # check if the file is of the specified type
        if right_filetype(a_file, filetype) is True:
        
            # begin counting rows
            length = file_len(target_directory, a_file)
            lengths[a_file] = length # subtract one to remove header count    
        else:
            pass
        
    return lengths

def save_counts(target_directory, output_directory, filetype):
    lengths = count_all(target_directory, filetype)
     # create a csv with length info for each file in the directory of interest
    with open(output_directory + "/" + os.path.basename(os.path.normpath(target_directory)) + '_row_counts.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["File Name", "Number of Rows"])
        for key in lengths.keys():
            f.write(f"{key},{lengths[key]}\n")


            
def main():
  
    # argparse module takes care of user input elegantly 
    args = parser.parse_args()

    
    # start counting - each function calls the next
    save_counts(args.target_directory[0], args.output_directory[0], args.filetype)
    
    # Terminal output - confirmation 
    print("Row count output is saved at %s" %args.output_directory[0] + "/" + os.path.basename(os.path.normpath(args.target_directory[0])) + '_row_counts.csv')
    
    pass


if __name__ == '__main__':
    main()