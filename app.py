import os
from flask_cors import CORS, cross_origin
from flask import Flask, request, render_template, jsonify
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction_pipeline import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')


app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = 'Input_CT_Scan.jpg'
        self.classifier = PredictionPipeline(self.filename)


@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict_result()
    return jsonify(result)


if __name__ == '__main__':
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080)
