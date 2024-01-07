from chickenDieaseClassifier.config.configurations import ConfigurationManager
from chickenDieaseClassifier.components.evaluation import Evaluation
from chickenDieaseClassifier import logger


STAGE_NAME = "Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(config=eval_config)
        evaluation.evaluation()
        evaluation.save_score()

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        model_evaluation_pipeline = ModelEvaluationPipeline()
        model_evaluation_pipeline.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e