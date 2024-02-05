import face_recognition
import os
from PIL import Image
import numpy as np

image = face_recognition.load_image_file("database copy/boy1.jpg")

folder_path = 'database copy'

image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

compare1 = face_recognition.face_encodings(image)[0]

for image_file in image_files:
    # Construct the full path to the image
    image_path = os.path.join(folder_path, image_file)
    try:
        with Image.open(image_path) as img:
            # Convert PIL image to NumPy array
            img_array = np.array(img)

            # Extract face encodings for the current image
            compare2 = face_recognition.face_encodings(img_array)[0]

            # Compare the face encodings
            result = face_recognition.compare_faces([compare1], compare2)

            if result[0]:
                print(f"{image_file}: Present")
            else:
                print(f"{image_file}: Absent")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

