# Author : Abhijeet Vaidya

import os.path
import csv
import sys
from logging import FileHandler

#import prettytable


class FileHandler:

    initial = 1

    def __init__(self, filePath):

        self.filePath = os.path.abspath(filePath)

    def display_file_name(self):

        fileName = str(os.path.basename(self.filePath))

        return fileName

    def displayResults(self):

        try:

            file = open(self.filePath, 'r')

            readInputData = csv.reader(file)

            printerObject = csv.writer(sys.stdout, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)

            # If first file

            currRow = 0

            for rows in readInputData:

                if currRow != 0:

                    data = rows

                    data.append(self.display_file_name())

                    printerObject.writerow(data)

                else:

                    if FileHandler.initial == 1:

                        data = rows

                        data.append('filename')

                        printerObject.writerow(data)

                    currRow = currRow + 1

            #Set file already read before.

            FileHandler.initial = -1

        except IOError:

            #If file does not exist.

            print('Error Loading file or File does not exist!!!')

def main():

    # Check if user passes the file paths to be appended.

    if(len(sys.argv) >= 2) :

        for i in sys.argv[1:]:

            # Solve separately for every file. and print to stdout

            FileHandler(i).displayResults()


    else :

        print("Please enter valid input stream (python csv-combiner-pmg-challenge.py path_to_file1.csv [path_to_file2.csv] [....])")




if __name__ == '__main__':
    main()