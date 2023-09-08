import sys
import datetime
import hashlib

# hash('apple') = 1324654czxczxczdvzjkhfkjsdhf
# hash('banan') = asfdsf6+s46df4ds4f5sdff

#Classes
class Block(object):
    #Properties
    block_no = 0
    data = "G"
    next = None
    hash = None
    previous_hash = 0x0
    timestamp=0

    def __init__(self, data, block_no,timestamp): #Input arguments
        self.data = data
        self.block_no = block_no
        self.timestamp = datetime.datetime.now()

    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.block_no).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8')
        )
        return h.hexdigest()

    def str(self):
        return "--------------"+"\nBLOCK HASH: " + str(self.hash()) + "\nBLOCK NO: " + str(self.block_no) + "\nBLOCK DATA: " + self.data + "\nTIME STAMP: " + str(self.timestamp) +"\n--------------"


class Blockchain(object):

    diff = 20
    maxNonce = 2 ** 32
    target = 2 ** (256 - diff)

    chain = []
    chain.append(Block("Начало голосования", 1,0))

    def add(self, block):
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1
        self.block = self.block.next

    def mine(self, block):
        self.chain.append(block)


def main():
    menu()


def menu():


    print("\n\n***** Добро пожаловать в систему голосования на основе блокчейна *****")
    print()

    choice = input("""
                      A: Вход
                      B: Выход
                      Пожалуйста, выберите ваше действие: """)

    if choice == "A" or choice == "a":
        login()

    elif choice == "B" or choice == "b":
        print("\n********* Вы вышли из системы **********")
        sys.exit()

    else:
        print("Надо написать именно или A или B английскими буквами")
        print("Попробуйте еще")
        menu()


def login():
    print("\n\n************** Вы вошли на страницу авторизации ***************")
    print()

    id=input("\n Введите ваш уникальный цифровой номер:")


    if id == "1234": #Default ID
        vote()

    else:
        print("Вы ввели несуществующий цифровой номер")
        print("Попробуйте еще")
        menu()

def vote():
    print("\n\n************* Добро пожаловать на страницу голосования ***************")
    print()

    yvote = input("\n За кого вы хотите отдать свой голос:\n"
               "A. Иосиф Пригожин\n"
               "B. Евгений Пригожин\n"
               "Сделайте свой выбор:")


    if yvote == "A" or yvote == "a" or yvote == "B" or yvote == "b":
        if yvote == "A" or yvote == "a":
            vote_name = "Иосиф Пригожин"
        else:
            vote_name = "Евгений Пригожин"

        print("\n--------------")
        print("Ваш голос учтен. Подождите пока другие узлы соединятся....")
        print("--------------")
        print("Текущий блокчейн :")

        blockchain = Blockchain()

        block = Block(vote_name, len(blockchain.chain)+1,datetime.datetime.now())
        blockchain.mine(block)

        for id in range(len(blockchain.chain)):
            print(blockchain.chain[id].str()) #Prints blockchain details

        print("Длина цепи: ")
        print(len(blockchain.chain)) # Prints blockchain length

        print("\n--------------")
        print("\n Спасибо, вы успешно проголосовали и ваш результат был добавлен в блокчейн.")
        print("\n Вы перенаправляетесь на домашнюю страницу.")

        menu()

    else:
        print("Вы ввели некорректный вариант голосования")
        print("Попробуйте еще")
        vote()


main()