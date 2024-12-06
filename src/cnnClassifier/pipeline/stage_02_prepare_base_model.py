import sys
from cnnClassifier import logger, CustomExceptionHandling
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier.config.configuration import ConfigurationManager

STAGE_NAME = '02 - Prepare Base Model'


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config_obj = ConfigurationManager()
        prepare_base_model_config = config_obj.get_prepare_base_model_config()

        prepare_base_model_obj = PrepareBaseModel(prepare_base_model_config)
        prepare_base_model_obj.get_base_model()
        prepare_base_model_obj.update_base_model()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(
            f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx==================x')
    except Exception as e:
        raise CustomExceptionHandling(e, sys)
