# Notes:

# This Python file assumes you have the .OFF files (binary) separated in each other individual folder. Note: Use mkdir_file.py if you haven't
# This Python file will only be used for Ariel-X Stick Slip test.  This parser does not apply to Op-Shock/Bench/Stick Slip Bench
# This also assumes you have the Macro Excel saved in a directory similar to C:\Users\labuser\AppData\Roaming\Microsoft\Excel\XLSTART\PERSONAL.XLSB
# If you don't have it, please obtain Macro (from Edward) and save it in your PERSONAL.XLSB

# Summary: This Python code script will traverse the .OFF files and parse any StickSlip_Summary.csv for Ariel-X automatically.

import os, os.path
import win32com.client

# Replace OFF directory here
for root, dirs, files in os.walk("V:/users/Edward/OFF"): #  Traverses through all the existing root and subdirectory of files that it contains
    for file in files: #  Traveres files only
        if file == "StickSlip_summary.csv":
            print('Currently parsing all the Excel data for you...')
            print('Starting with:')
            print(os.path.join(root,file))
            print('Please wait until parser is finished...')
            xl = win32com.client.DispatchEx('Excel.Application')
            xl.Workbooks.Open(os.path.join(root,file))
            xl.Application.Run("PERSONAL.XLSB!SS_ArielX") #  Run function calls the macro
            xl.Workbooks.Open(os.path.join(root,file))
            xl.ActiveWorkbook.SaveAs(Filename=os.path.splitext(os.path.join(root,file))[i0] + "_parsed_final.csv", FileFormat="6") #FileFormat = 6 saves the file as a .csv
            xl.Application.DisplayAlerts = False #  This will ignore any GUI pop ups that will prompt the user to save the file, when it isn't necessary
            xl.Application.Quit()
            print('Finished parsing the current Excel file.  Now saving...')
            print('Finished!')
            print(' ')           
            del xl
            
