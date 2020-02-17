class Bird:
    def fly(self):
        raise NotImplementedError
    #상속받는 클래스는 fly 함수를 구현해야만 한다

# class Eagle(Bird):
#     pass
#
# eagle = Eagle()
# eagle.fly()  # NotImplementedError 출력됨.


class Eagle(Bird):
    def fly(self):
        print("flying")


eagle = Eagle()
eagle.fly()



