import os
import platform

from qrcodeMaker import qrcodeMake
from scanner_windows import scan_qrcode_windows
from scanner_app import scan_qrcode_app


def main():

        systemName = platform.system()

        while True:
            print("请选择一个功能:")
            print("1. 生成二维码")
            print("2. 扫描二维码")
            print("3. 退出")
            choice = input("请输入选项 (1/2/3): ")

            if choice == '1':
                qrcodeMake()
            elif choice == '2':
                if systemName == 'Linux' or systemName == 'Darwin':
                    scan_qrcode_app()
                elif systemName == 'Windows':
                    scan_qrcode_windows()
            elif choice == '3':
                break
            else:
                print("无效的选项，请重新选择")

            input('按enter键继续...')
            os.system('cls')




if __name__ == "__main__":
    main()
