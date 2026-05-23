# wap accessing private method through a public method
class ishu:
    def public_method(self):
        print("THis is public method")
        self.__private_method()

    def __private_method(self):
        print("this is priavte method")

obj= ishu()
obj.public_method()