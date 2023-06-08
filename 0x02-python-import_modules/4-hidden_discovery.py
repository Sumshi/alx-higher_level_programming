#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4  # imports hidden_4 in the same directory
    names = [name for name in dir(hidden_4) if not name.startswith('__')]
    for name in sorted(names):  # sort in alphabeticall order
        print(name)
