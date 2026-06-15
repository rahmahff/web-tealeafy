import tensorflow as tf
import numpy as np
import os

MODEL_PATH = os.path.join(
    "app",
    "models",
    "saved_model3"
)

# Load SavedModel
model = tf.keras.layers.TFSMLayer(
    MODEL_PATH,
    call_endpoint='serving_default'
)

# LABEL PENYAKIT
LABELS_PENYAKIT = [
    'Algal Leaf Spot',
    'Blister Blight',
    'Brown Blight',
    'Gray Blight',
    'Helopeltis',
    'Red Rust',
    'Red Spider Mite',
    'Sehat'
]

# LABEL KESIAPAN
LABELS_KESIAPAN = [
    'Belum Siap Panen',
    'Siap Panen',
    'Tidak Layak Panen'
]

def get_prediction(processed_img):
    try:
        predictions = model(processed_img)
        print(predictions) 

        pred_penyakit = predictions['output_0']
        pred_kesiapan = predictions['output_1']
        pred_estimasi = predictions['output_2']

        # PENYAKIT
        confidence = np.max(pred_penyakit.numpy()[0])
        idx_penyakit = np.argmax(pred_penyakit.numpy()[0])
        hasil_penyakit = LABELS_PENYAKIT[idx_penyakit]
        akurasi_penyakit = float(confidence * 100)

        # KESIAPAN
        idx_kesiapan = np.argmax(pred_kesiapan.numpy()[0])
        hasil_kesiapan = LABELS_KESIAPAN[idx_kesiapan]
        akurasi_kesiapan = float(np.max(pred_kesiapan.numpy()[0]) * 100)

        # ESTIMASI
        hasil_estimasi = float(pred_estimasi.numpy()[0][0])

        return {
            'penyakit': hasil_penyakit,
            'akurasi_p': round(
                akurasi_penyakit, 2
            ),

            'kesiapan': hasil_kesiapan,
            'akurasi_k': round(
                akurasi_kesiapan, 2
            ),

            'estimasi_raw': round(
                hasil_estimasi, 2
            )
        }

    except Exception as e:
        print(
            f"Error pada Inference: {e}"
        )
        return None