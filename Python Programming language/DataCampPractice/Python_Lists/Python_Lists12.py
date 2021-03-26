"""
The Python code in the script already creates a list with the name areas and a copy named areas_copy.
Next, the first element in the areas_copy list is changed and the areas list is printed out.
If you hit Run Code you'll see that,
although you've changed areas_copy,
the change also takes effect in the areas list.
That's because areas and areas_copy point to the same list.

If you want to prevent changes in areas_copy from also taking effect in areas,
you'll have to do a more explicit copy of the areas list.
You can do this with list() or by using [:].
"""

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = areas      # Qui bisogna usare list(areas) oppure areas[:] per non condizionarla con l'altra lista

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)

print("Prova con list():")
areas_copy2 = list(areas)    # oppure areas[:]

areas_copy2[0] = 300

print(areas_copy2)
print(areas)

"""
Nice! 
The difference between explicit and reference-based copies is subtle, 
but can be really important. 
Try to keep in mind how a list is stored in the computer's memory.
"""