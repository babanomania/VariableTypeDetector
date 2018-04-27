import sys
import re
import pickle
#from sklearn.preprocessing import StandardScaler
from lib.dataset import *
from lib.trainer import *
from constants import *

input_data = sys.argv[1]

input_dataset = [transform_to_dataset( input_data )]

#scaler = StandardScaler()
#scaler.fit(input_dataset)
#input_dataset = scaler.transform(input_dataset)

#print " -- input dataset ", input_dataset
model = pickle.load( open(model_dump_file, 'rb') )
predictions = model.predict(input_dataset)

print input_data, " => ", predictions[0]
