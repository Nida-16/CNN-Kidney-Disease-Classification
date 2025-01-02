import sys
from cnnClassifier.utils.common import logger, CustomExceptionHandling
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_trainer import ModelTrainer

STAGE_NAME = '03 - Model Training stage'


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config_obj = ConfigurationManager()
        model_training_config = config_obj.get_model_training_config()

        model_trainer_component = ModelTrainer(model_training_config)
        model_trainer_component.get_base_model()
        model_trainer_component.train_valid_generator()
        model_trainer_component.train()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(
            f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx==================x')

    except Exception as e:
        raise CustomExceptionHandling(e, sys)
