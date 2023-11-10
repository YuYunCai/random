import random
import xml.etree.ElementTree as ET

# 函數：從XML文件讀取遊戲設定
def load_game_settings(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    x1 = int(root.find('x1').text)
    x2 = int(root.find('x2').text)
    n = int(root.find('n').text)
    return x1, x2, n

# 函數：開始遊戲
def start_game(x1, x2, n):
    target_number = random.randint(x1, x2)
    attempts = 0

    print(f"猜一個介於 {x1} 和 {x2} 之間的數字!")

    while attempts < n:
        guess = int(input("你的猜測："))

        if guess < target_number:
            print("太低了！")
        elif guess > target_number:
            print("太高了！")
        else:
            print("恭喜，你猜對了！")
            break

        attempts += 1

    if attempts == n:
        print(f"你已經猜了{n}次，遊戲結束。目標數字是{target_number}。")

# 主函數
def main():
    x1, x2, n = load_game_settings('game_settings.xml')
    start_game(x1, x2, n)

# 程式入口點
if __name__ == "__main__":
    main()