import os
import zipfile
import gdown
from chickenDieaseClassifier import logger
from chickenDieaseClassifier.utils.common import get_size
from chickenDieaseClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
    
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            try:
                file_id = self.config.source_url.split('/')[-2]
                gdown.download(url='https://drive.google.com/uc?id='+file_id, output=self.config.local_data_file, quiet=False)
                logger.info(f"Data downloaded at {self.config.local_data_file}")
            except Exception as e:
                raise e

        else:
            logger.info(f"File already exist od size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """Extracts the zip file into the data directory.
            The function return none
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)