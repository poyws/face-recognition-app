import face_recognition
import os
import pickle

def encode_known_faces():
    known_faces = {"names": [], "encodings": []}
    known_faces_dir = "models/known_faces"

    for filename in os.listdir(known_faces_dir):
        if filename.endswith(".jpg"):
            image = face_recognition.load_image_file(os.path.join(known_faces_dir, filename))
            encoding = face_recognition.face_encodings(image)[0]
            known_faces["names"].append(filename[:-4])
            known_faces["encodings"].append(encoding)

    return known_faces
