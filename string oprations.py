import array

a = "  soham soham  "
y = array.array("i", [1, 2, 3, 4, 5])
print(a.strip())
print(a.upper())
print(a.lower())
b = "valornt"
print(a.strip() + b)
c = 42
d = f"The value of c is {c}"
print(d)
e = f"the god of thunder {c} is thor"
print(e)
price = 59
txt = f"The price\b is {20*40:.2f} dollars"
print(txt)
z = "banana"
print(z.center(20, "~"))
print(bool("Hello"))
print(bool(15))
print(isinstance(price, int))
