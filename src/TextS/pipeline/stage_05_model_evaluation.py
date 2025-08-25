from TextS.config.configuration import ConfigurationManager
from TextS.components.model_evaluation import ModelEvaluation
from TextS.logging import logger



class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()
        