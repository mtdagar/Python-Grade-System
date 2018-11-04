# initializing some globals
dictMarks = {}

maxEng = 0
engTop = int()

maxMath = 0
mathTop = int()

maxHist = 0
histTop = int()

maxScience = 0
scienceTop = int()


x = input("Create a new record? (Y/N)")
if x == "Y":
    running = True
else:
    print("Bye then")
    running = False


while running:
    roll = int(input("Enter your roll no"))
    eng = int(input("Enter marks in English"))
    math = int(input("Enter marks in Math"))
    history = int(input("Enter marks in History"))
    science = int(input("Enter marks in science"))

    percentage = (eng + math + history + science)/4

    dictMarks.update({roll: {"English": eng, "Math": math, "History": history, "Science": science, "Total Percentage": percentage}})

    print("Record Created!")

    x = input("Create a new record? (Y/N)")
    if x == "Y" : running = True
    else : running = False

print("\n\n")

for the_key in dictMarks.keys():
    print("Roll no: " + str(the_key))
    for key, value in dictMarks[the_key].items():
        # idk how to switch in python
        if key == "English":
            if value > maxEng:
                maxEng = value
                engTop = the_key

        if key == "Math":
            if value > maxMath:
                maxMath = value
                mathTop = the_key

        if key == "History":
            if value > maxHist:
                maxHist = value
                histTop = the_key

        if key == "Science":
            if value > maxScience:
                maxScience= value
                scienceTop = the_key

        print(key, ' : ', str(value))
    print("\n")

print("English topper: roll no " + str(engTop))
print("Math topper: roll no " + str(mathTop))
print("History topper: roll no " + str(histTop))
print("Science topper: roll no " + str(scienceTop))
