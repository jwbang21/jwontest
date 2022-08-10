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
#         break                            # 강제로 중단하고 빠져나올때 쓸 수 있다.
    
a = 123
print(a)