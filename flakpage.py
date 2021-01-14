import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route("/")
def home():
    return render_template('form.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    print(features)
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = round(float(prediction[0]), 2)
    if(output == 1.0):
        return render_template('form.html',prediction_text='High chances of having diabetes.Consult doctor!')
    if (output == 0.0):
        return render_template('form.html', prediction_text='Low chances of having diabetes')

if __name__ == "__main__":
    app.run(debug=True)