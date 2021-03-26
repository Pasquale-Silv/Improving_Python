a = "this is a string"
a = a.split(" ")                  # a is converted to a list of strings.
print(a)

a = "-".join(a)
print(a)

print("------------------------")

def split_and_join(line):
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
