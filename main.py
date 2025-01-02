import sys
from cnnClassifier.utils.common import logger, CustomExceptionHandling
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline


STAGE_NAME = '01 - Data Ingestion stage'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    data_ingestion_obj = DataIngestionTrainingPipeline()
    data_ingestion_obj.main()
    logger.info(
        f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx==================x')
except Exception as e:
    raise CustomExceptionHandling(e, sys)


STAGE_NAME = '02 - Prepare Base Model'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    prepare_base_model_obj = PrepareBaseModelTrainingPipeline()
    prepare_base_model_obj.main()
    logger.info(
        f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx==================x')
except Exception as e:
    raise CustomExceptionHandling(e, sys)

STAGE_NAME = '03 - Model Training stage'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    model_training_obj = ModelTrainingPipeline()
    model_training_obj.main()
    logger.info(
        f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx==================x')
except Exception as e:
    raise CustomExceptionHandling(e, sys)
