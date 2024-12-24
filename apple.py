import io
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, Response

app = Flask(__name__)

def create_pingan_guo():
    # 创建一个画布
    fig, ax = plt.subplots(figsize=(6, 6))

    # 绘制平安果的外形，使用椭圆形状
    ellipse = plt.Circle((0.5, 0.5), 0.4, color='red', ec='darkred', lw=2, zorder=2)
    ax.add_artist(ellipse)

    # 绘制平安果的叶子
    leaf1 = plt.Polygon([(0.5, 0.9), (0.6, 1.1), (0.7, 0.9)], closed=True, color='green', zorder=3)
    leaf2 = plt.Polygon([(0.5, 0.9), (0.4, 1.1), (0.3, 0.9)], closed=True, color='green', zorder=3)
    ax.add_artist(leaf1)
    ax.add_artist(leaf2)

    # 绘制一些细节：例如果实上的光泽或图案
    ax.text(0.5, 0.5, "平安果", color="white", ha="center", va="center", fontsize=20, zorder=4)

    # 设置图形显示的范围和样式
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')  # 关闭坐标轴

    # 将图像保存为 PNG 格式并通过 Flask 返回
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches='tight', pad_inches=0)
    buf.seek(0)
    return buf

@app.route('/')
def pingan_guo_image():
    img = create_pingan_guo()
    return Response(img, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
