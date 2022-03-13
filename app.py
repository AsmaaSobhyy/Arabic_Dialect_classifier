
import base64

from flask import Flask, request, render_template
from sklearn.pipeline import Pipeline
import pickle



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    with open("ml_pipe.pickle", "rb") as f:
        (model) = pickle.load(f)

    to_predict_list = request.form.to_dict()

    prediction = model.predict([to_predict_list['text_to_pred']])

    return render_template('predict.html', prediction = prediction)

if __name__ == '__main__':
    app.run()