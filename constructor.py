class a:
    def __init__(self):
        self.x=1
        self.__y=1

    def getY(self):
            return self.__y
ab=a()
a.__y=45
print(ab.getY())
