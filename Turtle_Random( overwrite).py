import turtle
import random
import os
from datetime import datetime
from PIL import Image

# ====== 核心配置 ======
save_folder = r"E:\DOCUMENTS\Pictures\Turtle Graphics"  # 直接使用原始字符串路径

file_prefix = "art_"  # 文件名前缀
for i in range(10):
    # ====== 路径预处理 ======
    # 自动创建目标目录（如果不存在）
    if not os.path.exists(save_folder):
        os.makedirs(save_folder, exist_ok=True)  # exist_ok=True 防止多线程竞争报错

    # 生成唯一文件名（日期+随机码）
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    random_suffix = f"{random.randint(1000,9999):04d}"  # 4位随机数防碰撞
    filename = f"{file_prefix}{timestamp}_{random_suffix}"

    # ====== 绘图引擎 ======
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)

    # 增强型随机绘图算法，直线

    # 随机颜色
    colors1 = ["#"+''.join(random.choices('0123456789ABCDEF', k=6)) for _ in range(8)]  # 生成随机HEX颜色
    # 三原色
    colors2 = ["red", "blue", "green"]
    for _ in range(250):
        t.color(random.choice(colors1))
        t.pensize(random.randint(3, 15))
        t.forward(random.randint(20, 100))
        t.right(random.choice([-180, -90, 0, 90, 180]))
        if random.random() < random.random():  # 30%概率抬起画笔
            t.penup()
            t.goto(random.randint(-300,300), random.randint(-300,300))
            t.pendown()

    # ====== 智能保存系统 ======
    try:
        # 矢量图保存
        ps_path = os.path.join(save_folder, f"{filename}.ps")
        screen.getcanvas().postscript(file=ps_path, colormode='color')
        
        print(f"文件保存成功！\n矢量图：{ps_path}")

    except PermissionError:
        print(f"错误：没有写入权限，请检查路径 {save_folder}")
    except Exception as e:
        print(f"保存失败：{str(e)}")
    turtle.done()