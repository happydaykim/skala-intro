import re

def validate(user_input):
    """
    비밀번호 유효성을 검사하는 함수
    조건: 6자리 이상, 영문, 숫자, 특수문자 각 1개 이상 포함
    """
    
    # 정규표현식 설명:
    # ^                 : 문자열의 시작
    # (?=.*[a-zA-Z])    : (전방탐색) 최소 한 개의 영문자가 있는지 확인
    # (?=.*\d)          : (전방탐색) 최소 한 개의 숫자가 있는지 확인
    # (?=.*[^a-zA-Z0-9]): (전방탐색) 영문/숫자가 아닌 문자(특수문자)가 최소 한 개 있는지 확인
    # .{6,}             : 모든 문자가 6자리 이상이어야 함
    # $                 : 문자열의 끝
    
    pattern = r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{6,}$'
    
    # 패턴과 입력값이 일치하면 Match 객체(True 취급), 아니면 None(False 취급) 반환
    if re.match(pattern, user_input):
        return True
    else:
        return False