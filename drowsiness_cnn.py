# drowsiness_cnn.py
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout

# Image preprocessing
train_data = ImageDataGenerator(rescale=1./255, zoom_range=0.2, shear_range=0.2, horizontal_flip=True)
test_data = ImageDataGenerator(rescale=1./255)

train_ds = train_data.flow_from_directory(
    "dataset/train",
    target_size=(80, 80),
    batch_size=32,
    class_mode='binary')

test_ds = test_data.flow_from_directory(
    "dataset/test",
    target_size=(80, 80),
    batch_size=32,
    class_mode='binary')

# CNN Model
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(80, 80, 3)),
    MaxPool2D(2,2),

    Conv2D(64, (3,3), activation='relu'),
    MaxPool2D(2,2),

    Conv2D(128, (3,3), activation='relu'),
    MaxPool2D(2,2),

    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(1, activation='sigmoid')  # binary output
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.summary()

# Train Model
history = model.fit(train_ds, validation_data=test_ds, epochs=10)

model.save("drowsiness_model.h5")

print(" Model training complete and saved.")
