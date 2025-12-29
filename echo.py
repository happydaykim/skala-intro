import password  # password.py 파일을 불러옵니다.

print("=== 에코 & 비밀번호 검증 프로그램 ===")
print("조건: 6자리 이상, 영문/숫자/특수문자 포함")
print("종료하려면 '!quit'을 입력하세요.")
print("-" * 40)

while True:
    user_sentence = input("비밀번호 입력: ")

    # 1. 종료 조건 확인
    if user_sentence == '!quit':
        print("프로그램을 종료합니다.")
        break

    # 2. 비밀번호 유효성 검사 (password 모듈 사용)
    if password.validate(user_sentence):
        # 조건 만족 시 에코(그대로 출력)
        print(f"-> [성공] 입력하신 비밀번호는 사용 가능합니다: {user_sentence}")
    else:
        # 조건 불만족 시 경고 메시지
        print("-> [실패] 유효하지 않은 비밀번호입니다. (영문+숫자+특수문자, 6자리 이상)")
    
    print("-" * 40)