import cv2
import pyscreenshot as ImageGrab
import numpy as np

def scan_qrcode_windows():

    # 截取屏幕截图
    img = ImageGrab.grab()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # 初始化二维码检测器
    detector = cv2.QRCodeDetector()

    # 检测并解码二维码
    data, vertices_array, _ = detector.detectAndDecode(img)

    if vertices_array is not None:
        print("二维码内容：", data)
    else:
        print("未检测到二维码")
