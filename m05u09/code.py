import pprint
pp = pprint.PrettyPrinter(indent=2)

l_res = []
with open("score.txt") as f:
    for rad in f:
        rad = rad.strip()
        rad = rad.split("|")
        d = {"name": rad[0], "points": int(rad[1])}
        l_res.append(d)
    
print("Sorterad Lista:")
pp.pprint(sorted(l_res, key=lambda i: i["points"], reverse=True))
