shout = lambda stringa : stringa + '!!!'
print(shout('Hello'))

expFunc = lambda x, y : x ** y
print(expFunc(2, 3))

calcoloL = lambda x, y, z : (x + y - 1) *z
print(calcoloL(1, 1, 10))

echo_word = lambda word1, echo: word1 * echo
result = echo_word('hey', 5)
print(result)

nums = [2, 4, 6, 8, 10]

result = map(lambda a: a ** 2, nums)