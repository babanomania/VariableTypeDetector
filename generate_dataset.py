import sys
import re
import csv

from lib.dataset import *
from lib.util import *
from constants import *

with open(raw_file) as raw_data_file:
    with open(dataset_file, 'w') as dsfile:
        for line in raw_data_file:

            data_line = line.rstrip().split(',')
            str_dataset = transform_to_dataset( data_line[1] )
            wr = csv.writer(dsfile, quoting=csv.QUOTE_NONE)
            wr.writerow( data_line + str_dataset )

print "Dataset Generated"
