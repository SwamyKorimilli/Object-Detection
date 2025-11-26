# Live Object Detection with YOLOv8

This project implements **real-time object detection** using a webcam and the YOLOv8 model from Ultralytics. It focuses on detecting common day-to-day objects like persons, bottles, chairs, and vehicles, filtering results to display only specified classes. The script uses the pre-trained YOLOv8 nano model file `yolov8n.pt` (often referred to as yolov8pt in shorthand for YOLOv8 pre-trained models).

## Description

The script loads the pre-trained YOLOv8 nano model (`yolov8n.pt`) and processes video frames from the default webcam. Detections are run on each frame, and bounding boxes with labels are drawn for target objects if their class matches a predefined set. The output is displayed in a window, and the program exits when 'q' is pressed.

Target classes include: person, bottle, chair, tv, laptop, cell phone, book, cup, fork, knife, spoon, bowl, refrigerator, microwave, oven, toaster, bed, sofa, table, clock, remote, keyboard, mouse, backpack, handbag, dog, cat, cow, sheep, horse, car, bus, truck.

This is useful for **AI/ML engineering** students experimenting with computer vision, and it can be extended for cybersecurity applications like monitoring unauthorized objects in video feeds.

## Requirements

To run this project, install the following dependencies from `requirements.txt`:

- ultralytics
- opencv-python
- numpy
- torch
- torchvision
- torchaudio

## Installation

1. Clone the repository using the following command (replace `username/repo` with the actual repository path if needed):
git clone https://github.com/Rajeshram2864/Real-Time-Object-detection.git


Alternatively, you can clone from a forked version or another source.

2. Navigate to the project directory:
cd live-object-detection-yolov8


3. Install the required packages using pip:
pip install -r requirements.txt


4. Download the YOLOv8 model file `yolov8n.pt` from the Ultralytics repository and place it in a `models/` directory.

## Usage

1. Ensure your webcam is connected and accessible.

2. Run the Python script:
python live_object_detection.py



3. The script will open a window showing live detections. Press 'q' to exit.

For customization, modify the `TARGET_CLASSES` set in the script to include or exclude specific objects. This can help tailor the detection for cybersecurity scenarios, such as identifying suspicious items in a monitored area.

## Code Overview

The main script `live_object_detection.py` handles:
- Loading the YOLOv8 model (`yolov8n.pt`).
- Capturing webcam frames.
- Running object detection and filtering for target classes.
- Drawing bounding boxes and labels on detected objects.

## Contributing


Feel free to fork the repository and submit pull requests for improvements, such as adding more classes or integrating with other AI/ML tools for enhanced cybersecurity features.
