import cv2
from simple_facerec import SimpleFacerec
a=""
l=[]
def face():
    global a
    global l
    # Encode faces from a folder
    sfr = SimpleFacerec() 
    sfr.load_encoding_images("images/")

    # Load Camera
    cap = cv2.VideoCapture(0)
    f=open("names.txt","w")


    while True:
        ret, frame = cap.read()
        global l

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            a=str(name)+"\n"
            if name not in l:
                f=open("names.txt","w")
                l=[]
                l.append(name)
                
                f.write(str(name)+"\n")
                f.close()
            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
        count=0
        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
face()