#Practice Program
#Take two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
dupes = []
counter = 0
for x in a:
    if x in b:
        if a[counter] not in dupes:
            dupes.append(a[counter])
    counter += 1

print(dupes)