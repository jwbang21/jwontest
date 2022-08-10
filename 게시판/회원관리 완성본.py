import re

def chk_id (id):
    result = True
    reg = r'^[A-Za-z0-9_]{4,20}$'
    if not re.search(reg, id):
        print('아이디 생성 기준에 부적당하다.')
        result = False
    return result

def chk_password(pwd):
    result = True
    reg = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%&*?])[A-Za-z\d!@#$%&*?]{8,20}$'
    if not re.search(reg,pwd):
        print('비밀번호 기준에 부적당하다.')
        result = False
    return result

def make_id(regist_user):
    regist_id = []
    while True:
        uid = str(input('회원 아이디 입력: '))
        if uid in regist_user:
            print('이미 등록된 id입니다.')
            ex = input('메인 화면으로 이동하시겠습니까?')
            if ex == 'y' or ex == 'Y':
                return False
            else:
                continue
        else:
            res_id = chk_id(uid)
            if not res_id:
                continue
            else:
                regist_id.append(uid)
                break
            
    while True:
        pwd = str(input('비밀번호 입력: '))
        res_pwd = chk_password(pwd)
        if not res_pwd:
            continue
        else:
            regist_id.append(pwd)
            break
    return regist_id

def edit_password(uid, pwd):
    n_pwd = ''
    while True:
        pw = str(input('새로운 비밀번호 입력: '))
        if pw == pwd:
            print(f'기존 비번하고 같음')
            continue
        else:
            res_pwd = chk_password(pw)
            if not res_pwd:
                continue
            else:
                n_pwd = pw
                break
    print(f'id:{uid}, n_pwd:{n_pwd}')
    return uid, n_pwd

def main():
    regist_user = {'ID' : 'PASSWORD'}     # regist_user라는 변수에 앞으로 회원 정보를 담을 것으로 보이고, 형식은 { : }으로 보인다.
    sw = True       # sw를 선택하면 True이다라는 의미인 것같다. sw에서 제시한 번호를 선택을 하면 아래의 코드를 수행할 수 있게 만드는 기초작업인것 같다.
    
    while sw:
        print('-----------------------------')
        print('1. 회원 아이디 생성')
        print('2. 비밀번호 변경')
        print('3. 전체 회원 아이디 목록 보기')
        print('4. 종료')
        print('-----------------------------\n')
        
        select_no = int(input('번호 선택(1~4): '))     # '번호 선택'이라는 문구를 통해 input값을 받으면서 그 값은 정수여야 한다는 int 조건을 포함시켜주었다.
        
        if select_no == 1:      # input 값으로 1을 받았다면 수행하게 되는 작업이다.
            id_result = make_id(regist_user)        # id_result는 만든 id 결과물을 저장하는 변수인것 같고, 
            if id_result:
                regist_user[id_result[0]] = id_result[1]
                print(regist_user)
                
        if select_no == 2:
            uid = str(input('회원 아이디 : '))      # 회원 아이디를 입력하게 되면 uid라는 변수로 들어가게 된다.
            if uid in regist_user:      # uid에 들어온 회원 아이디가 regist_user에 속해있다면,
                print(f'{regist_user}')     # 처음에 입력했던 회원 아이디(uid)와 회원 아이디 비번을 함께 보여준다.
                n_pwd = edit_password(uid, regist_user[uid])        # 새로운 패스워드(n_pwd)
                regist_user[uid] = n_pwd
                print('비밀번호 변경 완료!\n')
            else:
                print('등록된 아이디가 아닙니다.\n')
                continue
            
        if select_no == 3:
            for uid, pwd in regist_user.items():
                print(f'id: {uid} / pw: {pwd}')
            print()     # 위에 print를 끝나고 한줄 띄우기 위해 실행한다.
            
        if select_no == 4:
            sw = False

main()

# def make_id(regist_user):
#     regist_id = []      # regist_id 리스트에 만들어진 id와 password들의 회원정보가 담길 것이다.
#     while True:
#         uid = str(input('회원 아이디 입력 : '))
#         if uid in regist_user:      # 'regist_user에 입력값에 입력했던 uid가 있다면' 이라는 가정을 의미한다.
#             print('이미 등록된 id입니다.')      # 등록되었다고 출력한다.
#             ex = input('메인 화면으로 이동하시겠습니까? (y/n): ')       # 출력하게되면 메인 화면으로 이동할지에 대한 질문을 던진다.
#             if ex == 'y' or ex == 'Y':      # 만약 y라고 답하게 된다면,
#                 return False        # return이 false이므로 make_id 함수 자체를 false 한다는 의미이므로 main에서의 make_id 뒤에 나오는 코드를 실행하지 않고, 메인 화면으로 이동하게 된다.
#             else:
#                 continue            # ex의 대답이 y가 아니라면, main에서의 make_id 뒤에 나오는 코드를 실행하게 된다.
#         else:                       # 유효성 체크를 위해서 필요한 코드로 보인다.
#             res_id = chk_id(uid)
#             if not res_id:
#                 continue
#             else:
#                 regist_id.append(uid)
#                 break
#     while True:
#         pwd = str(input('비밀번호 입력 : '))
#         res_pwd = chk_password(pwd)
#         if not res_pwd:
#             continue
#         else:
#             regist_id.append(pwd)   # append가 요소 마지막에 추가한다는 의미이므로 저장된 비밀번호를 맨 마지막 요소에 저장한다는 의미이다.
#             break
#     return regist_id        # return값이 regist_id라는 의미는, make_id의 처음에 선언해준 regist_id의 리스트로 돌아가게 된다.


# import re

# def chk_id(id):
#     result = True
#     reg = r'^[A-Za-z0-9_]{4,20}$'
#     if not re.search(reg, id):
#         print('아이디 생성 기준에 부적당합니다!')
#         result = False
#     return result

# def chk_password(pwd):
#     result = True
#     reg = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%&*?])[A-Za-z\d!@#$%&*?]{8,20}$'
#     if not re.search(reg, pwd):
#         print('비밀번호 기준에 부적당하다!')
#         result = False
#     return result

# def edit_password(uid, pwd):
#     n_pwd = ''
#     while True:
#         pw = str(input('새로운 비밀번호 입력 : '))
#         if pw == pwd:
#             print(f'기존 비번하고 같음!')
#             continue
#         else:
#             res_pwd = chk_password(pw)
#             if not res_pwd:
#                 continue
#             else:
#                 n_pwd = pw
#                 break
#     print(f'id:{uid}, n_pwd:{n_pwd}')
#     return uid, n_pwd
