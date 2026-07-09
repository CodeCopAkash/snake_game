class Animal:
    def __init__(self):
        self.eye = 2
        self.nose = 1
    @staticmethod
    def breathe():
        print("Inhale, Exhale")

class Fish(Animal):

    def __init__(self):
        super().__init__()

    @staticmethod
    def swim():
        print("I am under the water swimming")

nemo = Fish()
nemo.swim()
print(nemo.eye)
print(nemo.nose)

