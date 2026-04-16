from fuzzywuzzy import fuzz

def date_input(schedules):
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    print("Welcome")
    print("Share with me what your next week schedules:\n")

    learn_time = int(input("enter your "))


    return schedules

def schedules_

def information_unity():

    print("enter your units:")
    unit = input()




def about_you(choose):


def free_timescale():
    pass

def history():

    pass


def relevant_units(choose):
    pass


def welcome():
    pass

def main():
    schedule = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0 ,0, 0, 0], # ראשון
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0 ,0, 0, 0], # שני
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0 ,0, 0, 0], # שלישי
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0 ,0, 0, 0], # רביעי
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0 ,0, 0, 0], # חמישי
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0 ,0, 0, 0], # שישי
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0 ,0, 0, 0]  # שבת
    ]

    test_score = [
    [], # Mathematics
    [], # English
    [], # Hebrew Language
    [], # Bible Studies
    [], # History
    [], # Civics
    [], # Literature
    []  # Physical Education
    ]

    print("welcome to dell_project")
    while True:
        choice = input("enter your choice \n1 - tests scors \n2 - schedule \n3 - units \n4 - quit")
        if choice == "1":
            for i in range(len(test_score)):
                if len(test_score) == 0:
                    print("your have no updated test")
                else:
                    print(tests)
        if choice == "2":
            choice = input("enter your choice \n1 - free time \n2 - full schedule")
            if choice == "1":
                print(free_timescale(schedule))

            if choice == "2":
                print(schedule)

        if choice == "3":
            if len(units) == 0:
                 school_units = information_unity()
            else:
                print(school_units)
        if choice == "4":
            break

    print("Thank you for using this program")