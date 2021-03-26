field = "Pasquale"
fact = 30.747
y = 43.33333333
x = 200000434334444

# Complete the f-string
print(f"{field} create around {fact:.2f}% of the data but only {y:.1f}% is analyzed, "
      f"notazione scientifica: {x:e}, with quotes: {field!r}.")

print("------------------------------------------------------------")

list_links = [2, 4, 8, 9]
# Divide the length of list by 120 rounded to two decimals
print(f"Only {(len(list_links))*100/120:.2f}% of the posts contain links")
