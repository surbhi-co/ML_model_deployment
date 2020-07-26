import numpy as np
from flask import Flask, request,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('online_shopping_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction
    if output==0:
        return render_template('index.html', prediction_text='This session may not lead to a transaction'.format(output))
    else:
        return render_template("index.html",prediction_text="This session may lead to a transaction".format(output))

if __name__ == "__main__":
    app.run(debug=True)