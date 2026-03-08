import random
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
   
def get_class(model_path, labels_path, image_path):
    np.set_printoptions(suppress=True)

    # Load model
    model = load_model(model_path, compile=False)

    # Load labels
    class_names = open(labels_path, "r").readlines()

    # Prepare input array
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Load and preprocess image
    image = Image.open(image_path).convert("RGB")
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
    image_array = np.asarray(image)

    # Normalize image
    data[0] = (image_array.astype(np.float32) / 127.5) - 1

    # Predict
    prediction = model.predict(data)
    index = np.argmax(prediction)

    return class_names[index].strip(), float(prediction[0][index])