# import requirements needed
from flask import Flask, render_template, request
from utils import get_base_url
import sklearn
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split

# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
port = 12347
base_url = get_base_url(port)

# if the base url is not empty, then the server is running in development, and we need to specify the static folder so that the static files are served
if base_url == '/':
    app = Flask(__name__)
else:
    app = Flask(__name__, static_url_path=base_url+'static')

'''
TODO: load in and clean your dataset
'''

'''
TODO: train your model on the inputs "age" and "recurrence_rate"
'''
df = pd.read_csv("./static/NKI_cleaned.csv")
df = df[['ID', 'age', 'eventdeath', 'survival', 'timerecurrence',
        'chemo', 'hormonal', 'amputation', 'histtype']]
train = df.drop(['survival', "ID", "eventdeath"], axis=1)
test = df["survival"]
regr = linear_model.LinearRegression()
lfit = regr.fit(train, test)


# print('Coefficients: \n', regr.coef_)
# testing_data = testing.loc[:,['age', 'timerecurrence',
#         'chemo', 'hormonal', 'amputation', 'histtype']]
# testing_test = testing['survival']
# prediction_of_test = regr.predict()



# set up the routes and logic for the webserver
@app.route(f'{base_url}')
def home():
    return render_template('index.html')

@app.route(f'{base_url}', methods = ["GET", "POST"])

def home_post():
    '''
    TODO: Form Input :) 
    '''
    timerecurrence = request.form['recurrence_rate']
    age = request.form['age']
    chemo = request.form['chemo']
    hormonal = request.form['hormonal']
    amputation = request.form['amputation']
    histtype = request.form['histtype']
    
    '''
    TODO: make a prediction based on the user-given recurrence_rate and age. Predict survival and return that as a variable
    '''
    prediction = True
    
    X = np.array([age, timerecurrence, chemo, hormonal, amputation, histtype]).reshape(-1, 6)
    predict_result = lfit.predict(X)[0]
    

    return render_template('index.html', prediction = prediction, predict_result = predict_result)


if __name__ == '__main__':
    # IMPORTANT: change url to the site where you are editing this file.
    website_url = 'cocalc1.ai-camp.dev'
    
    print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')
    app.run(host = '0.0.0.0', port=port, debug=True)
