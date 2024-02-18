from pynput import mouse, keyboard
import time
import threading

class APMCalculator:
    def __init__(self):
        self.start_time = time.time()
        self.action_count = 0
        self.apm = 0

    def update_action(self):
        self.action_count += 1
        elapsed_time = time.time() - self.start_time
        self.apm = self.action_count / elapsed_time * 60  # Umrechnung in Aktionen pro Minute
        print(f"Current APM: {self.apm:.2f}")

    def on_press(self, key):
        self.update_action()

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.update_action()

    def run(self):
        # Tastatur-Listener starten
        keyboard_listener = keyboard.Listener(on_press=self.on_press)
        keyboard_listener.start()

        # Maus-Listener starten
        mouse_listener = mouse.Listener(on_click=self.on_click)
        mouse_listener.start()

        keyboard_listener.join()
        mouse_listener.join()

apm_calculator = APMCalculator()
apm_calculator.run()
