import cv2
import numpy as np
import face_recognition
from PIL import Image
import os
import time

path = 'present'
database_path = 'database'
if not os.path.exists(path):
    os.makedirs(path)
cap = cv2.VideoCapture(0)
img_counter = 1

# window_name = 'Live Video'
# cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    
try:
    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()
        # if ret:
        #     cv2.imshow(window_name, frame)
        # Generate a unique filename based on the current timestamp
        timestamp = time.strftime("%H%M%S")
        filename = f"{path}/image_{img_counter}.jpg"

        # Save the captured frame to the specified file
        cv2.imwrite(filename, frame)

        print(f"Image capturing: {filename}")

        # Wait for 5 minutes before capturing the next image
        time.sleep(5)

        img_counter += 1
        if img_counter >= 6:
            break
except KeyboardInterrupt:
        
    # If you manually stop the script (e.g., by pressing Ctrl+C), release the camera
    cap.release()
    print("Camera released.")


    
# Release the camera when the script is done
cap.release()


#face comparing
storage = os.listdir(path='database')
image = face_recognition.load_image_file("present/image_5.jpg")
face_locations = face_recognition.face_locations(image)
print("I found {} face in this photograph.".format(len(face_locations)))
i = 1
for face_location in face_locations:
    #print("Image number {}:".format(i))
    top, right, bottom, left = face_location
    print("A face location at pixel location Top: {}, Left: {}, Bottom: {}, left: {}".format(top, left, bottom, left))
        
    face_image = image[top:bottom, left:right]
    pil_image =Image.fromarray(face_image)
    photo = pil_image.save("present/face-{}.jpg".format(i))
    
    print(photo,"saving image:{}".format(i))
    i = i + 1
    

# Load the image from the database
print(f"person-1")
database_image_path = 'database/Chaitanya.jpg'
image_files = [f for f in os.listdir(path) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
database_image = face_recognition.load_image_file(database_image_path)
database_face_encodings = face_recognition.face_encodings(database_image)

if len(database_face_encodings) > 0:
    compare1 = database_face_encodings[0]
else:
    print("No faces found in the database image.")

for image_file in image_files:
    # Construct the full path to the image
    image_path = os.path.join(path, image_file)
    try:
        with Image.open(image_path) as img:
            # Convert PIL image to NumPy array
            img_array = np.array(img)

            # Extract face encodings for the current image
            face_encodings = face_recognition.face_encodings(img_array)

            if len(face_encodings) > 0:
                compare2 = face_encodings[0]

                # Compare the face encodings
                result = face_recognition.compare_faces([compare1], compare2)

                if result[0]:
                    print(f"{image_file}: Present")
                else:
                    print(f"{image_file}: Absent")
            else:
                print(f"{image_file}: No face found in the image")

    except Exception as e:
        print(f"Error processing {image_path}: {e}")

print(f"person-2")

database_image_path2 = 'database/Chaitu.jpg'
image_files2 = [f for f in os.listdir(path) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
database_image2 = face_recognition.load_image_file(database_image_path2)
database_face_encodings2 = face_recognition.face_encodings(database_image2)

if len(database_face_encodings2) > 0:
    compare3 = database_face_encodings2[0]
else:
    print("No faces found in the database image.")

for image_file2 in image_files2:
    # Construct the full path to the image
    image_path2 = os.path.join(path, image_file2)
    try:
        with Image.open(image_path2) as img:
            # Convert PIL image to NumPy array
            img_array = np.array(img)

            # Extract face encodings for the current image
            face_encodings = face_recognition.face_encodings(img_array)

            if len(face_encodings) > 0:
                compare4 = face_encodings[0]

                # Compare the face encodings
                result = face_recognition.compare_faces([compare3], compare4)

                if result[0]:
                    print(f"{image_file2}: Present")
                else:
                    print(f"{image_file2}: Absent")
            else:
                print(f"{image_file2}: No face found in the image")

    except Exception as e:
        print(f"Error processing {image_path2}: {e}")
