import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # load model 
        model = load_model(os.path.join('artifacts','training','model.h5'))
        test_image = image.load_img(self.filename, target_size =(224,224))
        test_image = np.expand_dims(test_image,axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        if result[0] == 0:
            return [{"image":'Coccidiosis'}]
        elif result[0] == 1:
            return [{"image":'Healthy'}]
        elif result[0] == 2:
            return [{"image":'New Castle Disease'}]
        else:
            return [{"image":'Salmonella'}]