import numpy as np
from tensorflow.keras.models import load_model
import joblib

# Load model and scaler
model = load_model('sentiment_model.h5')
scaler = joblib.load('scaler.pkl')

new_data = np.random.rand(10, 300)

new_data = scaler.transform(new_data)

predictions = model.predict(new_data)
print("Predictions:", predictions)