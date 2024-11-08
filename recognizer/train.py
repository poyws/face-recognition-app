import face_recognition
import os

def train_new_face(image_path, name):
    known_faces_dir = "models/known_faces"
    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)[0]

    with open(os.path.join(known_faces_dir, f"{name}.jpg"), "wb") as f:
        face_recognition.api.face_encodings(image)[0].tofile(f)
