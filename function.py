# def add(a, b):
#     return a + b
# result = add(1, 2)
# add = lambda(a, b):a + b
# result = add(1, 2)   #람다 활용

# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i
#     return result
#
# result = add_many(1,2,3,4,5,6,7)
# print(result)

# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result
#
# result = add_mul('add', 1,2,3,4,5)
# print(result)
# result = add_mul('mul', 1,2,3,4,5)
# print(result)

# def print_kwargs(**kwargs):     #key = value 형태의 결과값이 딕셔너리로 저장됨
#     print(kwargs)
#
# print_kwargs(a=1)
# print_kwargs(name='foo', age=3)

# def add_and_mul(a,b):
#     return a+b, a*b #파이썬에서 함수는 return을 만나면 함수를 빠져나옴
#
# result = add_and_mul(3,4) #두개의 결과를 튜플값으로 합쳐서 리턴해줌
# result1, result2 = add_and_mul(3,4) #결과값을 두개로 받고 싶으면 이렇게 하면 됨

# def say_myself(name, old, man=True):    #초기값은 항상 매개변수의 마지막에 위치
#     print("My name is %s." % name)
#     print("I'm %d years old." % old)
#     if man:
#         print("I'm a man.")
#     else:
#         print("I'm a woman.")
#
# say_myself("Glen", 29)

