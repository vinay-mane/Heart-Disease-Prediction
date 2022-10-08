import pickle
import numpy as np

file_name = 'heart_model.pkl'
unpickleFile = open(file_name, 'rb')
model = pickle.load(unpickleFile, encoding='latin1')

def heart_pred(a):
  a= np.asarray(a)
  input = a.reshape(1,-1)
  return model.predict(input)

print(heart_pred([51,1,0,140,298,0,1,122,1,4.2,1,3,3]))

print(heart_pred([63,1,3,145,233,1,0,150,0,2.3,0,0,1]))
