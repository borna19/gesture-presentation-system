import cv2
import mediapipe as mp


class HandDetector:

    def __init__(self):

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.mpDraw = mp.solutions.drawing_utils

    def detect_hands(self, frame):

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(rgb_frame)

        if self.results.multi_hand_landmarks:

            for hand_landmarks in self.results.multi_hand_landmarks:

                self.mpDraw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mpHands.HAND_CONNECTIONS
                )

        return frame

    def get_landmark_positions(self, frame):

        landmark_list = []

        if self.results.multi_hand_landmarks:

            hand = self.results.multi_hand_landmarks[0]

            for id, landmark in enumerate(hand.landmark):

                h, w, c = frame.shape

                x = int(landmark.x * w)
                y = int(landmark.y * h)

                landmark_list.append([id, x, y])

        return landmark_list