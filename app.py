import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__, template_folder='templates')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    features_name = ["age","sex","cp","trestbps","chol","fbs","restecg"]
    df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict(df)
         
    if output == 1:
        prediction = " Person might Heart Disease "
    else:
        prediction = "No sign of Heart Disease "
        

    return render_template('index1.html', predicted_output='Heart Disease: {}'.format(prediction))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)