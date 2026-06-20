import pyautogui


class PresentationController:

    def __init__(self):
        pass

    def execute_action(self, gesture):

        if gesture == "NEXT":

            pyautogui.press("right")

        elif gesture == "PREVIOUS":

            pyautogui.press("left")

        elif gesture == "START":

            pyautogui.press("f5")