with open ("teams.txt", "w") as file:
    for n in ["Chelsea", "Dinamo", "Arsenal"]:
        newline = n + "\n"
        file.write(newline)

file.close

file = open ("teams.txt", "r")
breakpoint()
files = file.readline

print(files[0], files[3])
