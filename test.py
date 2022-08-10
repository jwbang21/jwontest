# from email import message
# from logging.handlers import BaseRotatingHandler


# name = 'bang'
# message = 'hi ' + name + ' ... bye ' + name + '.'
# print(message)

# s1 = set([1,2,3,1,2,3])
# print(s1)

# s2 = 1,2,3,1,2,3
# print(s2[5])

# me = ['방지원', 27, '남자', 177]
# print(me[0])

# me = ['방지원', 27, '남자', 177]
# me[1] = 17
# print(me)


# def add(a,b):
#     return a+b
# print(add(4,5))

# user_list = ['이세진','지원','예진']
# product = 'book'

# print(f'{user_list[0]} 님이 {product} 을 삿습니다 ')

# a = "!!!"
# string = "Python"

# print(f'{a}{string}{a}')

# a = [1,2,3,4,5,6,7,8,9,10]
# print(a[2:4])

# a = [1,2,['a','b']]
# print(a[2][0])

# a = [1,2,['a','b',['Life', 'is']]]
# print(a[2][2][1])

# a = [1,2,3,4,5]
# print(a[1:3])

# a = [1,2,3]
# print(str(a[2]) + 'hi')

# a = [1,2,3]
# a.append([5,6])
# print(a)

# dic_user = ([('name','홍길동'), ('birth','1128'), ('age','30')])
# print(dic_user)

# dic = {'name':'홍길동', 'birth':'1128', 'age':'30'}
# print(dic)

# s2 = set('hello')
# print(s2)

# s1 = set([1,2,3])
# S1 = list(s1)
# print(S1)

# a = [1,2,3]
# b = a
# b = a[:]        # 이부분이 여기에 올지
# a[1] = 4
#                 # 여기에 올지에 따라서 달라진다.
# print(a)
# print(b)

# a = [1,2,3,4]
# print(id(a))
# b = a
# print(id(b))
# print(b)
# print(b is a)

# money = 5000
# card = True
# if money >= 30000 or card:
#     print("texi")
# else:
#     print("walk")

# pocket = ['phone', 'paper', 'money']
# if 'money' in pocket:
#     print('택시')
# else:
#     print('걷는다')

# pocket = ['phone']
# if 'money' in pocket:
#     print('택시')
# elif 'card' in pocket:
#     print('택시')
# else:
#     print('걸어가라')

# pocket = ['phone']
# card = False
# if 'money' in pocket:
#     print('택시')
# elif card:
#     print('택시')
# else:
#     print('걸어가라')

# treehit = 0
# while treehit < 10:          # treehit이 10보다 작을때까지 수행한다.
#     treehit = treehit + 1    # 9가 되면 10보다는 작으므로 treehit + 1을 수행할 수 있게된다.
#     print('나무를 %d번 찍었습니다.' %treehit)
#     if treehit == 10:       #10이 되면 while문 조건이랑 맞지 않으므로 중단되고, 나무가 넘어간다는 출력이 나오게 된다.
#         print('나무가 넘어갑니다.')

# prompt = """        
# 1. Add
# 2. Del
# 3. List
# 4. Quit
# Enter number : """  # 데이터가 길어질 때, """와 """ 사이에 작성할 수 있도록 한다.

# number = 0          # 0부터 시작하겠다는 의미
# while number != 4:  # 4가되면 멈추겠다는 의미
#     print(prompt)   # 위에서 지정해준 prompt를 출력하게 된다.
#     number = int(input())   # 사용자의 숫자 입력을 받아들이는 것을 의미

# coffee = 10
# while True:
#     money = int(input('돈을 넣어주세요 : '))
#     if money == 500:
#         print('커피가 나옵니다.')
#         coffee = coffee - 1
#         print('남은 커피는 %d개 입니다.' % coffee)
#     elif money > 500:                     # 500이상을 넣을때 구현된다.
#         print('거스름돈 %d원을 드립니다. 커피가 나옵니다' %(money - 500))
#         coffee = coffee - 1
#         print('남은 커피는 %d개 입니다.' % coffee)
#     else:                                # 500미만 일때 구현된다.
#         print('%d원을 돌려드립니다. 커피를 주지 않습니다.' % money)
#         print('남은 커피는 %d개 입니다.' % coffee)
#     if coffee == 0:                      # 남은 커피수가 0이 되면 중단하는 경우이다.
#         print('중단')
#         # break                            # 강제로 중단하고 빠져나올때 쓸 수 있다.
    
# a = 0               # a가 0부터 시작해서
# while a < 10:       # 10까지 될때까지 반복할 것이다라는 의미
#     a = a + 1       # 한번 사이클이 돌면 a는 +1을 해서 증가할 것이다라는 의미
#     if a % 3 == 0: continue     # 3의 배수는 제외시키는 것이므로 3으로 나눴을 때 0이 되는 것은 제외한다. 또한 continue를 사용함으로써 한번으로 끝나는게 아니라 다시 올라가서 a가 10을 안넘을 때까지 반복한다는 의미이다.
#     print(a)

# num_list = [100, 200, 500, 10000]
# for num in num_list:        # 변수를 num이라 두고 num_list라는 리스트의 숫자를 가져오는 기본적인 방법이다.
#     print(num)

# score = [90,25,67,45,80]
# for i in score:
#     if i > 60:
#         print('합격')
#     else:
#         print('불합격')

# score = [90,25,67,45,80]
# number = 0      # 0은 90을 가리키고, 1은 25를 가리킨다.
# for i in score:
#     number = number + 1     # 0이 대입되면 1이 되므로 결론은 1번이 90이 된다.
#     if i >= 60:
#         print('%d번 학생 합격입니다.' % number)
#     else:
#         print('%d번 학생 불합격입니다.' % number)

# sum = 0
# for i in range(1,101):  # 100까지니깐 range를 101까지 해야된다.
#     sum = sum + i   # sum이 0부터이므로 범위안에 있는 숫자가 계속해서 더해질 수 있는 구조이다.
# print(sum)

# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j, end = " ")
#     print('')

# 1부터 1000까지의 자연수 중 3의 배수의 합?
# sum = 0
# i = 1
# while i <= 1000:
#     if i % 3 == 0:
#         sum += i
#     i += 1
# print(sum)

# for i in range(1,101):
#     print(i)

# 70,60,55,75,95,90,80,80,85,100
#평균점수
# sum = 0
# score = [70,60,55,75,95,90,80,80,85,100]
# for i in score:
#     sum += i
#     average = sum / len(score)
# print(average)

# def sum(a,b):
#     return a + b

# a = 3
# b = 2
# print(sum(a,b))

# def add(*args):
#     finish = 0
#     for i in args:
#         finish += i
#     return finish

# finish = add(1,2,3,4,5)
# print(finish)

# def say(nick):
#     if nick == '바보':
#         return
#     print('나의 별명은 %s입니다.' % nick)

# say('야호')

# def say(num):
#     if num == 0:
#         return
#     print('나의 비밀번호는 %d 입니다.' % num)

# say(123)

# def my(name, age, man=True):
#     print("나의 이름은 %s입니다." %name)
#     print('나이는 %d살 입니다.' %age)
#     if man:
#         print('남자입니다.')
#     else:
#         print('여자입니다.')

# my('방지원', 27, True)
# my('방지원', 27, 'man')
# my('방지원', 27)

# a = 1
# def vartest(a):
#     a = a + 1
#     return a
    
# a = vartest(a)
# print(a)

# number = input('숫자를 입력하세요.')
# print('입력하신 숫자는 :',number)

# file = open('새파일.txt', 'w')
# for i in range(1,11):
#     data = '%d번째 줄입니다.\n' % i
#     file.write(data)
# file.close()

# file = open('새파일.txt', 'a')
# for i in range(11,13):
#     data = '%d번째 줄입니다.\n' % i
#     file.write(data)
# file.close()

# file = open('새파일.txt', 'r')
# print(file.read())
# file.close()

# with open('파일 이름', '파일 열기 모드') as file:

# 숫자 4자리를 입력받고 , 
# 천의 자리수와 1의 자리수에 +1 을 한 뒤 백의 자릿수와 십의 자리수의 위치를 변경하는 프로그램을 생성하시오

# 320으로 나눈 나머지를 출력하시오
# num = int(input('숫자 입력'))
# a = num // 1000
# b = (num // 100) % 10 
# c = (num // 10) % 10
# d = (num // 1) % 10
# x = a*1000 + b*100 + c*10 + d
# print(x)
# e = (a+1)*1000
# f = b*10
# g = c*100
# d1 = d + 1
# x1 = e + g + f + d1
# print(x1)
# print(x1 % 320)


# from datetime import datetime
# print(datetime.today())

# import datetime
# dt_now = datetime.datetime.now()
# print(dt_now.date())

# data=[10,20,30,40]
# for i, dt in enumerate(data):
#    if i%2 == 0:
#        continue
#    print(dt, end="") 

a = {'qw' : 'er'}
print(type(a))