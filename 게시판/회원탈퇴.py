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
        print('1. 회원 가입')
        print('3. 회원 탈퇴')
        print('4. 회원 목록')
        
        select_no = int(input('번호 입력: '))
        
        if select_no == 1:
            id_result = make_id(regist_user)
            if id_result:
                regist_user[id_result[0]] = id_result[1]
                print(regist_user)
                
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