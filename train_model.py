import sys
import re
import pickle
#from sklearn.preprocessing import StandardScaler
from lib.dataset import *
from lib.trainer import *
from constants import *



input_cols = file_to_list( cols_file )
#scaler = StandardScaler()
#scaler.fit(input_dataset)
#input_dataset = scaler.transform(input_dataset)

model = create_model( dataset_file, input_cols )
pickle.dump( model, open(model_dump_file, 'wb') )

print "model trained"
