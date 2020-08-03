# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods 
#and try them out here. Endeavor to copy the link without the first # comment sign beginning it.


string = "chino the good boy"
a = string.capitalize()
print (a)

b = string.encode(encoding="utf-8", errors="strict")
print(b)

c = string.count("o")
print (c)

d = string.endswith("you")
print (d)

print (string.find("t"))

print (string.expandtabs(16))

print ("{} makes us proud".format(string))

print (string.index("g"))

print(string.split())

print (string.isdigit())

print (string.replace(("chino"),("Daniel")))
