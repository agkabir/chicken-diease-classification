from chickenDieaseClassifier import logger
from chickenDieaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from chickenDieaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from chickenDieaseClassifier.pipeline.stage_03_training import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    base_model_pipeline = PrepareBaseModelPipeline()
    base_model_pipeline.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    model_training_pipeline = ModelTrainingPipeline()
    model_training_pipeline.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e