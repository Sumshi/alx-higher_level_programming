#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4  # imports hidden_4 in the same directory
names = dir(hidden_4)  # displays all names in dir hidden_4
for name in names:  # iterates over the list
    if name[:2] != "__":  # name does not start with - -
        print(name)  # prints all names that do not start with --
