members = 65
lines = ["None\n", "None\n", "0"]
for i in range(members):
    with open(f'hoursfile{i}.txt', 'w') as f:
        f.writelines(lines)
        f.close()
