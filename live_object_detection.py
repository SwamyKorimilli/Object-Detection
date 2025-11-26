import cv2
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("models/yolov8n.pt")  

# Define common objects for day-to-day recognition
TARGET_CLASSES = {
    "person", "bottle", "tv", "cell phone", "book", "cup",
    "fork", "knife", "spoon", "bowl", "microwave", "oven","dog"
    "toaster", "bed", "sofa", "table", "clock", "remote", "keyboard", "mouse",
    "backpack", "handbag", "cat", "cow", "sheep", "horse", "car", "bus", "truck"
}

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 detection
    results = model(frame)

    # Process detections
    for result in results:
        for box, class_id, conf in zip(result.boxes.xyxy, result.boxes.cls, result.boxes.conf):
            class_name = model.names[int(class_id)]

            # Only display selected objects
            if class_name in TARGET_CLASSES:
                x1, y1, x2, y2 = map(int, box)
                label = f"{class_name} ({conf:.2f})"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show output
    cv2.imshow("Live Object Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
