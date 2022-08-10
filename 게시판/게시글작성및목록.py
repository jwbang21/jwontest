def id(uid):
    uid = str(input('회원 아이디: '))

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

# import datetime
# def write_user(uid):       # 게시글을 작성할 수 있는 것들
#     if 
#     print('작성되었습니다.')
    # i = {'날짜':dt_now.date(), '작성자':uid, '게시글':write}    # 날짜나오는게 마음에 안듬, 한줄씩 띄워서 나왔으면 좋겠음
    # dt_now = datetime.datetime.now()
    
# def write(write_list, write_one):
#     dt_now = datetime.datetime.now()
#     if write_one in write_list:
#         i = {'글제목':write_one , '글내용':write_two, '작성자':uid, '날짜':dt_now.date()}
#         print(i)
    # else:
    #     print('작성된 글이 없습니다.\n')

def delete_user(regist_user, uid2):
    if uid2 in regist_user:
        del regist_user[uid2]
        print('탈퇴')
    else:
        print('실패')

import datetime
from turtle import title
def main():
    regist_user = {'ID' : 'PASSWORD'}
    write_list = ['ti', 'no']
    menu = True
    
    while menu:
        print('-----------------')
        print('1. 회원 가입')
        print('2. 회원 비번 변경')
        print('3. 게시글 작성')
        print('4. 게시글 목록')
        print('5. 회원 탈퇴')
        print('6. 회원 목록')
        print('7. 종료')
        print('-----------------')
        
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
                print('가입된 아이디가 아닙니다.\n')
                continue
            
        if select_no == 3:
            write_no = []
            uid = str(input('아이디 입력: '))            
            if uid in regist_user:
                title = str(input('게시글 제목: '))
                note = str(input('게시글: '))
                write_no.append(title)
                print('작성되었습니다.')
                continue
            else:
                print('가입된 아이디가 아닙니다.\n')
                continue
        
        if select_no == 4:
            dt_now = datetime.datetime.now()
            # for i in write_list:
            #     print(i)
            #     break
            uid = str(input('아이디 입력: '))
            if uid in regist_user:
                print(f'글제목:{title}, 글내용:{note}, 작성자:{uid}, 날짜:{dt_now.date()}')
            else:
                print('게시물을 볼 수 없습니다.')
                continue
                
        if select_no == 5:
            uid2 = str(input('회원 아이디: '))
            if uid2 in regist_user:
                delete_user(regist_user, uid2)
            else:
                print('가입된 아이디가 아닙니다.\n')
                continue
        
        if select_no == 6:
            for uid, pwd in regist_user.items():
                print(f'id: {uid}, pw: {pwd}')
            print()
            
        if select_no == 7:
            menu = False
                
main()