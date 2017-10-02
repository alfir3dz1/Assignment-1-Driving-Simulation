# Capital Letters according to the names given
alphabet = ['A', 'E', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']


def capital():
    for i in separate:
        if i in alphabet:
            print(i, end="")
    return

#Input according to the requirement
while True:
    endnames = input("\n End names: ")
    last_names = endnames.title()
    separate = list(last_names)
    print(end="")
    capital()
