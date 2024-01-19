#1
# class auto:
#     def __init__(self, logo, speed):
#         self.logo = logo
#         self.speed = speed

#     def __init__(self):
#         print(f"nazva {self.logo} spid {self.speed} km/h")

#     def __init__(self, nospeed):
#         self.speed = nospeed
#         print(f"spid now {self.logo}: {self.speed} km/h")


# auto = ("Aydi",300)
# auto.__init_subclass__()
# print(auto)



#2

# class auto:
#     def __init__(self, model, year, speed):
#         self.model = model
#         self.year = year
#         self.speed = speed

#     def count_speed(self):
#         return self.speed


# class speed_auto(auto):
#     def __init__(self, model, year, speed, level_sport):
#         super().__init__(model, year, speed)
#         self.level_sport = level_sport


# auto = speed_auto("BMW", 2023, 200, 20)
# print(auto.count_speed())


#3
# class Book:
#     def __init__(self, title, author, year_of_publication):
#         self.title = title
#         self.author = author
#         self.year_of_publication = year_of_publication

#     def info(self):
#         print(f"Book '{self.title}', author: {self.author}, year of publication: {self.year_of_publication}")


# book = Book("2018", "Vasil_Suxomlunsky", 1949)
# book.info()

#4
# class Fruit:
#     def __init__(self, fruit):
#         self.fruit = fruit

# class Apple(Fruit):
#     def __init__(self, fruit, gala):
#         super().__init__(fruit)
#         self.gala = gala

#     def info(self):
#         return f"Це яблуко сорту {self.gala}."

# class Banan(Fruit):
#     def __init__(self, fruit, yellow):
#         super().__init__(yellow)
#         self.yellow = yellow

#     def info(self):
#         return f"Це банан кольору {self.yellow}."

# apple = Apple("Червоне яблуко", "Гала")
# banan = Banan("Джамбо-банан", "жовтий")

# print(apple.info())
# print(banan.info())


#5
# class Bank_raxynok:
#     def __init__(self, number_raxynok, start_balance=0):
#         self.number_raxynok = number_raxynok
#         self.__balance = start_balance

#     def have_balance(self):
#         return self.__balance

#     def plus_money(self, syma):
#         self.__balance += syma

#     def take_money(self, syma):
#         if syma <= self.__balance:
#             self.__balance -= syma
#         else:
#             print("Недостатньо коштів на рахунку.")

# paxynock = Bank_raxynok("123456789", 1000)
# print("Початковий баланс:", paxynock.have_balance())
# paxynock.plus_money(500)
# print("Баланс після додавання грошей:", paxynock.have_balance())
# paxynock.take_money(300)
# print("Баланс після зняття грошей:", paxynock.have_balance())




#6
# class zoo:
#     def __init__(self, name):
#          self.name = name

#     def speak(self):
#          pass



# class crocodal(zoo):
#      def speak(self):
#          return f"{self.name} ar ar ar"



# class zurafa(zoo):
#     def speak(self):
#          return f"{self.name} ps ps ps ps"



# crocodal_instance = crocodal("ponchik")
# zurafa_instance = zurafa("lemon")

# print(crocodal_instance.speak())
# print(zurafa_instance.speak())



#додаткове завдання

# number = float(input("Введіть число: "))
# dorivhye = number ** 2
# print(f"Квадрат числа {number} дорівнює {dorivhye}")