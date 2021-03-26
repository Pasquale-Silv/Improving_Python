nums = [2, 4, 6, 8, 10]

result = map(lambda a: a ** 2, nums)
print(result)
print(list(result))

print("-----------------------------------------")

# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda stringa: stringa + "!!!", spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list =  list(shout_spells)

# Print the result
print(shout_spells_list)