import json


class Persons:
    Data = dict()

    def Jason_Upload(self):

        with open("Persons_List.json", "r") as file:
            self.Data = json.load(file)
            print(self.Data)
            Person.Verify_Function(input("Enter the name of the person "))

    def Verify_Function(self, name):
        self.name = name
        if self.name in self.Data:
            Persons.Check_List(self)
        else:
            self.Data[self.name] = 0
            Persons.Check_List(self)

    def Check_List(self):
        score = input("Enter check score: ")
        self.score = int(score)
        Persons.Quastion_Function(self)

    def Quastion_Function(self):

        Quastion = input("Collect scores? ")

        if Quastion == "Yes":
            Persons.Score_Collection(self)
        elif Quastion == "No":
            Persons.Score_Spending(self)

    def Score_Collection(self):
        self.Data[self.name] += self.score * 0.1
        Persons.Jason_Download(self)

    def Score_Spending(self):

        if self.Data[self.name] > self.score:
            self.Data[self.name] = (self.Data[self.name] - self.score) * (self.Data[self.name] - self.score > 0)
            Persons.Jason_Download(self)
        else:
            self.cash = (self.score - self.Data[self.name]) * (self.score - self.Data[self.name] > 0)
            self.Data[self.name] = 0
            Persons.Jason_Download(self)

    def Jason_Download(self):

        with open("Persons_List.json", "w") as write_file:
            self.Data[self.name] = self.Data[self.name]
            json.dump(self.Data, write_file)


while True:
    #f = open('Persons_List.json', 'w')
    Person = Persons()
    Person.Jason_Upload()