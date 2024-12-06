import sys
import gdown
from zipfile import ZipFile
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier.utils.common import create_directories
from cnnClassifier import logger, CustomExceptionHandling


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        try:
            dataset_url = self.config.source_URL
            download_location = self.config.local_data_file
            artefacts_dir = self.config.root_dir
            sheet_id = dataset_url.split('/')[-2]

            create_directories([artefacts_dir])

            gdown.download(id=sheet_id, output=download_location)
            logger.info(
                f'Downloaded dataset from {dataset_url} to {download_location}!')
        except Exception as e:
            raise CustomExceptionHandling(e, sys)

    def extract_zipfile(self):
        try:
            zipfile_filepath = self.config.local_data_file
            unzip_location = self.config.unzip_dir
            with ZipFile(zipfile_filepath, 'r') as zf:
                zf.extractall(unzip_location)
                logger.info(
                    f'Zipfile extracted from {zipfile_filepath} to folder {unzip_location}')
        except Exception as e:
            raise CustomExceptionHandling(e, sys)
