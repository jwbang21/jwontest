def make_id(regist_user):
    regist_id = []
    while True:
        uid = str(input('회원 아이디: '))
        if uid in regist_user:
            print('등록된 id')
        else:
            regist_id.append(uid)
            break
        
    while True:
        pwd = str(input('회원 비번: '))
        regist_id.append(pwd)
        break
    return regist_id

def edit_password(uid, pwd):
    n_pwd = ''
    while True:
        pw = str(input('새로운 비밀번호 입력: '))
        if pw == pwd:
            print(f'기존 비번하고 같습니다.')
            continue
        else:
            n_pwd = pw
            break
    print(f'id: {uid}, n_pwd: {n_pwd}')
    return uid, n_pwd

def delete_user(regist_user, uid2):
    if uid2 in regist_user:
        del regist_user[uid2]
        print('탈퇴')
    else:
        print('실패')
    
def main():
    regist_user = {'ID' : 'PASSWORD'}
    menu = True
    
    while menu:
        print('')
        print('1. 회원 가입')
        print('2. 회원 비번 변경')
        print('3. 회원 탈퇴')
        print('4. 회원 목록')
        print('')
        
        select_no = int(input('번호 입력: '))
        
        if select_no == 1:
            id_result = make_id(regist_user)
            if id_result:
                regist_user[id_result[0]] = id_result[1]
                print(regist_user)
                continue
            
        if select_no == 2:
            uid = str(input('회원 아이디: '))
            if uid in regist_user:
                print(f'{regist_user}')
                n_pwd = edit_password(uid, regist_user[uid])
                regist_user[uid] = n_pwd
                print('비밀번호 변경 완료 \n')
            else:
                print('등록된 아이디가 아닙니다.\n')
                continue
            
        if select_no == 3:
            uid2 = str(input('회원 아이디: '))
            if uid2 in regist_user:
                delete_user(regist_user, uid2)
            else:
                print('가입된 아이디가 아닙니다.\n')
                continue
        
        if select_no == 4:
            for uid, pwd in regist_user.items():
                print(f'id: {uid}, pw: {pwd}')
            print()
                
main()