file = input("Enter a file number, or 'all' to target all files")
amount = int(input("Enter the amount you want to change by"))
sign = input("Add or Subtract? (+/-)")


def change_file(file, amount, sign):
    with open(f"HoursFiles/hoursfile{file}.txt", "r") as f:
        lines = f.readlines()
        with open(f"HoursFiles/hoursfile{file}.txt", "w") as f:
            if sign == "+":
                lines[1] = str(int(lines[1][:-1]) + amount) + "\n"
            elif sign == "-":
                lines[1] = str(int(lines[1][:-1]) - amount) + "\n"
            f.writelines(lines)


if file == "all":
    for i in range(0, 65):
        change_file(str(i), amount, sign)
else:
    change_file(file, amount, sign)
