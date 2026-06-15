import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input


def prepare_image(
    image_path,
    target_size=(224, 224)
):
    """
    Preprocessing gambar untuk inferensi model
    """

    try:
        img = Image.open(image_path)

        if img.mode != "RGB":
            img = img.convert("RGB")

        img = img.resize(target_size)
        img_array = (tf.keras.preprocessing.image.img_to_array(img))
        img_array = (preprocess_input(img_array))
        img_array = np.expand_dims(img_array, axis=0)

        return img_array

    except Exception as e:
        print(
            f"Error pada preprocessing: {e}"
        )
        return None