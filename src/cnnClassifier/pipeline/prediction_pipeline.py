import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from cnnClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from cnnClassifier.utils.common import read_yaml


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict_result(self):
        trained_model_path = read_yaml(
            CONFIG_FILE_PATH).model_training.trained_model_path
        trained_model = load_model(trained_model_path)

        params_img_size = read_yaml(PARAMS_FILE_PATH).IMAGE_SIZE
        test_img = image.load_img(
            self.filename, target_size=tuple(params_img_size[:-1]))
        test_img = image.img_to_array(test_img)
        test_img = np.expand_dims(test_img, axis=0)
        result = np.argmax(trained_model.predict(test_img), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Tumor'
        else:
            prediction = 'Normal'
        return [{'image': prediction}]
