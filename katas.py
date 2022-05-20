from pip import main


class Unities:
    def __init__(self,name,age,email,password):
        self.name = name
        self.age = age
        self.Email = email
        self.Password = password
    
    def info(self):
        print(self.name)

if __name__ == "__main__":

    person = Unities("martin", 28, "martin@gmail.com", 11223322)
    person.info()