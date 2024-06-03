

import qrcode
from PIL import Image


def qrcodeMake():

    text = input("请输入一段文字: ")
    stuId = input("请输入学号: ")
    stuName = input("请输入姓名: ")

    # 组合信息
    combined_data = f"{text}\n学号: {stuId}\n姓名: {stuName}"

    # 创建二维码对象
    qr = qrcode.QRCode(
        version=1,  # 版本 1 是最小的二维码版本，适用于少量数据
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # 误差修正等级
        box_size=10,  # 每个格子的像素大小
        border=4,  # 边框宽度，单位是格子
    )

    # 添加数据到二维码
    qr.add_data(combined_data)
    qr.make(fit=True)

    # 创建二维码图像
    img = qr.make_image(fill='black', back_color='white')

    # 保存图像到文件
    img_filename = "student.png"
    img.save(img_filename)

    print(f"二维码已生成并保存为 {img_filename}")
