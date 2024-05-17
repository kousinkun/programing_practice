import random

nenrei = random.randint(0, 100)

if 0 < nenrei < 19:
    print('未成年です。\n 地方自治体によっては医療費が￥200のところも')
elif 20< nenrei < 59:
    print('成年です。\n 飲酒運転禁煙は控えめに')
elif 60 < nenrei < 100:
    print('定年後も元気100％で過ごして下さい')