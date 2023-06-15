import streamlit as st
import cv2
import os


def from_xywh_to_trbl(x, y, w, h):
    top = y + h
    bottom = y - h
    left = x - w
    right = x + w
    return top, right, bottom, left


def from_trbl_to_xywh(top, right, bottom, left):
    x = 0.5 * (right + left)
    y = 0.5 * (top + bottom)
    w = right - left
    h = top - bottom


# st.title("Webcam Live Feed")

def build_face_recognition():
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)

    cascPath = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    while run:
        ret, frame = camera.read()
        if ret:
            frame = cv2.flip(frame, 1)
            color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            # faces = face_recognition.face_locations(color, 'hog')

            for (x, y, w, h) in faces:
                cv2.rectangle(color, (x, y), (x + w, y + h), (0, 255, 0), 2)
                roi = color[y:y + h, x:x + w]

            FRAME_WINDOW.image(color)
    else:
        st.write('Stopped')


