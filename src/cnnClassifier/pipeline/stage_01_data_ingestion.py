import sys
from cnnClassifier import logger, CustomExceptionHandling
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier.config.configuration import ConfigurationManager

STAGE_NAME = '01 - Data Ingestion stage'


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config_obj = ConfigurationManager()
        data_ingestion_config = config_obj.get_data_ingestion_config()

        data_ingestion_obj = DataIngestion(data_ingestion_config)
        data_ingestion_obj.download_file()
        data_ingestion_obj.extract_zipfile()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(
            f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx==================x')
    except Exception as e:
        raise CustomExceptionHandling(e, sys)
