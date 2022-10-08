import json
from multiprocessing.dummy import Array
from flask import Flask, request,render_template
import heart
from flask_json import FlaskJSON, JsonError, json_response, as_json

app = Flask(__name__)
FlaskJSON(app)

@app.route('/pred',methods=['GET','POST'])
def mn():
  input_data = request.get_json()['data']

  print(type(input_data[0]))
  return json_response(str(heart.heart_pred(input_data)))

@app.route('/')
def mm():
  return render_template('index.html')

if __name__ == '__main__':
  app.run()