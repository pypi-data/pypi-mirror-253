# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md
import sys
from flask import render_template, request, jsonify
import flask
from flask import Flask
import numpy as np
import traceback
import pickle
import pandas as pd
import os

# App definition
app = Flask(__name__, template_folder='templates')

port = sys.argv[1]
model_path = sys.argv[2]

with open(model_path, 'rb') as f:
    classifier = pickle.load(f)


# if necessary, prepare your model columns
# with open('model_columns.pkl', 'rb') as f:
#   model_columns = pickle.load(f)


@app.route('/')
def welcome():
    return "Now you can ask your model to predict anything you want!"


@app.route('/stop')
def stop():
    os.system('kill %d' % os.getpid())
    return "You stopped the controller!"


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if flask.request.method == 'GET':
        return "Prediction page"

    if flask.request.method == 'POST':
        try:
            json_ = request.json
            query = pd.get_dummies(pd.DataFrame(json_))
            # if you need to specify columns:
            #           query = query_.reindex(columns = model_columns, fill_value= 0)
            prediction = list(classifier.predict(query))

            return jsonify({
                "prediction": str(prediction)
            })

        except:
            return jsonify({
                "trace": traceback.format_exc()
            })


# If you don't need new thread use this:
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
