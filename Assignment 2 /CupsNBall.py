location = {"x(ball)": "1"}

test = input("\nChanges: ")
a = test.upper()
b = list(a)

#first change
def changeAB():
    if location["x(ball)"] == "1":
        location["x(ball)"] = "2"
    elif location["x(ball)"] == "2":
        location["x(ball)"] = "1"

#second change
def changeBC():
    if location["x(ball)"] == "2":
        location["x(ball)"] = "3"
    elif location ["Ball"] == "3":
        location["x(ball)"] = "2"

#third change
def changeAC():
    if location["x(ball)"] == "1":
        location["x(ball)"] = "3"
    elif location["x(ball)"] == "3":
        location["x(ball)"] = "1"

#final change
for change in b:
    if change == "A":
        changeAB()
    elif change == "B":
        changeBC()
    elif change == "C":
        changeAC()
print("Final location of ball: ", location["x(ball)"])
