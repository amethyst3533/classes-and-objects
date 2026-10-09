class Job():
    name = ""
    age = 20
    years_of_experience = 2
    company_name = "Apple"
    worker_amount = 10
    #constructor- Called when object is created
    def __init__(self):
        print("Job interview")
    def change(self):
        self.name = input("What is your name? ")
        self.age = int(input("How old are you? "))
        self.company_name = input("What company do you work for? ")
        self.years_of_experience= int(input("How long have you worked for this company? "))
        self.worker_amount = input("How many colleagues do you have? ")
    def display(self):
        print(self.name)
        print(self.age)
        print(self.company_name)
        print(self.years_of_experience)
        print(self.worker_amount)

work = Job()
work.change()
work.display()