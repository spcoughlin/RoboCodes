import cv2
import numpy as np
import datetime

catCascade = cv2.CascadeClassifier('cascade.xml')

def interperet_code(c1, c2, gray):
    """
    Calculates the positions of all cells
    Scans cells and generates a string of the binary number
    """
    x_diff = abs(c2[0] - c1[0])

    row1 = [x_diff * 0.25, x_diff * 0.5, x_diff * 0.75, x_diff]
    row2 = [0, x_diff * 0.25, x_diff * 0.5, x_diff * 0.75]

    bin_str = ""
    for i in row1:
        x_val = c1[0] + int(i)
        y = c1[1]
        cv2.circle(gray, (x_val, y), 5, (255, 0, 0), 5)
        if np.any(gray[y, x_val] < 128):
            bin_str += "1"
        else:
            bin_str += "0"

    for i in row2:
        x_val = c1[0] + int(i)
        y = c2[1]
        cv2.circle(gray, (x_val, y), 5, (255, 0, 0), 5)
        if np.any(gray[y, x_val] < 128):
            bin_str += "1"
        else:
            bin_str += "0"

    return bin_str


def code_scanner():
    """
    Scans video feed for cat matches
    Gets positions of the centers of cats if 2 are detected
    Calls interperet_code
    """
    print("Video Starting...")
    video_capture = cv2.VideoCapture(0)
    print("Awaiting Code...")

    while True:
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cats = catCascade.detectMultiScale(
            gray,
            scaleFactor=1.015, # should be 1.01
            minNeighbors=5, # should be 4
        )

        for (x, y, w, h) in cats:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        if len(cats) >= 2:
            x, y, w, h = cats[0]
            c1 = [int((2 * x + w)/2), int((2 * y + h)/2)]

            x, y, w, h = cats[1]
            c2 = [int((2 * x + w)/2), int((2 * y + h)/2)]

            if c1[0] < c2[0]: # making sure c1 is the one on the left
                pass
            elif c1[0] > c2[0]:
                c1, c2 = c2, c1

            video_capture.release()
            cv2.destroyAllWindows()
            return int(interperet_code(c1, c2, gray), 2)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

def main():
    """
    Managing files and CLI
    """
    code = code_scanner()
    print(f'Code Found: {code}')

    with open(f'HoursFiles/hoursfile{code}.txt', 'r') as f:
        lines = f.readlines()
        f.close()

    if lines[0] != "None\n":
        clin = input(f"Welcome, {lines[0]}What would you like to do?\n1 - Clock In\n2 - Clock Out\n3 - Check Hours\n")

        try:
            clin = int(clin)
        except ValueError:
            print("Input was not an int!")

        if clin == 1:
            now = datetime.datetime.now().isoformat()

            with open('clockinlog.txt', 'a') as f:
                f.write(f"{str(code)}${now}\n")
                f.close()

            with open(f'HoursFiles/hoursfile{code}.txt', 'r') as f:
                lines = f.readlines()
                with open(f'HoursFiles/hoursfile{code}.txt', 'w') as f:
                    lines[2] = "1"
                    for i in lines:
                        f.write(i)
                    f.close()
                f.close()

            print(f"Clocked in at {now}")

        elif clin == 2:
            now = datetime.datetime.now()

            with open('clockinlog.txt', 'r') as f:
                logs = f.readlines()
                logs = logs[::-1]
                f.close()

            past = datetime.datetime.now() # failsafe
            with open(f'HoursFiles/hoursfile{code}.txt', 'r') as f:
                lines = f.readlines()

                for i in logs:
                    if int(i.split('$')[0]) == code and lines[2] == "1":
                        isostr = i.split('$')[1]
                        past = datetime.datetime.fromisoformat(isostr[:len(isostr) - 1])
                        break

                time_to_add = (now - past).total_seconds()
                time_to_add = time_to_add / 3600 # converting to hours
                hours = float(lines[1][:len(lines[1]) - 1])
                hours += time_to_add
                lines[1] = str(hours) + "\n"
                lines[2] = "0"

                with open(f'HoursFiles/hoursfile{code}.txt', 'w') as f:
                    f.writelines(lines)
                    f.close()
                f.close()

                with open(f'HoursFiles/hoursfile{code}.txt', 'r') as f:
                    lines = f.readlines()
                    print(f"Hours: {lines[1]}")

        elif clin == 3:
            with open(f'HoursFiles/hoursfile{code}.txt', 'r') as f:
                lines = f.readlines()
                print(f"Hours: {lines[1]}")

    elif lines[0] == "None\n":
        clin = input(f"Would you like to create a file for code # {code}?\n1 - Yes\n2 - No\n")

        try:
            clin = int(clin)
        except ValueError:
            print("Input was not an int!")

        if clin == 1:
            name = input("Enter Your Name: ")
            with open(f'HoursFiles/hoursfile{code}.txt', 'r') as f:
                lines = f.readlines()
                lines[0] = name + "\n"
                lines[1] = "0" + "\n"
                lines[2] = "0"
                with open(f'HoursFiles/hoursfile{code}.txt', 'w') as f:    
                    f.writelines(lines)
                    f.close()
                f.close()

            print(f"File created - Code:{code} User:{name}")

        elif clin == 2:
            pass

    clin = input("Would you like to run the program again?\n1 - Yes (Suggested)\n2 - No (Quit)\n")
    if clin == "1": main()
    if clin == "2": pass 


if __name__ == "__main__":
    main()
