nums = (3, 4, 6)
print(nums)
print(type(nums))
# nums[0] = 2 (INVALID - 'tuple' object does not support item assignment)
# La tupla è una lista di oggetti immodificabili, non puoi cambiare gli elementi all'interno di essa.

# Unpack nums into num1, num2, and num3
num1, num2, num3 = nums           # Assegna gli elementi della tupla alle variabili indicate
print(num1)
print(num2)
print(num3)

# Construct even_nums
even_nums = (2, 4, 6)
print(even_nums)

