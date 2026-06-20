import unittest

from gesture_controller import GestureController


class GestureControllerTests(unittest.TestCase):
    def test_detect_gesture_returns_none_for_incomplete_landmarks(self):
        controller = GestureController()

        short_landmarks = [[0, 0, 0] for _ in range(5)]

        result = controller.detect_gesture(short_landmarks)

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
