class Asker:
    @staticmethod
    def askall(lst):
        for i in lst:
            i.report()

class Sender:
    count = 0
    @classmethod
    def report(cls):
        if cls.count == 0:
            print('Greetings!')
            cls.count += 1
        else:
            print('Get away!') 

lst = [Sender(), Sender(), Sender()]
Asker.askall(lst)

