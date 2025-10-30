### SET
# this is one of the 4 built-in data types
#it is unordered, unchangeable and un-indexed
set1 = {"music", "football", "games"}
set2 = {"sicki", "santana", "dicey", "manuel", "football"}
print(type(set1))
print(set1)
set3 = set1 - set2
set5 = set2.difference(set1)
set6 = set1.symmetric_difference(set2)
print(set3)
print(set5)
print(set6)
set4 = set1.union(set2)
print(set4)
if 'santana' in set4:
    print(" SANTANA STILL DEY OH ")


### DICTIONARIES
# this is the last of the 4 built-in data types
# it is ordered, changeable and do not allow duplicates
Dict1 = {
    "brand": "iphone",
    "version": "iphone11",
    "year purchased": 2024
}
print(Dict1)
print(Dict1["version"])
print(len(Dict1))
print(Dict1.keys())
print(Dict1.values())
x = Dict1.items()
print(x)
Dict1["year purchased"]= 2025
print(x)
if "version" in Dict1:
  print("Yes, 'model' is one of the keys in the dictionary")
for x in Dict1:
    print(x)
for (x,y) in Dict1.items():
    print(f"{x,y}\n")

## Nested Dictionaries
myfam = {
    "  firstborn ": {
        "name": "Joy",
        "nickname": "Jenny"
    },
    "  secondborn ": {
        "name":  "Clare",
        "nickname": "Cutie"
    },
    "  thirdborn ": {
        "name":  "Christian",
        "nickname": "Snr Dice"
    },
    "  fourthborn ": {
        "name":  "Charity",
        "nickname": "Starity"
    },
    "  fifthborn ": {
        "name": "Emmanuel",
        "nickname": "Dice"
    },
    "  lastborn ": {
        "name":  "Victor",
        "nickname": "Dice ailes"
    },
}
#OB- order of birth
for p, OB in myfam.items():
    print(p)
    for name in OB:
        print(name + ':', OB[name])
