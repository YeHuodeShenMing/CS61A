import random

def get_user_choice():
    user_choice = input("请选择（石头/剪刀/布）：")
    return user_choice.lower()

def get_computer_choice():
    choices = ["石头", "剪刀", "布"]
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "平局！"
    elif (user == "石头" and computer == "剪刀") or (user == "剪刀" and computer == "布") or (user == "布" and computer == "石头"):
        return "你赢了！"
    else:
        return "计算机赢了！"

def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"你选择了：{user_choice}")
    print(f"计算机选择了：{computer_choice}")
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    main()
