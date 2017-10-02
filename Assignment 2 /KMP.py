# Capital Letters according to the names
alphabet = ['A', 'E', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']


def capital():
    for a in separate:
        if a in alphabet:
            print(a, end="")
    return

#Input according to the requirement
while True:
    endnames = input("\n End names: ")
    last_names = endnames.title()
    separate = list(last_names)
    print("Output: ", end="")
    capital()
