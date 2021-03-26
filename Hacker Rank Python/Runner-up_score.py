if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(sorted(arr)[-2])

"""
5
2 3 6 6 5

Expected Output: 5
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arrSet = set(arr)

    print(sorted(arrSet)[-2])

print("Poichè :")
print("Lista: ", arr)
print("Set: ", arrSet)
