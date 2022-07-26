import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('Fish_Species.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('fish_species.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = (prediction[0])

    return render_template('fish_species.html', prediction_text='Species of fish$ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)