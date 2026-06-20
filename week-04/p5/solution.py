numbers = input("enter a number:")
seen = set()
duplicates = set()
for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
print("Duplicates:", list(duplicates))
