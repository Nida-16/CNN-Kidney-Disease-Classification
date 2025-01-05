import os
import mlflow
import mlflow.keras
from pathlib import Path
import tensorflow as tf
from urllib.parse import urlparse
from cnnClassifier.utils.common import save_json, read_yaml, logger
from cnnClassifier.config.configuration import EvaluationConfig


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale=1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation='bilinear'
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset='validation',
            shuffle=False,
            **dataflow_kwargs
        )

    def evaluation(self):
        self.model = tf.keras.models.load_model(
            self.config.path_to_trained_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()

    def save_score(self):
        scores = {'loss': self.score[0], 'accuracy': self.score[1]}
        save_json(path=Path('scores.json'), data=scores)

    def log_into_mlflow(self):
        credentials_path = Path('secrets.yaml')
        creds = read_yaml(credentials_path)
        os.environ["MLFLOW_TRACKING_URI"] = creds.MLFLOW_TRACKING_URI
        os.environ["MLFLOW_TRACKING_USERNAME"] = creds.MLFLOW_TRACKING_USERNAME
        os.environ["MLFLOW_TRACKING_PASSWORD"] = creds.MLFLOW_TRACKING_PASSWORD

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_storage = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {'loss': self.score[0], 'accuracy': self.score[1]})

            if tracking_url_type_storage != 'file':
                mlflow.keras.log_model(
                    self.model, 'model', registered_model_name='VGG16Model')
                logger.info(
                    'Model registered as VGG16Model in the MLflow Model Registry.')
            else:
                mlflow.keras.log_model(self.model, 'model')
                logger.info(
                    'Tracking backend is file-based. Logging the model without registering')
