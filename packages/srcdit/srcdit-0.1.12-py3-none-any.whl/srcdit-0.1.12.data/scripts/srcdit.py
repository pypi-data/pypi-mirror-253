import sys
import subprocess
import os

from colorama import Fore


def key_value_edit(file, key_value):
    if not os.path.isfile(file):
        print(
            Fore.RED
            + "File "
            + Fore.BLUE
            + file
            + Fore.RED
            + " not found. Did you misspell?"
        )
        exit()

    try:
        key, value = key_value.split("=")
    except ValueError:
        print(Fore.RED + "Incorrect syntax\nFile left unchanged")
        return

    try:
        int(value)
    except ValueError:
        value = f'"{value}"'

    with open(file, "r") as f:
        data = f.read()
        lines = data.split("\n")

        for i in range(len(lines)):
            if lines[i].find(key) != -1:
                print(Fore.RESET + "Found line with given key - " + Fore.BLUE + key)
                front, _ = lines[i].split(key)
                lines[i] = front + f"{key}={value}"
                break

        else:
            print(Fore.BLUE + key + Fore.YELLOW + " not found")

            while True:
                yes_no = input(Fore.RESET + "Add new? (y/n)\n")

                if yes_no.lower() in ["yes", "y"]:
                    lines.append(f"{key}={value}")
                    break

                elif yes_no.lower() in ["no", "n"]:
                    print(Fore.RED + "File unchanged")
                    return

                else:
                    print(Fore.RED + "Invalid input. Please enter yes/no")

    with open(file, "w") as f:
        data = "\n".join(lines)
        f.write(data)
        print(Fore.GREEN + "File changed")

    print(Fore.RESET + "", end="")


def main():
    if len(sys.argv) != 3:
        print("Invalid arguments")
        return

    key_value_edit(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
