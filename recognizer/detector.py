import face_recognition
import cv2

def detect_faces(image_path, known_faces):
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_faces["encodings"], face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_faces["names"][first_match_index]
        
        names.append(name)
    
    return names
