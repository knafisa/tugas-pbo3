class Sample:
    gamma = 0 #class variable
    def __init__(self):
        self.alpha = 1 #instance variable
        self.__delta = 3 #private

obj = Sample()
obj.beta = 2 #instance variable yg hanya ada pada "obj" instance
print(obj.__dict__) 