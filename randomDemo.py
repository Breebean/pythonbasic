import random

# a = random.random() #0.0~1.0 사이의 실수 중 난수를 돌려줌

# b = random.randint(1, 10) #1~10 사이의 정수 중 난수를 돌려줌


def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)


if __name__ == "__main__":  #만일 이 파일이 인터프리터에 의해 실행되는 경우에 실행됨
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))


def random_pop2(data):
    number = random.choice(data)
    data.remove(number)
    return number
