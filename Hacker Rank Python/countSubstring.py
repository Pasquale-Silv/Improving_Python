# ABCDCDC
# CDC

def count_substring(string, sub_string):
    contatore = 0
    for i in range(len(string)):
        print("stringa filtered:", string[i:len(sub_string)+i])
        print(sub_string)
        if string[i:len(sub_string)+i] == sub_string:
            contatore += 1
    return contatore


if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"

    count = count_substring(string, sub_string)
    print(count)

print("----------------------------")


def count_substring(string, sub_string):
    contatore = 0
    for i in range(len(string)):
        if string[i:len(sub_string) + i] == sub_string:
            contatore += 1
    return contatore


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
