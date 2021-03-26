if __name__ == '__main__':
    n = int(input())                               # Questa è inutile!
    integer_list = map(int, input().split())
    print(integer_list)
    tuple_int = tuple(integer_list)
    print(tuple_int)

    print("Hash delle tupla di interi:")
    print(hash(tuple_int))
