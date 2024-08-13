import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.preprocessing import StandardScaler
import joblib

data = np.random.rand(1000, 300)  # 1000 samples, 300 features each
labels = np.random.randint(0, 2, 1000)  # binary labels

# Standardize data
scaler = StandardScaler()
data = scaler.fit_transform(data)

# Save scaler
joblib.dump(scaler, 'scaler.pkl')

model = Sequential([
    Dense(128, input_shape=(300,), activation='relu'),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(1, activation='sigmoid')
])

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(data, labels, epochs=10, batch_size=32)

model.save('sentiment_model.h5')