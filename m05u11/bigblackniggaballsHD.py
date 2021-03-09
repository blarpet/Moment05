capital = 10000
interest = 1.03
year = 0
finalValue = 10000

with open("data.txt", "w") as fw:

    while year < 16:
        fw.write(f"Account has the value of {finalValue} kr. \nThere has been {year} years.\n\n")
        finalValue = capital*interest
        interest = interest*1.03
        year += 1

print(finalValue)