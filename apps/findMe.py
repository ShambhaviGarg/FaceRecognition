from msilib.schema import Directory
from operator import imod
from tkinter import Image
import cv2
import numpy as np
import face_recognition
import os
import streamlit as st
import streamlit.components.v1 as components 
from PIL import Image 

@st.cache
def load_image(image_file):
    img=Image.open(image_file)
    return img 

def app():
    st.title("Face Recognition System")
    st.subheader("Click Run to start")
    run = st.checkbox('Run') 
    FRAME_WINDOW = st.image([])

    KNOWN_FACES_DIR = "test_images"
    TOLERANCE = 0.5
    FRAME_THICKNESS = 3
    FONT_THICKNESS = 2
    MODEL = "cnn"

    video = cv2.VideoCapture(0) #id of videoCapture is 0 due to using laptop camera.

    while run:

        print("loading known faces")

        known_faces = []
        known_names = []

        for name in os.listdir(KNOWN_FACES_DIR):
            for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
                image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
                encoding = face_recognition.face_encodings(image)[0]
                known_faces.append(encoding)
                known_names.append(name)
       
#safe zone
        while True:
            ret , image = video.read()
            locations = face_recognition.face_locations(image)
            encodings = face_recognition.face_encodings(image, locations)

            for face_encoding, face_location in zip(encodings, locations):
                results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
                match = None

                if True in results: #create box around face & display name
                    match = known_names[results.index(True)]
                    print(f"Match found: {match}")
                    top_left = (face_location[3], face_location[0])
                    bottom_right = (face_location[1], face_location[2])
                    color = (0,255,0)
                    cv2.rectangle(image[results.index(True)], top_left, bottom_right, color, FRAME_THICKNESS)

                    top_left = (face_location[3], face_location[2])
                    bottom_right = (face_location[1], face_location[2]+22)
                    cv2.rectangle(image[results.index(True)], top_left, bottom_right, color, FRAME_THICKNESS)
                    cv2.putText(image, match, (face_location[3]+10, face_location[2]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200,0,0), FONT_THICKNESS)

                    FRAME_WINDOW.image(image)

                    st.write("person found")
                    

    else:
        st.write("stopped")