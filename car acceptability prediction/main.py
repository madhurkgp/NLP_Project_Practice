from flask import Flask, request, render_template
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import os
from modelbuilding import logistic, dtree, randomforest, svc, knn


app = Flask(__name__)

# Get the absolute path of the directory containing this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# reading the data from csv file

def readdata():
    colnames = ['buying', 'maint', 'doors',
                'persons', 'lug_boot', 'safety', 'class']
    df = pd.read_csv(os.path.join(BASE_DIR, "car.data"), names=colnames)

    return df


# groupby with status col

def getdict(colname):

    df = readdata()
    return dict(df.groupby([colname])['class'].count())

# label encoding


def labelencoding(df):
    encoder = LabelEncoder()
    data = df.copy()
    getmappings = {}
    for col in list(data.columns):
        data[col] = encoder.fit_transform(data[col])

        # get the mappings of the encoded dataframe
        getmappings[col] = dict(
            zip(encoder.classes_, encoder.transform(encoder.classes_)))

    return getmappings, data


@ app.route("/", methods=["GET", "POST"])
def hello_world():

    getmappings, data = labelencoding(readdata())

    if request.method == "POST":

        mydict = request.form
        buy = mydict['buy']
        maintain = mydict['maintain']
        doors = mydict['doors']
        person = mydict['person']
        luggage = mydict['luggage']
        safety = mydict['safety']
        algo = mydict['algo']

        value = mydict['feature']

        values = ["Buying", "Maintenance", "Doors",
                  "Persons", "Luggage", "Safety"]
        keys = ['buying', 'maint', 'doors',
                'persons', 'lug_boot', 'safety', 'class']
        mapper = dict(zip(keys, values))

        valuecount = getdict(value)

        # Selection of Algorithm

        algomapper = {'rf': randomforest(
            data), 'dt': dtree(data), 'svc': svc(data)}

        classmapper = {0: 'unacc', 1: 'acc',
                       2: 'good', 3: 'vgood'}
        algorithm = algomapper[algo]
        accuracy, recall, precision, f1score, model = algorithm

        inputparam = [[buy, maintain, doors, person, luggage, safety]]
        predict = model.predict(inputparam)
        predictedclass = classmapper[predict[0]]

        return render_template('index.html', predictedclass=predictedclass, display=True, accuracy=round(accuracy*100, 2), precision=precision, showtemplate=True, valuecount=valuecount, value=mapper[value], mapper=valuecount)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
