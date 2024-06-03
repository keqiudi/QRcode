import cv2

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics.texture import Texture


class qrcodeScanApp(App):
    def build(self):
        self.img1 = Image()
        layout = BoxLayout(orientation='vertical')
        self.result_label = Label(text="二维码内容将显示在这里")
        layout.add_widget(self.img1)
        layout.add_widget(self.result_label)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1.0 / 30.0)
        return layout

    def load_video(self, *args):
        ret, frame = self.capture.read()
        if ret:
            buffer = cv2.flip(frame, 0).tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
            self.img1.texture = texture
            self.detect_qr_code(frame)

    def detect_qr_code(self, frame):
        detector = cv2.QRCodeDetector()
        data, vertices_array, _ = detector.detectAndDecode(frame)
        if vertices_array is not None:
            self.result_label.text = "二维码内容：" + data

def scan_qrcode_app():
    scanner = qrcodeScanApp()
    scanner.run()

