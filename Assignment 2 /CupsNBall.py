x = {"Ball": "1"}

test = input("\nChanges: ")
a = test.upper()
b = list(a)

#first change
def changeAB():
    if x["Ball"] == "1":
        x["Ball"] = "2"
    elif x["Ball"] == "2":
        x["Ball"] = "1"

#second change
def changeBC():
    if x["Ball"] == "2":
        x["Ball"] = "3"
    elif x ["Ball"] == "3":
        x["Ball"] = "2"

#third change
def changeAC():
    if x["Ball"] == "1":
        x["Ball"] = "3"
    elif x["Ball"] == "3":
        x["Ball"] = "1"

#final change
for change in b:
    if change == "A":
        changeAB()
    elif change == "B":
        changeBC()
    elif change == "C":
        changeAC()
print("Final location of ball: ", x["Ball"])
