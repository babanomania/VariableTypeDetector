
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.utils import shuffle

def create_model( file_path, headers ):

    print " -- building model -- "
    sampleData = pd.read_csv(file_path, names = headers)

    largeSampleData = sampleData
    for i in range(1):
        largeSampleData = largeSampleData.append(sampleData)
    sampleData = shuffle(largeSampleData)

    X = largeSampleData.drop('Type',axis=1)
    X = X.drop('Data',axis=1)
    y = largeSampleData['Type']

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    scaler = StandardScaler()
    scaler.fit(X_train)

    #X_train = scaler.transform(X_train)
    #X_test = scaler.transform(X_test)

    mlp = MLPClassifier(hidden_layer_sizes=(25,25,25),max_iter=10000, verbose=False )
    mlp.fit(X_train,y_train)

    print " -- model build done -- "
    predictions = mlp.predict(X_test)

    print " -- Confusion Matrix "
    print(confusion_matrix(y_test,predictions))

    print " -- classification Report "
    print(classification_report(y_test,predictions))

    return mlp
