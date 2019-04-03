# Notes:

# This Python file goes though the directory you want and deletes all the unnecessary duplicate files automatically.

import os, os.path

for root, dirs, files in os.walk("V:\\users\\Edward\\OFF"):
    for file in files:
        if file == 'StickSlip_summary_parsed_final.csv':  # Change file name option 1 here
            os.remove(os.path.join(root, file))
            print('Removed ' + os.path.join(root, file))
        elif file == 'StickSlip_summary_parsed.csv':  # Change file name option 2 here
            os.remove(os.path.join(root, file))
            print('Removed ' + os.path.join(root, file))
        elif file == 'StickSlip_summary.csvparsed':  # Change file name option 3 here
            os.remove(os.path.join(root, file))
            print('Removed ' + os.path.join(root, file))
