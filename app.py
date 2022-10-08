import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
# from flask_json import FlaskJSON, JsonError, json_response, as_json

# Starting file of our application
app = Flask(__name__)
# Load our model
logismodel = pickle.load(open('heart_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index2.html')

# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     data=request.json['data'] #receive the data and store it in data object.
#     print(data)
#     new_data=np.array(data).reshape(1,-1)
#     output=logismodel.predict(new_data)
#     return json_response(str(output[0]))

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=np.array(data).reshape(1,-1)
    print(data)
    output = logismodel.predict(final_input)[0]
    return render_template("index2.html",prediction_text="Model predicted value is:  ${}".format(output))

if __name__=="__main__":
    app.run(debug=True)