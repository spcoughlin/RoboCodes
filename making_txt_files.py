import shutil

members = 65
lines = ["None\n", "None\n", "0"]
for i in range(members):
    with open(f'hoursfile{i}.txt', 'w') as f:
        f.writelines(lines)
        shutil.move(f"hoursfile{i}.txt", f"C:/HoursFiles/hoursfile{i}.txt")
        f.close()
