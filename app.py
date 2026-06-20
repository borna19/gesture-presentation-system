import cv2
import time

from hand_detector import HandDetector
from gesture_controller import GestureController
from presentation_control import PresentationController


cap = cv2.VideoCapture(0)

detector = HandDetector()

gesture = GestureController()

presentation = PresentationController()

last_action_time = 0

cooldown = 1


while True:

    success, frame = cap.read()

    frame = cv2.flip(frame, 1)

    frame = detector.detect_hands(frame)

    landmarks = detector.get_landmark_positions(frame)

    current_gesture = gesture.detect_gesture(landmarks)

    current_time = time.time()

    if current_gesture:

        cv2.putText(
            frame,
            f"Gesture: {current_gesture}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        if current_time - last_action_time > cooldown:

            presentation.execute_action(current_gesture)

            last_action_time = current_time

    cv2.imshow("Gesture Presentation Controller", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break


cap.release()

cv2.destroyAllWindows()