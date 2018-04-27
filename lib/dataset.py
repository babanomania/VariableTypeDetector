
from lib.util import *

def file_to_dataset( file_name ):
    dataset = []

    with open(file_name) as raw_data_file:
        for line in raw_data_file:

            data_line = line.rstrip().split(',')
            str_dataset = transform_to_dataset( data_line[1] )
            dataset.append(str_dataset)

    return dataset

def file_to_predictions( file_name ):
    predictions = []

    with open(file_name) as raw_data_file:
        for line in raw_data_file:

            data_line = line.rstrip().split(',')
            predictions.append(data_line[0])

    return predictions

def file_to_testdata( file_name ):
    testdata = []

    with open(file_name) as raw_data_file:
        for line in raw_data_file:

            data_line = line.rstrip().split(',')
            testdata.append(data_line[1])

    return testdata

def transform_to_dataset( testData ):

    isNumber = False
    isSpace = False
    isHyphen = False
    isDot = False
    isColon = False
    isString = False
    isOthSpChr = False

    isLenDate = False
    isLenTMSP = False

    for a in testData:

        if is_number(a):
            isNumber = True

        elif ( a == ' ' ):
            isSpace = True

        elif ( a == '-' ):
            isHyphen = True

        elif ( a == '.' ):
            isDot = True

        elif ( a == ':' ):
            isColon = True

        elif a.isalpha():
            isString = True

        else:
            isOthSpChr = True

    return [ sigmoid(isNumber), sigmoid(isSpace), sigmoid(isHyphen),
             sigmoid(isDot), sigmoid(isColon), sigmoid(isString), sigmoid(isOthSpChr),
             sigmoid( len(testData) == len('12-12-1900') ),
             sigmoid( len(testData) == len('12-12-1900 12:12:12') ) ]
