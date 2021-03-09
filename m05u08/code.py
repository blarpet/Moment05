file = 'score.txt'
list = []

with open(file) as f:
    for rad in f:
        if len(rad) >  1:
            list.append(int(rad))

list.sort()

print(f"The whole list sorted: {list}")
print(f"The amount of results in the list is {len(list)}")
print(f"Medium is of all results: {sum(list)/len(list)}")
