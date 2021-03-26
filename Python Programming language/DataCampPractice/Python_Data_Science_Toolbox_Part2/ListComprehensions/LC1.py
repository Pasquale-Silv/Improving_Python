nums = [12, 8, 21, 3, 16]; new_nums1 = []          # Puoi usare ; per separare istruzioni sulla stessa riga di codice
for num in nums:
    new_nums1.append(num + 1)

print(nums)
print(new_nums1)

print("-------------------------\nCon List Comprehensions (LC): ")

new_nums2_LC = [num + 1 for num in nums]
print(new_nums2_LC)

confronto_for_LC = new_nums1 == new_nums2_LC
print("Confronto tra le liste generate con for/LC: '{}', sono uguali, solo che LC lo fa in una riga di codice!".format(confronto_for_LC))

print([x ** 2 for x in nums])

print("------------------------------------")

print(list(range(0, 11)))

LC1 = [x for x in range(11)]
print(LC1)