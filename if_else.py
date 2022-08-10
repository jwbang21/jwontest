# print(0)
# if True:
#     print(1)
# print(2)

# print('----')

# print(0)
# if False:
#     print(1)
# print(2)

# input_id = input('id : ')
# id = 'egoing'
# if input_id == id:
#     print('Welcome')
# else:
#     print('go away')

# input_name = input('name : ')
# name = 'bang'
# if input_name != name:
#     print('wrong')
# else:
#     print('짝짝짝')

# input_id = input('id : ')
# id1 = 'egoing'
# id2 = 'bang'
# if input_id == id1:
#     print('Welcome')
# elif input_id == id2:
#     print('Welcome')
# else:
#     print('Who?')

input_id = input('id: ')
id = 'egoing'
input_password = input('password: ')
password = '1111'
if input_id == id:
    if input_password == password:
        print('welcome')
    else:
        print('wrong password')
else:
    print('wrong id')