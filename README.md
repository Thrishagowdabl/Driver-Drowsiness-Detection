 Driver Drowsiness Detection using Deep Learning (CNN + OpenCV)

A real-time Driver Drowsiness Detection System built using Convolutional Neural Networks (CNN) and OpenCV.
It continuously monitors the driver’s eye state through a webcam feed and triggers an alert when signs of drowsiness are detected.

 Overview

Drowsiness while driving is one of the major causes of road accidents.
This project aims to reduce such risks by detecting the driver’s eye state in real-time.
If the driver’s eyes remain closed beyond a certain time threshold, an alarm is triggered to alert them.

 Key Features

 Real-time face and eye detection using Haar Cascade classifiers

CNN model trained to classify eyes as open or closed

 Alarm system triggers when eyes remain closed for too long

 Works on any standard laptop with a webcam

 Achieves up to 95% accuracy on test datasets

 Configurable parameters (thresholds, model paths, etc.)

 Tech Stack
Category	Technology
Programming Language	        Python
Computer Vision             	OpenCV
Deep Learning                	TensorFlow / Keras
Classifiers                  	Haar Cascade (haarcascade_frontalface_default.xml, haarcascade_eye.xml)
Sound Alert                  	winsound
IDE	                         VS Code

 How It Works

Capture live video from the webcam.

Detect face and eye regions using Haar Cascades.

Extract and preprocess the eye region (resize, normalize, etc.).

Pass the processed image to a CNN model that predicts whether eyes are open or closed.

Maintain a score:

Increment when eyes are closed.

Decrement when eyes are open.

If the score exceeds a threshold → trigger an alarm.

Reset score after alert.

Workflow Diagram
Textual Flow
Start Camera Feed 
      ↓
Detect Face & Eyes 
      ↓
Preprocess Eye Region 
      ↓
CNN Prediction (Open/Closed)
      ↓
Update Score 
      ↓
If Score > Threshold → Trigger Alarm 
      ↓
Reset Score

 Installation & Setup
1️ Clone the Repository
git clone https://github.com/Thrishagowdabl/Driver-Drowsiness-Detection.git
cd Driver-Drowsiness-Detection

2️ Install Dependencies
pip install opencv-python tensorflow numpy keras pygame

3️ Train the Model
python drowsiness_cnn.py

4️ Run the Detection
python detect_from_cam.py

 Project Structure
Driver-Drowsiness-Detection/
│
├── dataset/                                      # Training and testing images
├── drowsiness_cnn.py                             # CNN model training script
├── detect_from_cam.py                            # Real-time detection script
├── haarcascade_frontalface_default.xml
├── haarcascade_eye.xml
├── drowsiness_model.h5                           # Saved model
└── README.md

Results

Real-time detection with high accuracy

Alarm triggers when driver appears drowsy

Portable and easy to deploy

Author

Thrisha Gowda B L
 Mysuru, India
 Information Science and Engineering

