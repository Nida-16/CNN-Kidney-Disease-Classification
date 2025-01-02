import os
from cnnClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import (DataIngestionConfig,
                                                PrepareBaseModelConfig,
                                                ModelTrainingConfig)


class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir, config.unzip_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        params = self.params

        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_path,
            updated_base_model_path=config.updated_base_model_path,
            params_image_size=params.IMAGE_SIZE,
            params_include_top=params.INCLUDE_TOP,
            params_classes=params.CLASSES,
            params_weights=params.WEIGHTS,
            params_learning_rate=params.LEARNING_RATE
        )
        return prepare_base_model_config

    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_training
        params = self.params
        base_model_config = self.config.prepare_base_model
        training_data_folder = os.path.join(
            self.config.data_ingestion.unzip_dir, 'kidney-ct-scan-image')

        create_directories([config.root_dir])

        model_training_config = ModelTrainingConfig(
            root_dir=config.root_dir,
            updated_base_model_path=base_model_config.updated_base_model_path,
            trained_model_path=config.trained_model_path,
            training_data_dir=training_data_folder,
            params_epoch=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_if_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE,
        )
        return model_training_config
