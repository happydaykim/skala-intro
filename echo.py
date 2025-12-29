print("프로그램을 시작합니다. '!quit'을 입력하면 종료됩니다.")

while True:
    user_sentence = input("문장을 입력하세요: ")

    if user_sentence == '!quit':
        print("프로그램을 종료합니다.")
        break

    print(f"입력하신 문장: {user_sentence}")