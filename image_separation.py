import face_recognition
from PIL import Image
import time
import os



storage = os.listdir(path='database')
image = face_recognition.load_image_file("present/class.jpg")
face_locations = face_recognition.face_locations(image)
print("I found {} face in this photograph.".format(len(face_locations)))


i = 1


for face_location in face_locations:
    #print("Image number {}:".format(i))
    top, right, bottom, left = face_location
    print("A face location at pixel location Top: {}, Left: {}, Bottom: {}, left: {}".format(top, left, bottom, left))
        
    face_image = image[top:bottom, left:right]
    pil_image =Image.fromarray(face_image)
    photo = pil_image.save("present/faces-{}.jpg".format(i))
    i = i + 1
    
        
    
    #distance = face_recognition.face_distance([image1],image2)
    #cv2.rectangle(image, (left, top), (right, bottom), (225, 0, 225), 2)
    
    
    ''' for images in attendance:
            if(i==images):
                present'''