search = input("Enter a name to search for")

for i in range(0, 65):
    with open(f"HoursFiles/hoursfile{i}.txt", "r") as f:
        line = f.readline()
        if line.__contains__(search):
            print(f"{search} was found in file {i}")