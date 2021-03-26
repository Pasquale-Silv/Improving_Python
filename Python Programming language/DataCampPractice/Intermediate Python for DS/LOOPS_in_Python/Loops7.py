# Looping over a dictionary dict:

world = { "afghanistan":30.55,
          "albania":2.77,
          "algeria":39.21 }

for key, value in world.items() :          # Also k. v
    print(key + " -- " + str(value))       # unordered

print('--------------------------')

# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for k, v in europe.items():
    print("the capital of " + k + " is " + v)

