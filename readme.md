Run the script in the same directory as the input file (probably "export.csv") to avoid having to type out its full path.  The format of the command is:

    python trancher.py input_file_name output_file_name tranch_size

For example, to generate tranches of size 1000, run:

    python trancher.py input_file.csv output_file.csv 1000
   
Each contact is randomly assigned to a tranch, so the exact number of contacts per tranch is only approximate.
