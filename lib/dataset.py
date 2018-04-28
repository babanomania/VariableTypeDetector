import re
from lib.util import *

def file_to_dataset( file_name ):
    dataset = []

    with open(file_name) as raw_data_file:
        for line in raw_data_file:

            data_line = line.rstrip().split(',')
            str_dataset = transform_to_dataset( data_line[1].strip() )
            dataset.append(str_dataset)

    return dataset

def file_to_predictions( file_name ):
    predictions = []

    with open(file_name) as raw_data_file:
        for line in raw_data_file:

            data_line = line.rstrip().split(',')
            predictions.append(data_line[0].strip())

    return predictions

def file_to_testdata( file_name ):
    testdata = []

    with open(file_name) as raw_data_file:
        for line in raw_data_file:

            data_line = line.rstrip().split(',')
            testdata.append(data_line[1].strip())

    return testdata

def transform_to_dataset( testData ):

    hasNumber = False
    hasOthSpChr = False

    for a in testData:

        if a.isdigit():
            hasNumber = True

        elif ( not ( a.isalpha() or ' ' in testData or '-' in testData or '.' in testData or ':' in testData) ):
            hasOthSpChr = True

    return [ sigmoid(is_number(testData)),
             sigmoid(re.match(".*\d.*", testData)),
             sigmoid(' ' in testData),
             sigmoid('-' in testData),
             sigmoid('.' in testData),
             sigmoid(':' in testData),
             sigmoid( hasOthSpChr ),
             sigmoid( len(testData) == len('12-12-1900') ),
             sigmoid( len(testData) == len('12-12-1900 12:12:12') ) ]
