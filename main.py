from chickenDieaseClassifier import logger
from chickenDieaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e