class GestureController:

    def __init__(self):
        pass

    def fingers_up(self, landmarks):

        fingers = []

        # Thumb
        if landmarks[4][1] > landmarks[3][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Fingers
        tips = [8, 12, 16, 20]

        for tip in tips:

            if landmarks[tip][2] < landmarks[tip - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    def detect_gesture(self, landmarks):

        if len(landmarks) == 0:
            return None

        fingers = self.fingers_up(landmarks)

        total = fingers.count(1)

        # ONE Finger = NEXT
        if fingers == [0,1,0,0,0]:
            return "NEXT"

        # TWO Fingers = PREVIOUS
        elif fingers == [0,1,1,0,0]:
            return "PREVIOUS"

        # FIVE Fingers = START
        elif total == 5:
            return "START"

        return None