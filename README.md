# row_count
A simple command-line tool to count the rows of each file in a given directory. 


```
usage: row_count.py [-h]
                    {csv,txt,tsv}
                    target_directory
                    output_directory


positional arguments:
  {csv,txt,tsv}
               Specify the file type you want to evaluate.
               
  target_directory
               Specify the directory in which you want to count rows of files.
               
  output_directory
               Specify where to save the row count output.

optional arguments:
  -h, --help   Show this help message and exit.
```



Example: Say you want the row counts of all txt files located in your Documents folder, and you want that output to be saved on your Desktop.

```
python row_count.py txt ./Documents ./Desktop 
```

Output: A csv file containing the filename and number of rows in each txt file.





##### Notes - 
(1) This tool doesn't walk through sub-directories, just the top level directory.

(2) Relative paths are considered valid input.

(3) The script specifies Python installed through Anaconda Navigator. You may need to change this for your own machine.
