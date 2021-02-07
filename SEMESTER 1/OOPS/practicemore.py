class A:
    def __init__(self):
        self.j=10
        print("A")
class B:
    def __init__(self):
        print("B")
    def func(self):
        print("B")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("C")

obj = C()
obj.func()
print(obj.j)
print(C.__mro__)