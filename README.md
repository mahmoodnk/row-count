# row-count
Objective: Find row counts for files in a given directory

Usage: row_count.py [-h]
                    {csv,txt,tsv}
                    target_directory
                    output_directory

A simple command-line tool to count the rows of each file in a given directory.

positional arguments:
  {csv,txt,tsv}
               Specify the file type you want to evaluate.
               
  target_directory
               Specify the directory in which you want to count rows of files.
               
  output_directory
               Specify where to save the row count output.

optional arguments:
  -h, --help   Show this help message and exit.
