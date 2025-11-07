import cv2
import time
import threading
import winsound

# Haarcascade files
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

score = 0
MAX_SCORE = 50
alarm_on = False

# Run beep in background
def beep_alarm():
    global alarm_on
    while alarm_on:
        winsound.Beep(1000, 300)  # short beep but non-blocking due to thread
        time.sleep(0.1)

frame_center_x = 320
frame_center_y = 240
box_size = 250

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]

   
    x1 = frame_center_x - box_size//2
    y1 = frame_center_y - box_size//2
    x2 = frame_center_x + box_size//2
    y2 = frame_center_y + box_size//2
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255,255,0), 2)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    face_in_box = False
    eyes_open = False

    for (x, y, w_f, h_f) in faces:
        face_center_x = x + w_f//2
        face_center_y = y + h_f//2

        if x1 < face_center_x < x2 and y1 < face_center_y < y2:
            face_in_box = True
        else:
            face_in_box = False

        roi_gray = gray[y:y+h_f, x:x+w_f]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)

        if len(eyes) > 0:
            eyes_open = True
        else:
            eyes_open = False

        cv2.rectangle(frame, (x, y), (x+w_f, y+h_f), (0,255,0), 2)

   
    if face_in_box:
        if eyes_open:
            if score > 0:
                score -= 1
            cv2.putText(frame, "Eyes Open", (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        else:
            score += 1
            cv2.putText(frame, "Eyes Closed", (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    else:
        score += 2
        cv2.putText(frame, "FACE OUTSIDE BOX!", (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    
    if score >= MAX_SCORE:
        cv2.putText(frame, "ALERT! DROWSINESS!", (50,200), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 3)
        if not alarm_on:
            alarm_on = True
            threading.Thread(target=beep_alarm, daemon=True).start()
    else:
        alarm_on = False

    cv2.putText(frame, f"Score: {score}", (20,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        alarm_on = False
        break

cap.release()
cv2.destroyAllWindows()
