import sys
import re
import pickle
#from sklearn.preprocessing import StandardScaler
from lib.dataset import *
from lib.trainer import *
from constants import *
from sklearn.metrics import classification_report,confusion_matrix

input_dataset = file_to_dataset(test_data_file)
actual_op = file_to_predictions(test_data_file)
test_strings = file_to_testdata(test_data_file)

#scaler = StandardScaler()
#scaler.fit(input_dataset)
#input_dataset = scaler.transform(input_dataset)

#print " -- input dataset ", input_dataset
model = pickle.load( open(model_dump_file, 'rb') )
predictions = model.predict(input_dataset)

print
print " -- Confusion Matrix "
print(confusion_matrix(actual_op,predictions))

print
print " -- classification Report "
print(classification_report(actual_op,predictions))

print
print " -- Correct Predictions "
for index, item in enumerate(predictions):
    actual_op_tobe = actual_op[index]
    if( actual_op_tobe == item ):
        print "{} => {}".format( test_strings[index].ljust(22), actual_op_tobe.ljust(8), item )
print

print
print " -- Incorrect Predictions "
for index, item in enumerate(predictions):
    actual_op_tobe = actual_op[index]
    if( actual_op_tobe != item ):
        print "{} Actual => {} Predicted => {}".format( test_strings[index].ljust(22), actual_op_tobe.ljust(8), item )
print
