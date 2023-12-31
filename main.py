import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Capture video from webcam
cap = cv2.VideoCapture(0)


def activate_shocker():
    print("Shocker activated")
    with open("D:\\shocker.txt", "w") as f:
        f.write("get shocked mf")


def main():
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # calculate TOO_LOW based on the height of the frame
        frame_height, frame_width, _ = frame.shape
        TOO_LOW = int(frame_height * 0.25)

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        if len(faces) == 0:
            continue

        # find the largest face (i.e. the one closest to the camera, the computer user)
        face = max(faces, key=lambda f: f[2])

        (x, y, w, h) = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        for _x, _y, _w, _h in faces:
            if (_x, _y, _w, _h) != (x, y, w, h):
                cv2.rectangle(frame, (_x, _y), (_x + _w, _y + _h), (0, 255, 0), 2)

        # Draw the line at TOO_LOW
        cv2.line(frame, (0, TOO_LOW), (frame_width, TOO_LOW), (0, 0, 255), 2)

        # Check if the face is too low
        if y > TOO_LOW:
            print("Face is too low")
            activate_shocker()

        # Display the frame
        cv2.imshow("Frame", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
