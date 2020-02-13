# list = ['a', 'b', 'c']
# for i in list:
#     print(i)

# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a:
#     print(first + last)

# marks = [90, 24, 65, 44, 98]
# for number in range(len(marks)):
#     if marks[number] < 60:
#         continue
#     print("%d번 학생 합격입니다." % (number+1))

# number = 0
# for mark in marks:
#     number = number + 1
    # if mark >= 60:
    #     print("%d번 학생은 합격입니다." % number)
    # else:
    #     print("%d번 학생은 불합격입니다." % number)
    # if mark < 60:
    #     continue
    # print("%d번 학생은 합격입니다." % number)

# add = 0
# for i in range(1, 11):
#     add = add + i
# print(add)

#구구단
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i*j, end=" ") # end=" " 를 넣어준 이유는 for문이 끝나기 전에 줄바뀌는것 방지
#     print('')

# a = [1,2,3,4]
# result = []
# for num in a:
#     result.append(num*3)
# result = [num * 3 for num in a]
# print(result)
# result = [num * 3 for num in a if num % 2 == 0]
# print(result)
# [표현식 for 항목1 in 반복가능객체1 if 조건문1
#         for 항목2 in 반복가능객체2 if 조건문2
#         ...
#         for 항목n in 반복가능객체n if 조건문n]

