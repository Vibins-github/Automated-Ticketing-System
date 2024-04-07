import cv2
import face_recognition
import pandas as pd
from datetime import datetime

# Load known faces and names
known_faces = []
known_names = []

# Load known faces from images
# Loop through your data folder and load each person's images using face_recognition.load_image_file()
# Append each person's face encoding to known_faces list
# Append the corresponding name to known_names list

# Initialize video capture
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face found in the frame
    for face_encoding in face_encodings:
        # Compare face encoding with known faces
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"

        # Check if any known face matches
        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]

        # Draw rectangle and put text on the frame
        # This part can be customized based on your preference

        # Export data to Excel
        if name != "Unknown":
            data = {'Name': [name], 'Timestamp': [datetime.now()]}
            df = pd.DataFrame(data)
            df.to_excel('recognized_people.xlsx', index=False, mode='a', header=False)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture
video_capture.release()
cv2.destroyAllWindows()
