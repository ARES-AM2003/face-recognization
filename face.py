import cv2
import queue
import face_recognition
import numpy as np
import threading


# Capture camera
camera = cv2.VideoCapture(0)

# Set frame property
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cnt = 0
face_match = False
reference_img_path = "/home/aresam/Desktop/face/images/test_image.jpg"

# Load the reference image and encode it
reference_img = face_recognition.load_image_file(reference_img_path)
reference_encoding = face_recognition.face_encodings(reference_img)[0]

# Queue for frames thread manage garna ra thread ko lagi frame pass garna
frame_queue = queue.Queue()

def check_face():
    global face_match
    # face match na vayesama registered face haru check garna
    while True:
        frame = frame_queue.get()
        if frame is None:
            break
        
        # Encode faces in the frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        
        face_match = False
        
        for face_encoding in face_encodings:
            # Compare faces
            matches = face_recognition.compare_faces([reference_encoding], face_encoding)
            if True in matches:
                face_match = True
                break

# Start face checking thread
# thread  parallel execution garna ra smooth execution garnause garya
thread = threading.Thread(target=check_face)
thread.start()

# Camera frame window
while True:
    # ret chai frame read garna ko lagi use garya
    ret, frame = camera.read()

    if ret:
        # cnt chai sab frame na heri kana 30 frame ma herna use garya 
        if cnt % 30 == 0:
            frame_queue.put(frame.copy())
        cnt += 1

        if face_match:
            cv2.putText(frame, "Face Match", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "Face Not Match", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("Camera", frame)

    # Exit condition
    if cv2.waitKey(1) == ord('q'):
        break

# Stop face checking thread
frame_queue.put(None)
thread.join()

# Release resources
camera.release()
cv2.destroyAllWindows()
