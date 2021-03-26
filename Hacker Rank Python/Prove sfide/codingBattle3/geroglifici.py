# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

'''

numSeq = int(input())
sequenze = []

for i in range(numSeq):
    lungSeq = int(input())
    sequenza = list(map(int, input().strip().split()))
    sequenze.extend(sorted(sequenza))
sequenze.sort()
sequenze = set(sequenze)
sequenze = " ".join(map(str, sorted(list(sequenze))))
print(sequenze)
